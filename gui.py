import framebuf
from display import Display

class Emoji:
    def __init__(self, dat):
        self.data = dat

    def Good():
        return Emoji("good.dat")

    def Angry():
        return Emoji("angry.dat")

    def Confused():
        return Emoji("confused.dat")
        
    def Dehydrated():
        return Emoji("dehydrated.dat")

    def Sleepy():
        return Emoji("sleepy.dat")

# y addr's start at 6 bc of memory layout
Y_START = 6
TOP_BAR_TEXT_START_X = 5
TOP_BAR_TEXT_Y = 5
TOP_BAR_LINE_Y = 20
EMOJI_START_X = 5
EMOJI_START_Y = 40
TEXT_START_X = 150
TEXT_MAX_WIDTH
TEXT_MAX_HEIGHT = 50
class BlantsGui:
    def __init__(self, disp: Display):
        self.disp = disp

    # TODO: Add more stuff here (e.g. widget to display moisture in a corner somewhere)
    def render(
        self,
        text,
        emoji=None,
        topbar=None
    ):
        lines = text.splitlines()
        if len(lines) > 5:
            raise Exception("too many lines")

        # display text
        y_padding = 0
        for l in lines:
            if len(l) > 16:
                raise Exception("line too long")

            self.disp.text(l, TEXT_START_X, TEXT_START_Y + y_padding, 0x00)

            y_padding += 10

        if emoji != None:
            if not isinstance(emoji, Emoji):
                raise Exception("bad emoji")

            with open(emoji.data, 'rb') as em_bytes:
                print("reading emoji data for", emoji, emoji.data)
                em_buf = framebuf.FrameBuffer(bytearray(em_bytes.read()), 128, 80, framebuf.MONO_HLSB)
                print("read", em_buf)
                self.disp.blit(em_buf, EMOJI_START_X, EMOJI_START_Y)

        if topbar != None:
            self.disp.hline(0, TOP_BAR_LINE_Y, self.disp.dims()[1] - 1, 0x00)
            self.disp.text(topbar, TOP_BAR_TEXT_START_X, TOP_BAR_TEXT_Y, 0x00)

        self.disp.show()
