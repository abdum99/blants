import machine
from time import sleep
from board import Board, NODEMCU_ESP8266 
import sys
# from umqtt.simple import MQTTClient

from config import MOISTURE_LEVEL_LIQUID, MOISTURE_LEVEL_DRY, MOISTURE_LEVEL_MIN_THRES, MOISTURE_LEVEL_MAX_THRES, BLANTS_SLEEP_PERIOD_MSEC, WATER_PUMP_SLEEP_PERIOD


def should_water(measurement):
    return measurement < MOISTURE_LEVEL_MIN_THRES


class Blants:
    def __init__(self):
        self.board = Board(NODEMCU_ESP8266)
        self.adc = self.board.ANALOG_PIN
        self.led = self.board.ON_BOARD_LED_PIN

        #configure RTC.ALARM0 to be able to wake the device
        self.rtc = machine.RTC()
        self.rtc.irq(trigger=self.rtc.ALARM0, wake=machine.DEEPSLEEP)

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

    def blink(self):
        self.led.on()
        sleep(0.2)
        self.led.off()
        sleep(0.2)


    def measure_moisture(self):
        measurements = []
        for _ in range(5):
            val = self.adc.read_u16()
            print("val:", val)
            measurements.append(val)
            self.blink()

        raw_val = sum(measurements) / len(measurements)

        if raw_val < MOISTURE_LEVEL_LIQUID:
            return MOISTURE_LEVEL_LIQUID
        return 1 - ((raw_val - MOISTURE_LEVEL_LIQUID) / (MOISTURE_LEVEL_DRY - MOISTURE_LEVEL_LIQUID))


    def _water(self):
        while self.measure_moisture() < MOISTURE_LEVEL_MAX_THRES:
            print("watering; water pump on")
            sleep(1)
            print("water pump off")
            sleep(WATER_PUMP_SLEEP_PERIOD)


    def run(self):
        while True:
            measurement = self.measure_moisture()
            print("Moisture:", measurement * 100, "%")
            if should_water(measurement):
                print("watering...")
                self._water()
                print("done watering")
                continue

            print("going into deep sleep")
            #put the device to sleep
            # set RTC.ALARM0 to fire after Xmilliseconds, waking the device
            self.rtc.alarm(self.rtc.ALARM0, BLANTS_SLEEP_PERIOD_MSEC)
            machine.deepsleep()


if __name__ == '__main__':
    blants = Blants()
    blants.run()
