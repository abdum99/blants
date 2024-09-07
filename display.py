import epaper2in9 as epd

# This is just an abstraction around epd tbh
# To give myself the option to support multiple display sizes, colors, etc
# but for now, it's an inconvenient way to access the epd lol
class Display:
    def __init__(self, board):
        self.epd = epd.EPD(
            spi=board.SPI_INT,
            cs=board.cs,
            dc=board.dc,
            rst=board.rst,
            busy=board.busy,
            )

    def set_frame_memory(self, image, x, y, w, h):
        self.epd.set_frame_memory(image, x, y, w, h)

    def display_frame(self):
        self.epd.display_frame()

    def dims(self):
        return self.epd.width, self.epd.height
