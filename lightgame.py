from gpiozero import Button
from gpiozero import LED
from time import sleep
import random

score = 0
count_seconds = 0
difficulty = 0
time_on_min = [0.50,0.25,0.15,0.10,0.05]
time_on_max = [1,0.50,0.25,0.20,0.10]
time_off_min = [0.50,0.25,0.15,0.10,0.05]
time_off_max = [1,1,1,1,1]








button = Button(15)
green = LED(2)
yellow = LED(3)
red = LED(14)
blue = LED(17)
white = LED(18)

green.off()
red.off()
yellow.off()
white.off()
blue.off()

while True:
    print (difficulty)
    green.off()
    red.off()
    blue.off()
    white.off()
    while not button.is_pressed:
        yellow.on()
        sleep(
            random.uniform(
                time_on_min[difficulty],
                time_on_max[difficulty]
                )
            )
    
        if button.is_pressed:
            break
    
        yellow.off()
        sleep(
            random.uniform(
                time_off_min[difficulty],
                time_off_max[difficulty]
                )
            )

    if yellow.is_lit:
        green.on()
        score = score + 1
        
    else:
        red.on()
        score = 0
        blue.off()
        white.off ()
        
    if score == 2:
        blue.on()
    if score == 5:
        white.on()
        
    count_seconds = 0
    start_menu = 5
    twobytwo = 2
    while button.is_pressed:
        if count_seconds == start_menu:
            green.off()
            yellow.off()
            red.off()
            blue.off()
            white.off()
        if count_seconds == start_menu + twobytwo:
            green.on()
            difficulty = 0
        if count_seconds == start_menu + (twobytwo*2):
            difficulty = 1
            yellow.on()
        if count_seconds == start_menu + (twobytwo*3):
            red.on()
            difficulty = 2
        if count_seconds == start_menu + (twobytwo*4):
            blue.on()
            difficulty = 3
        if count_seconds == start_menu + (twobytwo*5):
            white.on()
            difficulty = 4
        
        sleep(0.5)
        count_seconds = count_seconds + 0.5
        pass