""" This script is a race car starting line. It uses a servo to be the gate, Servo is connected to GP18.
LEDs connected to GP0-GP3. Button connected to GP4
This script is in micropython and can be used on any of the Raspberry pi picos and esp8266, 32
"""
from machine import Pin, PWM  #From library machine import Pin and PWM
from utime import sleep      #From library utime import sleep

# Define GPIO pins
button_pin = 6  # Button connected to GPIO 6
led1_pin = 0     # Connection for external LEDs
led2_pin = 1
led3_pin = 2
led4_pin = 3
servo = PWM(Pin(18))  #Servo connected to GP18
M = 7864            #180º position of the servo
H = int(M/2)       #90º position of the servo
freq = 50            #PWM Frequency: 50
servo.freq(freq)  #Servo freq: 50

# Set up the button as an input with an internal pull-up resistor
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Set up the LEDs as an output
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
led3 = Pin(led3_pin, Pin.OUT)
led4 = Pin(led4_pin, Pin.OUT)
servo.duty_u16(M)  #Set the servo position to 180º
try:  #Try the indented code but if it doesn't work drop down to exceptions
    while True: #Using "while" in this way allows the program to run in a loop, untill the loop is broken
        # Check if the button is pressed (active low due to pull-up resistor)
        if button.value() == 0:
           led1.on()          #Turn the LED on
           sleep(1)     #Wait 1.2 seconds
           led1.off()         #Turn the LED off
           led2.on()               #Turn the LED on
           sleep(1)     #Wait 1.2 seconds
           led2.off()         #Turn the LED off
           led3.on()               #Turn the LED on
           sleep(1)     #Wait 1.2 seconds
           led3.off()         #Turn the LED off
           led4.on()               #Turn the LED on
           servo.duty_u16(H)    #Set servo position to 90º
           sleep(3)            #Wait 3 seconds
           servo.duty_u16(M)    #Set the servo position back to 180º
           led4.off()         #Turn the LED off
        else:            #If the button value is not low execute the indented code
            pass   #Do nothing
        
        # Small delay to debounce
        sleep(0.01)
except KeyboardInterrupt:   #Exeption: Keyboard interrupt
    servo.deinit()      #Turn off PWM
    led1.off()         #Turn the LEDs off
    led2.off()
    led3.off
    print("There has been a keyboard interrupt") #Print a message into the shell