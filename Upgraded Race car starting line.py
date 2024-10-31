# This script causes an external LED to glow when a button is pressed.

from machine import Pin #By loading only the class called "Pin", we don't have to use machine.Pin in our code, we just use Pin
import utime

# Define GPIO pins
button_pin = 16  # Button connected to GPIO 16
led1_pin = 15     # Connection for external LED
led2_pin = 14
led3_pin = 13
led4_pin = 12

# Set up the button as an input with an external pull-up resistor
button = Pin(button_pin, Pin.IN, None)

# Set up the LED as an output
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
led3 = Pin(led3_pin, Pin.OUT)
led4 = Pin(led4_pin, Pin.OUT)

while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
    # Check if the button is pressed (active high due to pull-down resistor)
    if button.value() == 1:
       led1.on()          #Turn the LED on
       utime.sleep(1.2)     #Wait 1.2 seconds
       led1.off()         #Turn the LED off
       utime.sleep(0.01)  #Wait 0.01 seconds
       led2.on()          #Turn the LED on
       utime.sleep(1.2)     #Wait 1.2 seconds
       led2.off()         #Turn the LED off
       utime.sleep(0.01)  #Wait 0.01 seconds
       led3.on()          #Turn the LED on
       utime.sleep(1.2)     #Wait 1.2 seconds
       led3.off()         #Turn the LED off
       utime.sleep(0.01)  #Wait 0.01 seconds
       led4.on()          #Turn the LED on
       utime.sleep(2)     #Wait 2 seconds 
       led4.off()         #Turn the LED off
       utime.sleep(3)     #Wait 3 seconds
    else:
        led1.off()  # Turn off the LED when button is released
        led2.off()
        led3.off()
        led4.off()
    
    # Small delay to debounce
    utime.sleep(0.01)