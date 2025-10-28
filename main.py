import os
import tweepy
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
#from picamera2 import PiCamera

import secrets 
import config

# Set Base GPI O settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.relay, GPIO.OUT)  #Set IO for Relay activation 'Move the Skeleton'
GPIO.setup(config.trickinput, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Set IO for button press 'Trick'
GPIO.setup(config.treatinput, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Set IO for button press 'Treat'

#Define the Camera
#cam = PiCamera() 

# Function to open lid of candy bucket
def open():
    servo = Servo(config.servo)
    servo.min()
    sleep(1)
    servo.max()

# Function to close lid of candy bucket
def close():
    servo = Servo(config.servo)
    servo.max()
    sleep(1)
    servo.min()

# Function to play sound file
def sound(f):
    os.system("mpg123 sounds/{} &".format(f))

# Function to start skeleton movement
def move_start():
    GPIO.output(config.relay, 1)

# Function to stop skeleton movement
def move_stop():
    GPIO.output(config.relay, 0)

# Function that starts camera hardware
# This has to be a seperate function because of delay
#def camera_start():
#    cam.start_preview()

# Function that will snap 4 pictures and store locally
#def camera_snap():
#    picnum = 0
#    for i in range (4):
#        cam.capture('images/img_%s.jpg' %picnum)
#        picnum += 1 #increment the picnum by 1
#        sleep (.5) #delay between pictures

# Function that will stop camera hardware    
#def camera_stop():    
#    cam.stop_preview()


# Function that posts to twitter API, post includes images and message based on input recieved
def tweet(stat):
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)
    # Upload image
    images = ('images/img_0.jpg', 'images/img_1.jpg', 'images/img_2.jpg', 'images/img_3.jpg')
    media = [api.media_upload(i).media_id_string for i in images]
    # Post tweet with image
    tweet = "HAPPY HALOWEEN! They chose {}! #trickortreatmachine".format(stat)
    post_result = api.update_status(status=tweet, media_ids=media)

while (1):
        #Trick input
        if (GPIO.input(config.trickinput) == 1):
                print ("Button Press Detected")
                print ("They choose Trick!!!")
#                camera_start()
                sound(config.tricksound1)
                move_start()
#                camera_snap()
                sleep(1)
                print ("shutting it down")
                move_stop()
                sound(config.tricksound2)
#                camera_stop()
#                tweet("TRICK")
                print("End of Trick")
        #Treat input
        elif (GPIO.input(config.treatinput) == 1):
                print ("Button Press Detected")
                print ("They choose Treat!!!")
                sound(config.treatsound1)
                sleep(1)
                open()
#                camera_start()
                sleep(5)

                sound(config.treatsound2)
                move_start()
#                camera_snap()
                print("shutting it down")
                move_stop()
                close()
                sound(config.treatsound3)
#                camera_stop()
#                tweet('TREAT')
                print ("End Treat")

