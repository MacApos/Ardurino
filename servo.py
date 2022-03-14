from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('COM3')  # Change to your port
pin3 = 3
pin5 = 5
pin9 = 9

for pin in pin3, pin5, pin9:
    board.digital[pin].mode = SERVO

while True:
    for i in range(0, 180, 20):
        board.digital[pin].write(i)
        sleep(0.5)
    for i in range(180, 0, -20):
        board.digital[pin].write(i)
        sleep(0.5)