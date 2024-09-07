import machine
import esp
from time import sleep
from board import Board, NODEMCU_ESP8266 
import sys
# from umqtt.simple import MQTTClient

from config import MOISTURE_LEVEL_LIQUID, MOISTURE_LEVEL_DRY, MOISTURE_LEVEL_MIN_THRES, MOISTURE_LEVEL_MAX_THRES, BLANTS_SLEEP_PERIOD_MSEC, WATER_PUMP_SLEEP_PERIOD_SEC, WATER_PUMP_WATER_PERIOD_SEC, BLANTS_DEEPSLEEP_PERIOD_MSEC 


def should_water(measurement):
    return measurement < MOISTURE_LEVEL_MIN_THRES


class Blants:
    def __init__(self):
        self.board = Board(NODEMCU_ESP8266)
        self.adc = self.board.ANALOG_PIN
        self.led = self.board.ON_BOARD_LED_PIN

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

    def blink(self, interval=0.2):
        self.led.on()
        sleep(interval)
        self.led.off()
        sleep(interval)


    def measure_moisture(self):
        measurements = []
        for _ in range(5):
            val = self.adc.read_u16()
            print("val:", val)
            measurements.append(val)
            self.blink(interval=0.5)

        raw_val = sum(measurements) / len(measurements)

        if raw_val < MOISTURE_LEVEL_LIQUID:
            return MOISTURE_LEVEL_LIQUID
        return 100 * (1 - ((raw_val - MOISTURE_LEVEL_LIQUID) / (MOISTURE_LEVEL_DRY - MOISTURE_LEVEL_LIQUID)))

    def sprinkle(self):
        # TODO:
        print("watering; water pump on")
        self.board.WATER_PUMP_PIN.on()
        sleep(WATER_PUMP_WATER_PERIOD_SEC)
        self.board.WATER_PUMP_PIN.off()
        print("water pump off")

    def water(self):
        while self.measure_moisture() < MOISTURE_LEVEL_MAX_THRES:
            # blink 5 times
            for _ in range(5):
                self.blink(interval=0.1)

            self.sprinkle()
            sleep(WATER_PUMP_SLEEP_PERIOD_SEC)


    def run(self):
        self.board.ON_BOARD_LED_PIN.off()
        while True:
            measurement = self.measure_moisture()
            print("Moisture:", measurement, "%")
            if should_water(measurement):
                print("watering...")
                self.water()
                print("done watering")
                continue

            #put the device to sleep
            # print("going into deep sleep")
            # #configure RTC.ALARM0 to be able to wake the device
            # self.rtc = machine.RTC()
            # self.rtc.irq(trigger=self.rtc.ALARM0, wake=machine.DEEPSLEEP)
            # # # set RTC.ALARM0 to fire after Xmilliseconds, waking the device
            # self.rtc.alarm(self.rtc.ALARM0, BLANTS_SLEEP_PERIOD_MSEC)
            # # # sleep
            # machine.deepsleep(2000)
            print("sleeping...")
            esp.deepsleep(BLANTS_DEEPSLEEP_PERIOD_MSEC)
            sleep(5)


if __name__ == '__main__':
    blants = Blants()
    blants.run()
