import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

#Sets the GPIO to the BCM state/pin layout
GPIO.setmode(GPIO.BCM) 
#DEBOUCE_TIME = 500 #Sets the defualt debouce time for the buttons

#Inicializes the camera object
camera = PiCamera()

# GPIO 23 set up as input
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  


#Function called when the button is pressed
def recordButtonPressed(time)
    # Activates the camera and allows it to focus
    camera.start_preview()
    sleep(2)
    
    #Takes Picuture then begins recording video
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(2) #Waits while recording video
    
    #Stops recording and turns off camera
    camera.stop_recording()
    camera.stop_preview()
    
    #Runs shell command to convert video to mp4
    command = "MP4Box -add beepvid.h264 beepvid.mp4"
    call([command], shell=True)
    print("vid conv")
    
    
try:  
    #Waits till the putton is pressed, connecting pin 23 to ground.
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    recordButtonPressed()
    print "whatever was waiting for a button press."  
    
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
