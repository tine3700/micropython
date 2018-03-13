Building your own Temperature and Humidity Sensor
---------------------
-------------------------

After exploring the temperature and humidity sensor and runing your first test test script in the REPL, we want to combine our
different hardware compnents.

Hardware needed for this task:
----------------

* pyboard lite with accelerometer
* Jumper Wires with male Pins
* Temperature Sensor HDC1080 on break out board
* LCD160CRv1.0 with header
* Micro USB cable for connecting to the PC

Wire up your Sensor to one of the I2C Ports (do you remember on which Pins they are, if not, you can always have a look at the
Data sheet of the pyboard)
Take a look into the HDC1080 test program. The easiest way to show the meassured temperature and humidity on your
Display is directing the REPL to the Display. If you don't remember how that works. Please go back to::

**TASK 1**
Show the Temperature and Humidity on your Display with directing the REPL directly to it.

This looks not very nice. Now we want to show both Temperature and Humidity values on a nice setup.

**TASK 2**
Draw two squares and put the Temperature and Humidity values into these squares. Label both squares with the right values. Temperature in °C and Humidity in %.


**TASK 3**


Try to make two boxes for the temperature and the humidity values and show them on the Display.


