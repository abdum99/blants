from blants import Blants
import config

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

    # runs for a max of 5 minutes
    def _serve(self):
        try:
            while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # timeout in 5 minutes
                sock.settimeout(3) 
                sock.bind(('', 80))
                print("socket bound to:", )
                sock.listen(5)

                conn, addr = sock.accept()
                print("got connection from", str(addr))

                cmd = conn.recv(1024)
                print("received:", cmd)
                if len(cmd) == 0:
                    break

                _process_cmd(cmd)
        except Exception as e:
            print("Exception:", e)

    def serve(self):
        self._serve()

    def _process_cmd(cmd: str):
        tokens = cmd.split()
        if token[0] == "get":
            _process_get()

    def _process_get(tokens: str[]):
