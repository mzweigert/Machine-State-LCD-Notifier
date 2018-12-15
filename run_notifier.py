import RPi.GPIO as GPIO
import machine_state_info
import time

GPIO_PIN = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

BACKLIGHT_ON = False
IDDLE_TIME = 0
machine_state_info.lcd.backlight_off()

while True:
       time.sleep(0.5)
       MOVE_DETECTED = GPIO.input(GPIO_PIN) == 1
      
       if MOVE_DETECTED: 
	     if not BACKLIGHT_ON:
		   machine_state_info.refresh()
		   machine_state_info.lcd.backlight_on()             
                   BACKLIGHT_ON = True

	     IDDLE_TIME = 0
       elif IDDLE_TIME == 10:
	     BACKLIGHT_ON = False     
	     machine_state_info.lcd.backlight_off()
       elif not MOVE_DETECTED and BACKLIGHT_ON:
	     IDDLE_TIME += 0.5
