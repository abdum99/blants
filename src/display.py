from time import sleep
import framebuf
import epd2in9 as epd

# This is just an abstraction around epd tbh
# To give myself the option to support multiple display sizes, colors, etc
# but for now, it's an inconvenient way to access the epd lol

class Display(framebuf.FrameBuffer):
    def __init__(self, _):
        return None

    def show(self):
        return None

    def clear_display(self):
        return None

    def display_frame(self, _):
        return None

    def dims(self):
        return None, None

class Epd2in9Display(Display, epd.EPD_2in9_Landscape):
    def __init__(self, board):
        epd.EPD_2in9_Landscape.__init__(
            self,
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

def create_display(display_name, board) -> Display | None:
    if display_name == "waveshare_epd2in9":
        return Epd2in9Display(board)

    else:
        return None
