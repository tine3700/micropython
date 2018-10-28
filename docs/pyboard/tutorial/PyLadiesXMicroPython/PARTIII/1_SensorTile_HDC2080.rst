.. _Top:

MicroPython SensorTile
----------------------

The MicroPython SensorTile has a Temperature and Humidity Sensor (HDC2080)
a Light Sensor (OPT3001), an Amplifier (PAM8304) a Buzzer (Audio Magnetic) to make sound and a RGB LED for having some blinking.

MicroPython X-Skin Adapter Board
--------------------------------

For connecting the sensor to the MicroPython pyboard plug in the X-Skin Adapter Board on the X-Position. On top you have 2 x 20-pin bus headers for connecting different types of sensor adapter boards. To make sure to have them in the correct orientation place the hole in the SensorTile over the nut on the X-Skin Adapter Board.

Running the first test programm
-------------------------------

To see, if the different Sensors on the Tile are working. Please use the driver in this repository named `tile_one.py <tile_one.py>`_. You need to download this file to your pyboard (or just copy-paste code from github). Besides the driver you'll find a little demo program to run. After copying driver to your board type into your REPL:

.. code-block:: python

	import tile_one
	s=tile_one.TILE_ONE()
	s.demo()

The first entry is the time since the pyboard was started in ms. Second entry is the LED value. Temperature in °C, Humidity in % and Light Intensity measured in lux. There is also a little buzzer sound everytime you run the demo program.


Accessing the features of the SensorTile
----------------------------------------

The SensorTile has an RGB (Red, Green, Blue) LED. To play with this LED you can type:

.. code-block:: python

	import tile_one
	s=tile_one.TILE_ONE()
	s.led(color=1) #for red
	s.led(color=2) #for green
	s.led(color=3) #for blue
	s.led(color=7) #for white
	s.led(color=0) #turns off the LED

After making some light, we want to add some different kinds of sound. To use the Buzzer on the SensorTile type:

.. code-block:: python

	# freq = frequency dur = duration
	s.beep(freq=100, dur=200)
	
Accessing the sensor data:

.. code-block:: python

	# temperature and humidity
	s.hdc()
	# light intensity
	s.opt()

+------------+------------+-----------+
|   Back_    |   Top_     |  Next_    |
+------------+------------+-----------+

.. _Back: ../PARTII/2_LCD160CRv11.rst
.. _Next: 2_Temperature.rst
