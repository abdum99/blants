from time import sleep
import framebuf
import epd2in9 as epd

# This is just an abstraction around epd tbh
# To give myself the option to support multiple display sizes, colors, etc
# but for now, it's an inconvenient way to access the epd lol

class Display(framebuf.FrameBuffer):
    def __init__(self, board):
        raise "Not Implemented"

    def show(self):
        raise "Not Implemented"
    def clear_display(self):
        raise "Not Implemented"

    def display_frame(self, image):
        raise "Not Implemented"

    def dims(self):
        raise "Not Implemented"


class Epd2in9Display(epd.EPD_2in9_Landscape):
    def __init__(self, board):
        super().__init__(
            spi=board.SPI_INT,
            rst=board.RST_PIN,
            busy=board.BUSY_PIN,
            cs=board.CS_PIN,
            dc=board.DC_PIN,
        )
        self.Clear(0xff)
        self.fill(0xff)
        self.display_Base(self.buffer)

    def show(self):
        self.display_Partial(self.buffer)

    def clear_display(self):
        self.Clear(0xff)

    def dims(self):
        return self.width, self.height

