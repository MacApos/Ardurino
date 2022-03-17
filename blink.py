from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('COM3')  # Change to your port
pin = 3

while True:
    board.digital[pin].write(1)
    sleep(10)  # delays for 9 seconds
    board.digital[pin].write(0)
    sleep(1)  # delays for 9 seconds

