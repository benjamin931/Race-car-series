# This script causes an external LED to glow when a button is pressed.

from machine import Pin #By loading only the class called "Pin", we don't have to use machine.Pin in our code, we just use Pin
from utime import sleep

# Define GPIO pins
button_pin = 6  # Button connected to GPIO 6
led1_pin = 0     # Connection for external LEDs
led2_pin = 1
led3_pin = 2
led4_pin = 3

# Set up the button as an input with an internal pull-up resistor
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)

# Set up the LED as an output
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
led3 = Pin(led3_pin, Pin.OUT)
led4 = Pin(led4_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
    # Check if the button is pressed (active high due to pull-down resistor)
    if button.value() == 1:
       led1.on()          #Turn the LED on
       sleep(1.2)     #Wait 1.2 seconds
       led1.off()         #Turn the LED off
       led2.on()          #Turn the LED on
       sleep(1.2)     #Wait 1.2 seconds
       led2.off()         #Turn the LED off
       led3.on()          #Turn the LED on
       sleep(1.2)     #Wait 1.2 seconds
       led3.off()         #Turn the LED off
       led4.on()          #Turn the LED on
       sleep(2)     #Wait 2 seconds 
       led4.off()         #Turn the LED off
    else:     #If button value is not = 1:
        pass              #Do nothing
    
    # Small delay to debounce
    utime.sleep(0.01)
