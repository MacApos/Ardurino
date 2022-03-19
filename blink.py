from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('COM5')  # Change to your port
pin = 9

while True:
    board.digital[pin].write(1)
    sleep(10)
    print('high')
    board.digital[pin].write(0)
    sleep(1)
    print('low')

