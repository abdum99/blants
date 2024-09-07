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


def map_point(val, s_min, s_max, t_min, t_max):
    return int(((val - s_min) / (s_max - s_min)) * (t_max - t_min)) + t_min

COLOR_BLACK = 0x0
COLOR_WHITE = 0xf

# y addr's start at 6 bc of memory layout
Y_START = 6
TOP_BAR_TEXT_START_X = 5
TOP_BAR_TEXT_Y = 5
TOP_BAR_LINE_Y = 20
EMOJI_START_X = 5
EMOJI_START_Y = 40
TEXT_START_X = 150
TEXT_START_Y = 50
GRAPH_START_X = 150
GRAPH_END_X = 290
GRAPH_START_Y = 35
GRAPH_END_Y = 115
class BlantsGui:
    def __init__(self, disp: Display):
        self.disp = disp

    def _emoji(self, em):
        if not isinstance(em, Emoji):
            raise Exception("bad emoji")

        with open(em.data, 'rb') as em_bytes:
            em_buf = framebuf.FrameBuffer(bytearray(em_bytes.read()), 128, 80, framebuf.MONO_HLSB)
            self.disp.blit(em_buf, EMOJI_START_X, EMOJI_START_Y)

    def _clear_right_side(self):
        # clear area
        self.disp.rect(
            GRAPH_START_X,
            GRAPH_START_Y,
            GRAPH_END_X - GRAPH_START_X,
            GRAPH_END_Y - GRAPH_START_Y + 15, # +15 to clear label
            COLOR_WHITE,
            True
        )

    def _graph(self, points, label=None, display_last=True, min=0, max=100):
        graph_width = GRAPH_END_X - GRAPH_START_X
        graph_height = GRAPH_END_Y - GRAPH_START_Y

        # clear area
        self._clear_right_side()

        # borders
        self.disp.rect(GRAPH_START_X, GRAPH_START_Y, graph_width, graph_height, COLOR_BLACK)

        # # draw axis
        # self.disp.vline(GRAPH_START_X, GRAPH_START_Y, graph_height, COLOR_BLACK)

        # draw points
        x_inc = graph_width // len(points)
        x = GRAPH_START_X
        for i in range(len(points) - 1):
            self.disp.line(
                x,
                #TODO: correct this by flipping graph_start and graph_end
                map_point(points[i], min, max, GRAPH_END_Y, GRAPH_START_Y),
                x + x_inc,
                map_point(points[i + 1], min, max, GRAPH_END_Y, GRAPH_START_Y),
                COLOR_BLACK
            )
            x += x_inc

        if display_last:
            self.disp.rect(GRAPH_END_X - 20, GRAPH_END_Y - 20, 20, 20, COLOR_BLACK, True)
            self.disp.text(str(points[-1]), GRAPH_END_X - 18, GRAPH_END_Y - 14, COLOR_WHITE)

        # label
        if label != None:
            # horizontal centering
            # assuming each letter is 8 pixels
            # num_letters * 8 / 2
            self.disp.text(
                label,
                GRAPH_START_X + (graph_width // 2) - (len(label) * 4),
                GRAPH_END_Y + 5,
                COLOR_BLACK
            )

    def _text(self, text):
        lines = text.splitlines()
        if len(lines) > 5:
            raise Exception("too many lines")

        # clear area
        self._clear_right_side()
        # display text
        y_padding = 0
        for l in lines:
            if len(l) > 24:
                raise Exception("line too long")

            self.disp.text(l, TEXT_START_X, TEXT_START_Y + y_padding, COLOR_BLACK)
            y_padding += 10


    # either text or data_points
    # if both are provided, only text will be displayed
    def render(
        self,
        topbar=None,
        emoji=None,
        text=None,
        data_points=None,
        graph_label=None,
    ):
        if emoji != None:
            self._emoji(emoji)

        if topbar != None:
            self.disp.hline(0, TOP_BAR_LINE_Y, self.disp.dims()[1] - 1, COLOR_BLACK)
            self.disp.text(topbar, TOP_BAR_TEXT_START_X, TOP_BAR_TEXT_Y, COLOR_BLACK)

        if text != None:
            self._text(text)
        elif data_points != None:
            self._graph(data_points, label=graph_label)

        self.disp.show()
