from board import Board, NODEMCU_ESP32
from display import Epd2in9Display
from gui import BlantsGui, Emoji
from time import sleep

sample_points = [24, 22, 12, 81, 75, 60, 40, 9, 72, 50, 33, 28, 10, 5, 99, 90, 89, 88, 39, 38, 37, 36, 35, 34]
sample_points_2 = [40, 9, 72, 50, 33, 28, 10, 5, 99, 90, 89, 88, 39, 38, 37, 36, 35, 34, 24, 22, 12, 81, 75, 60]

if __name__ == '__main__':
    board = Board(NODEMCU_ESP32)
    epd_disp = Epd2in9Display(board)
    gui = BlantsGui(epd_disp)

    print("ready about to render \"hello world\"")
    print("about to render")
    # gui.render(
    #     topbar="moisture: 26.3%",
    #     emoji=Emoji.Confused(),
    # )
    # sleep(5)
    # gui.render(
    #     emoji=Emoji.Good(),
    #     data_points=sample_points,
    # )
    gui.render(
        emoji=Emoji.Sleepy(),
        topbar="sleepin since 8:12pm 8/31/2024",
        data_points=sample_points_2,
        graph_label="Last 24 hours",
    )
    sleep(5)
    gui.render(
        emoji=Emoji.Good(),
        text="doin' juuust fine"
    )
