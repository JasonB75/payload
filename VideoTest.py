from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(2)
camera.stop_recording()
camera.stop_preview()
