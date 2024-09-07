from machine import Pin, ADC
NODEMCU_ESP8266 = 'nodemcu_esp8266'
PICO_RP2 = 'pico_rp2'

class Board:
    ON_BOARD_LED_PIN = None
    ANALOG_PIN = None
    def __init__(self, board: string):
        if board == 'nodemcu_esp8266':
            print("configuring", board)
            self.ON_BOARD_LED_PIN = Pin(2, Pin.OUT)
            self.ANALOG_PIN = ADC(0)
        elif board == 'pico_rp2':
            print("configuring", board)
            self.ON_BOARD_LED_PIN = Pin(25, Pin.OUT)
            self.ANALOG_PIN = ADC(Pin(26))

        print(self)

