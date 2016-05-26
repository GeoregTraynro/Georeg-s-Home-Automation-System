#Import the required module.
import RPi.GPIO as GPIO, time, os      
from lcd1602 import LCD1602
DEBUG = 1
#Set the mode of numbering the pins.
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
#Run code used in master code
def run():
    while True:
    	#GPIO pin 21 is the output (TEMP'S led).
    	print ("DEBUG: setting up the gpio pins")
        GPIO.setup(21, GPIO.OUT)              
        print RCtime(14)     # Read RC timing using pin #14

        if RCtime(14) > 5000:
        	print ("DEBUG: values for ldr are beeing printed")
        	#If tempreture sensors value is below 5000, turns led on
            GPIO.output(21, True)
            print ("DEBUG: LED is on, values are above 50000")
            #prints on lcd screen "led on"
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)
        else:
        	#otherwise (if value is below 50000), turns led off
            GPIO.output(21, False)
            print ("DEBUG: LED is off, values are below 50000")
            #prints on lcd display "Fan Off"
            lcd.lcd_string("LED:",lcd.LCD_LINE_1)
            lcd.lcd_string("OFF",lcd.LCD_LINE_2)
#run()
