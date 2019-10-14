import RPi.GPIO as GPIO


#Sets the GPIO to the BCM state
GPIO.setmode(GPIO.BCM) 

DEBOUCE_TIME = 500 #Sets the defualt debouce time for the buttons


def recordButtonPressed

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    print "\nFalling edge detected. Now your program can continue with"  
    print "whatever was waiting for a button press."  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
