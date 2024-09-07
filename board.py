from machine import Pin, ADC, SPI
NODEMCU_ESP8266 = 'nodemcu_esp8266'
PICO_RP2 = 'pico_rp2'

class Board:
    ON_BOARD_LED_PIN = None
    WATER_PUMP_PIN = None
    ANALOG_PIN = None

    # spi
    SPI_INT = None

    # pins used by epaper -- wiring dependent
    CS_PIN = None
    DC_PIN = None
    RST_PIN = None
    BUSY_PIN = None
    def __init__(self, board):
        if board == 'nodemcu_esp8266':
            print("configuring", board)
            self.ON_BOARD_LED_PIN = Pin(2, Pin.OUT)
            self.WATER_PUMP_PIN = Pin(4, Pin.OUT)
            self.ANALOG_PIN = ADC(0)

            # spi
            # TODO: check if I can change baudrate to something higher
            self.SPI_INT = SPI(0)
            self.CS_PIN = Pin(15, Pin.OUT)
            self.DC_PIN = Pin(1, Pin.OUT)
            self.RST_PIN = Pin(3, Pin.OUT)
            self.BUSY_PIN = Pin(5, Pin.OUT)
        elif board == 'pico_rp2':
            print("configuring", board)
            self.ON_BOARD_LED_PIN = Pin(25, Pin.OUT)
            self.ANALOG_PIN = ADC(Pin(26))
            raise "Need more config"

        print(self)

