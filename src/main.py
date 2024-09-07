from server import BlantServer
from time import sleep
import blants as b

if __name__ == '__main__':
    # blants setup
    blant = b.Blants()
    # bs = BlantServer(blant)
    # sleep for 1min to allow debugging
    blant.board.ON_BOARD_LED_PIN.on()
    sleep(60)
    blant.board.ON_BOARD_LED_PIN.off()
    blant.run()
