#Import the required module.
import RPi.GPIO as GPIO #GPOI
from lcd1602 import LCD1602 #LDC DISPLAY
from time import sleep #SLEEP?
import time #TIME
import ldr
import hdr
import led

print ("DEBUG: setting up the gpio pins")
#Set the mode of numbering the pins.
GPIO.setmode(GPIO.BCM)
#GPIO pin 20 is the output (LDR'S LED).
GPIO.setup(20, GPIO.OUT)
#GPIO pin 2 is the input (LDR'S BUTTON).
GPIO.setup(2, GPIO.IN)
#Initialise GPIO20 to LOW (true) so that the LED is off.
GPIO.output(20, False)
#GPIO pin 26 is the input (TEMP'S Button).
GPIO.setup(26, GPIO.IN)
#GPIO pin 13 is the output (SINGLE BUTTON LED).
GPIO.setup(13, GPIO.OUT)
#GPIO pin 6 is the input for (SINGLE BUTTON LED).
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Initialise GPIO13 to high (true) so that the LED is off.
GPIO.output(13, False)
#(TEMP'S LED)
GPIO.setup(12, GPIO.OUT)

#Definition
lcd = LCD1602() #LCD DISPLAY
isPressed = False #BUTTON'S
isOn = False #BOUTTON'S

#define light level (ALSO USED IN THE TEMPRETURE)
def light_level(pin):
        level = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.setup(pin, GPIO.IN)
        while (GPIO.input(pin) == GPIO.LOW):
                level += 1
        return level
#While Loop
while 1:            #PRINTING THE Home Screen
    print ("DEBUG: Home screen")
    lcd.lcd_string("Home",lcd.LCD_LINE_1)
    lcd.lcd_string("Automation",lcd.LCD_LINE_2)
    
    #LDR
    if GPIO.input(2):
    	print ("DEBUG:Light dependent ristor's button pressed")
        if not isPressed: #IF BUTTON PRESSED
               print ("DEBUG: running LDR's code")
               lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
               lcd.lcd_string("ON",lcd.LCD_LINE_2)#PRINT LED 1: ON
               ldr.run()
    #SINGLE LED BUTTON
    if GPIO.input(6):
    	print ("DEBUG: Single led button pressed")
        lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
        lcd.lcd_string("ON",lcd.LCD_LINE_2)
        print ("DEBUG: waiting for 3 seconds")
        print ("DEBUG: led is off")
        time.sleep(3)
        if not isPressed:
        	print ("DEBUG: LED button pressed")
            isPressed = True
            isOn = not isOn
            GPIO.output( 13, isOn)
            print ("DEBUG: led is on")
            lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
            lcd.lcd_string("OFF",lcd.LCD_LINE_2)

    #THERMISTOR/fan
    if GPIO.input(26):
    	print ("DEBUG: Fan button pressed")
        if not isPressed: #WHEN FAN BUTTON PRESSED
               print ("DEBUG: running Fan code") 
               lcd.lcd_string("FAN:",lcd.LCD_LINE_1)
               lcd.lcd_string("ON",lcd.LCD_LINE_2) #PRINT LED 3: ON (WILL CHANGE OUT LED TO THE FAN
               hdr.run()

    else:
    	print ("DEBUG: returning to home screen")
        isPressed = False #RETURNS TO HOME SECREN