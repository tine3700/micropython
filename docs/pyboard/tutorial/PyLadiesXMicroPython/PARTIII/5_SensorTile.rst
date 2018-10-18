Building your own Temperature and Humidity Control Device
---------------------

The MicroPython SensorTile has a Temperature and Humidity Sensor (HDC2080) a Light Sensor (OPT3001), an Amplifier (PAM8304) a Buzzer (Audio Magnetic) to make sound and a RGB LED for having some blinking.
For our next little task, we would like to combine the LCD160CR and the Sensor adapter board.
After exploring the temperature and humidity sensor and runing your first test script in the REPL, we want to combine our
different hardware components. Now we want to build our own Temperature and Humidity meassurement device. Of course, you can buy such devices for a few Euros, but where is the fun in that?

Hardware needed for this task:
----------------

* pyboard lite with accelerometer and headers
* SensorTile Temperature Sensor HDC2080 on break out board
* Protoskin-Adapter Board
* LCD160CRv1.1 Display with header
* Micro USB cable for connecting to the PC
* SD-Card for the data-logger in advanced task

Plug in the Protoskin-Adapter Board on top of the pyboard. Make sure to plug it into the 'X' position for this first task. PIC
Take a look into the HDC2080 test program. The easiest way to show the meassured temperature and humidity on your
Display is directing the REPL to the Display. If you don't remember how that works. Please go back to Link:

.. image:: /docs/pyboard/tutorial/img/1_SensorTile_Adapter.jpg

**TASK 1: Using the I2C connecton at the Y-skin of the pyboard**

Have a look at the datasheet of the pyboard lite with accelerometer. There you can see that you have an 'X' and 'Y' position how to connect the different components. Can you adjust the test code in the hdc2080_test.py and use the Temperature sensor with the 'Y' position? On which Pins is it?

**Note:** The Sensor Adapter board provides you the wiring between the I2C Pins and the sensor itself. You don't have to manually wire any connections up.

**TASK 2: Temperature and Humidity on your computer screen with the REPL**

Show the Temperature and Humidity on your Display with directing the REPL directly to it.
This looks not very nice. Now we want to show both Temperature and Humidity values on a nice setup.

**TASK 3: Temperature and Humidity on the LCD160CR**

Show the Temperature and Humidity values on the Display. Try to show them in different colours. Add the right Temperature in °C and Humidity in %. Feel free to do this in any way you like.

.. image:: /docs/pyboard/tutorial/img/image.png

**TASK 4: Data-logger for the Temperature**

Think about how you would like to log your data in an infinite loop. There are two ways of doing this. There is the internal flash of the pyboard and if you put a SD-Card in your pyboard, the data will be logged to that file.

.. code-block:: python

	rtc = pyb.RTC()

    def writeLog(rtc, temp, hum):
    """Append a line with the current timestamp to the log file"""
    datetime=rtc.datetime()
    timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % (datetime[0],
	datetime[1], datetime[2], datetime[4], datetime[5], datetime[6]))
    logline = ("%s %s %s" % (timestamp, temp, hum))

    print(logline)
    try:
        with open("/sd/logdata.txt", "a") as f:
            f.write("%s\n" % logline)
            f.close()
            pyb.sync()
    except:
	pass
    try:
	with open("/flash/logdata.txt", "a") as f:
	    f.write("%s\n" % logline)
            f.close()
            pyb.sync()

    except OSError as error:
        print("Error: can not write to SD card. %s" % error)

	def log():
	for i in range(20):
	    writeLog(rtc,hdc_temp(),hdc_hum())
