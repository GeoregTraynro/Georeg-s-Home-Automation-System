# Import the required module.
import RPi.GPIO as GPIO #GPOI
from lcd1602 import LCD1602 #LDC DISPLAY
from time import sleep #SLEEP?
import time #TIME

# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BCM)
# GPIO pin 20 is the output (LDR'S LED).
GPIO.setup(20, GPIO.OUT)
#GPIO pin 5 is the input (LDR'S BUTTON).
GPIO.setup(5, GPIO.IN)
# Initialise GPIO20 to LOW (true) so that the LED is off.
GPIO.output(20, False)
#GPIO pin 26 is the input (TEMP'S Button).
GPIO.setup(26, GPIO.IN)
# GPIO pin 13 is the output (SINGLE BUTTON LED).
GPIO.setup(13, GPIO.OUT)
#GPIO pin 6 is the input for (SINGLE BUTTON LED).
GPIO.setup(6, GPIO.IN)
# Initialise GPIO10 to high (true) so that the LED is off.
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
    lcd.lcd_string("Home",lcd.LCD_LINE_1)
    lcd.lcd_string("Automation",lcd.LCD_LINE_2)

    #LDR
    if GPIO.input(5):
        if not isPressed: #IF BUTTON PRESSED
               lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
               lcd.lcd_string("ON",lcd.LCD_LINE_2)#PRINT LED 1: ON
               print light_level(21)
               time.sleep(3) #WEIGHT 3 SECONDS
               if light_level(21) > 9000: #ANY BRIGHTER THAT 9000 LED WONT TURN ON
                   GPIO.output(20 , True)
                   lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
                   lcd.lcd_string("OFF",lcd.LCD_LINE_2) #PRINT LED 1: OFF
                   isPressed = True
                   isOn = not isOn
                   GPIO.output( 20, isOn)
                   time.sleep(3) #SLEEP 3 SECONDS
    #SINGLE LED BUTTON
    if GPIO.input(6):
        if not isPressed:#WHEN BUTTON PRESSED
            lcd.lcd_string("LED 2:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)#PRINT LED 2: ON
            isPressed = True
            isOn = not isOn
            GPIO.output( 13, isOn)
            time.sleep(3) #SLEEP 3 SECONDS

    #THERMISTOR/fan
    if GPIO.input(26):
        if not isPressed: #WHEN FAN BUTTON PRESSED
               lcd.lcd_string("LED 3:",lcd.LCD_LINE_1)
               lcd.lcd_string("ON",lcd.LCD_LINE_2) #PRINT LED 3: ON (WILL CHANGE OUT LED TO THE FAN
               print light_level(19)
               time.sleep(3) #WEIGTH 3 SECONDS
               if light_level(19) > 9000: #IF HEATING IS ANY LESS THAN 9000 FAN WONT TURN ON
                   GPIO.output(12 , True)
                   lcd.lcd_string("LED 3:",lcd.LCD_LINE_1)
                   lcd.lcd_string("OFF",lcd.LCD_LINE_2) #PRINT LED 3: OFF (WILL CHANGE OUT LED TO THE FAN
                   isPressed = True
                   isOn = not isOn
                   GPIO.output( 12, isOn)
                   time.sleep(3) #WEIGHT 3 SECONDS


    else:
        isPressed = False #RETURNS TO HOME SECREN
