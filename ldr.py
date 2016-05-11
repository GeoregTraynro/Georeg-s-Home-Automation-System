import RPi.GPIO as GPIO, time, os      
from lcd1602 import LCD1602 
DEBUG = 1
GPIO.setmode(GPIO.BCM)

lcd = LCD1602()

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.5)

        GPIO.setup(RCpin, GPIO.IN)

        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
def run():
    while True:                       
        GPIO.setup(20, GPIO.OUT)              
        print RCtime(21)     # Read RC timing using pin #19

        if RCtime(21) > 4000:
            GPIO.output(20, True)
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)
        else:
            GPIO.output(20, False)
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("OFF",lcd.LCD_LINE_2)

