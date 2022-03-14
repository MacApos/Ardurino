import pyfirmata

board = pyfirmata.Arduino('COM3')  # Change to your port
print("Start")
while True:
    board.digital[3].write(0)
