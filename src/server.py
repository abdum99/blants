from blants import Blants
import config
from time import sleep

import network
import usocket as socket

class BlantServer:
    def __init__(self, blants: Blants):
        self.blants = blants

    def _setup_wifi(self):
# set access point
        ap = network.WLAN(network.AP_IF) # create access-point interface
        ap.active(True)         # activate the interface
        ap.config(essid=config.WIFI_SSID, password=config.WIFI_PASSWORD) # set the SSID of the access point
        # wait for it to start
        while ap.active() == False:
            pass

        print("wifi up. addr:", ap.ifconfig())

    def _double_blink(self):
        self.blants.blink(interval=0.1)
        self.blants.blink(interval=0.1)

    # runs for a max of 5 minutes
    def _serve(self):
        try:
            while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # timeout in 5 minutes
                sock.settimeout(config.SERVER_TIMEOUT) 
                sock.bind(('', 80))
                print("socket bound to:", )
                sock.listen(5)

                conn, addr = sock.accept()
                print("got connection from", str(addr))
                self._double_blink()

                cmd = conn.recv(1024)
                print("received:", cmd)
                if len(cmd) == 0:
                    break

                self._process_cmd(conn, cmd)
        except Exception as e:
            print("Exception:", e)

    def serve(self):
        self._serve()

    def _process_cmd(self, conn, cmd):
        tokens = cmd.split()
        if tokens[0] == "GET":
            self._process_get(conn, tokens)
        elif tokens[0] == "PUT":
            self._process_put(conn, tokens)

    def _process_get(self, conn, tokens):
        if len (tokens) < 2:
            print("Bad command.")
            conn.send("ERR: Bad command.")
            return
        
        if tokens[1] == "moisture":
            moisture = self.blants.measure_moisture()
            conn.send(f"OK: moisture:{moisture}%")


    def _process_put(self, conn, tokens):
        if len(tokens) < 3:
            print("Bad command.")
            conn.send("ERR: Bad command.")
            return

        if tokens[1] == "water" and tokens[2] == "on":
            conn.send("OK: watering..")
            self.blants.sprinkle()
            
