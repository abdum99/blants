import epaper2in9 as epd
class Display:
    def __init__(self, board):
        self.board = board
        self.epd = epd.EPD(
            spi=self.board.SPI_INT,
            cs=self.board.cs,
            dc=self.board.dc,
            rst=self.board.rst,
            busy=self.board.busy,
    )
