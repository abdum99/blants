import network
import usocket as socket

import config
import blants

# debug
import esp
esp.osdebug(None)

import gc
gc.collect()

def setup_wifi():
# set access point
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.active(True)         # activate the interface
    ap.config(essid=config.WIFI_SSID, password=config.WIFI_PASSWORD) # set the SSID of the access point
    # wait for it to start
    while ap.active() == False:
        pass

    print("wifi up. addr:", ap.ifconfig())

def setup_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # timeout in 5 minutes
    sock.settimeout(300) 
    sock.bind(('', 80))
    print("socket bound to:", )
    sock.listen(5)

    conn, addr = sock.accept()
    print("got connection from", str(addr))

    request = conn.recv(1024)
    print("received:", request)


if __name__ == '__main__':
    # network setup
    setup_wifi()
    # setup_server()

    # blants setup
    blant = blants.Blants()
    blant.run()
