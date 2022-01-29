# X9C103---Digital-Pot-control-with-Raspberry-Pi
TLDR - Control the X9C103 using a Raspberry Pi. Uses the RPi.GPIO library. Includes initialize, activate, step, and sweep modes. Uses BCM numbering. 
- Srikanth Sugavanam, IIT Mandi, 29th January 2022

The X9C103_BCM.py is a module that will allow you to control the X9C103 digital potentiometer (https://www.renesas.com/us/en/document/dst/x9c102-x9c103-x9c104-x9c503-datasheet). In principle, it should also work for the C102, C104, and the C503 as the code is based on the same datasheet. The code is however tested only for the X9C103, and hence I have named the repository and files as such. 

It basically is a collection of some simple functions, that obfuscates the timing diagram considerations. Simply define the CS, UD and INC pin selections, the direction you want to move the pot wiper, and the number of increments, and it will take care of the timing considerations and move the wiper. The code does not make any assumptions about the resistance values, nor does it measure it actively in any form, so you will need to do some breadboard testing on the side to ensure it is working to spec for you. When the chip is disconnected, it will store the last value of resistance. 

I have included an additional sweep function that will sweep through all values of the resistance (ramp up 99 steps, ramp down 99 steps). I found it useful to run this sweep once towards the beginning of the code, in case you aren't sure what is the last stored resistance value on the pot, and want a clean slate. 

Alternatively, - and the purpose for which the sweep function was actually written - you can use the sweep as a trigger and automatically sweep through all the resistance values. Particularly useful if you want to do a characterization experiment. 

X9C103 uses the RPi.GPIO and time libraries. So you wouldn't have to include these libraries in your code if you are already calling the X9C103_BCM.py module.

To use this module, simply put the X9C103_BCM.py file in your current working folder. The X9C103_BCM_Example.py shows how to use the different functions. 

Remember - as in any software based control of hardware exercise, ensure that your electrical/electronic connections and specifications are correct. Also remember that the RPi GPIOs accept only up to 3.3 V. I tested the X9C103 by powering it with the 3.3 V pin on the RPi itself. It worked, so it should for you too.

If you run into any issues, I will try to resolve them as best as I can, but you will see the codes are quite simple, and are based off the timing diagram on the X9C103 datasheet. If you run into a bug - it is most likely one of these issues - 

--- You specified board pins instead of BCM pin numbers.

--- The chip is not being powered properly via the 3.3 V pin. 

--- You are using the chip in a potential divider config when you want to use it as a variable resistor (and vice versa). ['Somebody I know' did this]

--- The wiper is either at the top most position when you want to sweep it further up, or vice versa. Reset the wiper.

--- You run into strange resistance values. I would put my money on timing. Change the underlying library code as per the datasheet as required. 

--- ***The wiper movement is not linear. I have seen this happen a couple of times - the quick fix is to run the Reset sweep a couple of times and it gets better.

Happy sweeping! - Srikanth. 
