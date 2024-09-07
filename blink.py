import machine
from time import sleep

ON_BOARD_LED_PIN = machine.Pin(2, machine.Pin.OUT)

print("wake reason:", machine.wake_reason())
while True:
    ON_BOARD_LED_PIN.on()
    sleep(2)
    ON_BOARD_LED_PIN.off()
    sleep(2)
