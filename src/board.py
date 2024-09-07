from machine import Pin, ADC, SPI
WEMOS_D1MINI_ESP8266 = 'wemos_d1mini_esp8266'
NODEMCU_ESP32 = 'nodemcu_esp32'
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
        print("configuring", board)
        if board == WEMOS_D1MINI_ESP8266:
            self.ON_BOARD_LED_PIN = Pin(2, Pin.OUT)
            self.ANALOG_PIN = ADC(0)
            # self.WATER_PUMP_PIN = Pin(4, Pin.OUT)
            #
            # # spi
            # # TODO: check if I can change baudrate to something higher
            # self.SPI_INT = SPI(0)
            # self.CS_PIN = Pin(15, Pin.OUT)
            # self.DC_PIN = Pin(1, Pin.OUT)
            # self.RST_PIN = Pin(3, Pin.OUT)
            # self.BUSY_PIN = Pin(5, Pin.IN)
            raise "Need more config"
        elif board == NODEMCU_ESP32:
            self.ON_BOARD_LED_PIN = Pin(2, Pin.OUT)
            self.WATER_PUMP_PIN = Pin(4, Pin.OUT)
            self.ANALOG_PIN = ADC(0)

            # spi
            # TODO: check if I can change baudrate to something higher
            # self.SPI_INT = SPI(1, baudrate=10000000busy, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(14), mosi=Pin(13))
            self.SPI_INT = SPI(1)
            self.CS_PIN = Pin(23, Pin.OUT)
            self.DC_PIN = Pin(22, Pin.OUT)
            self.RST_PIN = Pin(19)
            self.BUSY_PIN = Pin(21, Pin.IN)
        elif board == PICO_RP2:
            self.ON_BOARD_LED_PIN = Pin(25, Pin.OUT)
            self.ANALOG_PIN = ADC(Pin(26))
            raise "Need more config"

        print(self)

