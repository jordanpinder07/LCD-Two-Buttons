# Write your code here :-)
# code-lcd-i2c
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Simple test for 16x2 character lcd with an I2C LCD backpack."""
import board
import digitalio
import time
import time
import board
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Write your code here :-)
# code-lcd-i2c
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Simple test for 16x2 character lcd with an I2C LCD backpack."""
import board
import digitalio
import time
import time
import board
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

score_button = digitalio.DigitalInOut(board.GP10)
score_button.direction = digitalio.Direction.INPUT
score_button.pull = digitalio.Pull.UP

score_button.value

print(score_button.value)


ball_count_button = digitalio.DigitalInOut(board.GP6)
ball_count_button.direction = digitalio.Direction.INPUT
ball_count_button.pull = digitalio.Pull.UP

ball_count_button.value

print(ball_count_button.value)

# Initialize the score variable
score = 0
ball_count = 10

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
i2c = busio.I2C(board.GP1, board.GP0)

# Talk to the LCD at I2C address 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)
lcd.set_backlight(True)

while True:
    print ("Button value:")
    print(score_button.value)
    if score_button.value == False:
        score = score + 50
        print("Button is pressed")
        time.sleep(0.2)
    else:
        print("Button not pressed")
        time.sleep(0.5)

    print ("Ball_count_button value:")
    print(ball_count_button.value)
    if ball_count_button.value == False:
        ball_count = ball_count - 1
        ball_count = ball_count - 1
        print("Ball_count_button is pressed")
        time.sleep(0.2)
    else:
        print("Ball_count_button not pressed")
        time.sleep(0.5)

        print("refreshing LCD")
    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("ball count:")
    lcd.print(str(ball_count))
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Score: ")
    lcd.print(str(score))


