from machine import ADC, Pin
import time
from board import Board, NODEMCU_ESP8266 
import sys
# from umqtt.simple import MQTTClient
import config

MOISTURE_LEVEL_DRY = 58000
MOISTURE_LEVEL_LIQUID = 30000

board = Board(NODEMCU_ESP8266)

class Blants:
    def __init__(self):
        self.adc = board.ANALOG_PIN
        self.led = board.ON_BOARD_LED_PIN

    #     self._setup()
        self._do_prechecks()

    # def _setup(self):
    #     try:
    #         # setup mqtt
    #         self.mqtt = MQTTClient(
    #             client_id=config.MQTT_CLIENT_ID,
    #             server=config.MQTT_BROKER_HOST
    #         )

        if not self._do_prechecks():
            print("prechecks failed; soft rebooting...")
            sys.exit()

    def _do_prechecks(self):
        if self.adc == None:
            print("ADC is None..")
            return False

        if self.led == None:
            print("led is None...")
            return False

        return True


    def run(self):
        while True:
            print("Moisture:", self.measure_moisture(), "%")
            time.sleep(2)

    def measure_moisture(self):
        measurements = []
        for _ in range(10):
            val = self.adc.read_u16()
            print("val:", val)
            measurements.append(val)
            self.led.on()
            time.sleep(0.5)
            self.led.off()
            time.sleep(0.5)

        raw_val = sum(measurements) / len(measurements)

        if raw_val < MOISTURE_LEVEL_LIQUID:
            return MOISTURE_LEVEL_LIQUID
        return 1 - ((raw_val - MOISTURE_LEVEL_LIQUID) / (MOISTURE_LEVEL_DRY - MOISTURE_LEVEL_LIQUID))


if __name__ == '__main__':
    blants = Blants()
    blants.run()
