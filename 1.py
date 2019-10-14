import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

#Sets the GPIO to the BCM state
GPIO.setmode(GPIO.BCM) 
DEBOUCE_TIME = 500 #Sets the defualt debouce time for the buttons
camera = PiCamera()


def recordButtonPressed(time)
#TAB THESE
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(2)
camera.stop_recording()
camera.stop_preview()


# GPIO 23 set up as input
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    recordButtonPressed()
    print "whatever was waiting for a button press."  
    
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
