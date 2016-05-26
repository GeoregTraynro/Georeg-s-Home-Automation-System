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
    	#GPIO pin 12 is the output (TEMP'S led).
    	print ("DEBUG: setting up the gpio pins")
        GPIO.setup(12, GPIO.OUT)              
        print RCtime(19)     # Read RC timing using pin #19

        if RCtime(19) < 50000:
        	print ("DEBUG: Values of fan are being printed")
        	#If tempreture sensors value is above 50000, turns led on
            GPIO.output(12, True)
            print ("DEBUG: LED is on, values are above 50000")
            #prints on lcd screen "fan on"
            lcd.lcd_string("FAN:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)
        else:
        	#otherwise (if value is below 50000), turns led off
            GPIO.output(12, False)
            #prints on lcd display "Fan Off"
            print ("DEBUG: LED is on, values are below 50000")
            lcd.lcd_string("FAN:",lcd.LCD_LINE_1)
            lcd.lcd_string("OFF",lcd.LCD_LINE_2)
#run()
