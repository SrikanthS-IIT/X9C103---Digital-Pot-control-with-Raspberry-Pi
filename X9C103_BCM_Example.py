# X9C103_Example.py
# Author - Srikanth Sugavanam, IIT Mandi, India - 26th January 2022

# This program shows how to use the X9C103 library for controlling this digital potentiometer using Raspberry Pi.
# Note - the BCM numbering convention is followed.

import X9C103_BCM as pot


#Setting pins - note the BCM board numbering convention has been used.
CS = 16
INC = 20
UD = 21
#GND = pin34
delay = 0.1

#Setup the GPIO inputs/outputs on the Raspberry Pi
pot.initiate(CS,INC,UD)

#Activate the pot for receiving wiper move instructions
pot.activate(CS,INC,UD)

#Set the wiper to move up
flag = 1 #moving wiper up = 1, moving wiper down = 0
steps = 1
pot.wiperset(CS,INC,UD,flag)
pot.wipermove(CS,INC,UD,steps)

flag = 0
steps = 1
 
pot.wiperset(CS,INC,UD,flag)
pot.wipermove(CS,INC,UD,steps)

#Reset the wiper if required - the wiper will ramp sweep through all values. 
#This function can also be used to trigger an oscilloscope measurement.
#pot.reset(CS,INC,UD)

#Disconnect pot
pot.disconnect(CS,INC,UD)

