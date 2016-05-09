import RPi.GPIO as GPIO, time, os      

DEBUG = 1
GPIO.setmode(GPIO.BCM)

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
        GPIO.setup(12, GPIO.OUT)              
        print RCtime(19)     # Read RC timing using pin #19

        if RCtime(19) > 28000:
            GPIO.output(12, True)
        else:
            GPIO.output(12, False)

#run()
