import framebuf
import json
from display import Display

class Emoji:
    # TODO: Use to-fb here
    Happy = None 

# y addr's start at 6 bc of memory layout
Y_START = 6
class DisplayGui:
    def __init__(self, display: Display):
        self.disp = display

    def _new_frame_buffer(self):
        width, height = self.disp.dims()
        buf = bytearray(width * height // 8)
        return framebuf.FrameBuffer(buf, width, height, framebuf.MONO_HLSB), buf

    def render_hello_world(self):
        from hello_world_dark import hello_world_dark
        self.disp.clear_display()
        self.disp.display_frame(hello_world_dark)

    # TODO: Add more stuff here (e.g. widget to display moisture in a corner somewhere)
    def render(
        self,
        emoji,
        text: str
        ):
        fb, buf = self._new_frame_buffer()
        fb.fill(0xff)

        fb.text(text, 2, Y_START + 2, 0x0)
        self.disp.display_frame(buf)
        print("displayed frame")
