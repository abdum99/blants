import framebuf
import display as disp

class Emoji:
    # TODO: Use to-fb here
    Happy = None 

# y addr's start at 6 bc of memory layout
Y_START = 6
class DisplayGui:
    def __init__(self, display: disp.Display):
        self.disp = display

    def _new_frame_buffer(self):
        width, height = self.disp.dims()
        buf = bytearray(width * height // 8)
        return framebuf.FrameBuffer(buf, height, width, framebuf.MONO_VLSB), width, height

    # TODO: Add more stuff here (e.g. widget to display moisture in a corner somewhere)
    def render(
        self,
        emoji: Emoji,
        text: str
        ):
        fb, width, height = self._new_frame_buffer()
        fb.fill(0)

        fb.text(text, 2, Y_START + 2, 0xffff)
        # def set_frame_memory(self, image, x, y, w, h):
        self.disp.set_frame_memory(fb, 0, 0, width, height)
        self.disp.display_frame()
