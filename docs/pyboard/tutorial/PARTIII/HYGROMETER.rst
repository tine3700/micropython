Building your own Temperature and Humidity Control Device
---------------------

After exploring the temperature and humidity sensor and runing your first test script in the REPL, we want to combine our
different hardware components. Now we want to build our own Temperature and Humidity meassurement device. Of course, you can buy such devices for a few Euros, but where is the fun in that?

Hardware needed for this task:
----------------

* pyboard lite with accelerometer
* Jumper Wires and male Pins
* Temperature Sensor HDC1080 on break out board
* LCD160CRv1.0 Display with header
* Micro USB cable for connecting to the PC

Wire up your Sensor to one of the I2C Ports (do you remember on which Pins they are? If not, you can always have a look at the
Data sheet of the pyboard)
Take a look into the HDC1080 test program. The easiest way to show the meassured temperature and humidity on your
Display is directing the REPL to the Display. If you don't remember how that works. Please go back to Link:

**TASK 1**

Have a look at the datasheet of the pyboard lite with accelerometer. Can you adjust the test code in the hdc1080test.py and use the Temperature sensor with the other I2C? On which Pins is it?

**TASK 2**

Show the Temperature and Humidity on your Display with directing the REPL directly to it.

This looks not very nice. Now we want to show both Temperature and Humidity values on a nice setup.

**TASK 3**

Draw two squares and put the Temperature and Humidity values into these squares. Label both squares with the right values. Temperature in °C and Humidity in %. Feel free to do this in any way you like.

**TASK 4**

Try to make two boxes for the temperature and the humidity values and show them on the Display. Or can you think of a more beautiful way?

**TASK 5**



