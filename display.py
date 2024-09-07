from time import sleep
import epd2in9 as epd

# This is just an abstraction around epd tbh
# To give myself the option to support multiple display sizes, colors, etc
# but for now, it's an inconvenient way to access the epd lol

class Display:
    def __init__(self, board):
        raise "Not Implemented"

    def clear_display(self):
        raise "Not Implemented"

    def display_frame(self, image):
        raise "Not Implemented"

    def dims(self):
        raise "Not Implemented"

class Epd2in9(Display):
    def __init__(self, board):
        self.epd = epd.EPD_2in9_Landscape(
            spi=board.SPI_INT,
            cs=board.CS_PIN,
            dc=board.DC_PIN,
            rst=board.RST_PIN,
            busy=board.BUSY_PIN,
            )
        self.epd.init()

    def clear_display(self):
        self.epd.Clear(0xff)

    def display_frame(self, image):
        self.epd.display(image)

    def dims(self):
        return self.epd.width, self.epd.height

