import RPi.GPIO as GPIO, time, os
from lcd1602 import LCD1602
DEBUG = 1
GPIO.setmode(GPIO.BCM)

lcd = LCD1602

def run():
    while True:
        GPIO.setup(13, GPIO.OUT)
#button=6
#led=13
        if GPIO.output(13, True):
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)
        else:
            GPIO.output(13, False)
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("OFF",lcd.LCD_LINE_2)
