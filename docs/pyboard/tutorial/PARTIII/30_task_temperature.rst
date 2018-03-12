After exploring the temperature and humidity sensor and runing your first test test script in the REPL, we want to combine our
different hardware compnents.

Hardware
----------------

* Hardware needed for this task
* pyboard lite with acc
* Jumper Wire with male Pins
* Temperature Sensor HDC1080
* LCD160CRv1.0 with header

Wire up your Sensor to one of the I2C Ports (do you remember on which Pins they are, if not, you can always have a look at the
Data sheet of the pyboard)
Take a look into the HDC1008 test program. The easiest way to show the meassured temperature and humidity on your
Display is directing the REPL to the Display. If you don't remember how that works. Please go back to::

This looks not very nice. Now we want to show both Temperature and Humidity values on a nice setup.

Try to make two boxes for the temperature and the humidity values and show them on the Display.


