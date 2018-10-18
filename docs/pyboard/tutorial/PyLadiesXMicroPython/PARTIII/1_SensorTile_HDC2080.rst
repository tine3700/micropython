MicroPython SensorTile
---------------------

The MicroPython SensorTile has a Temperature and Humidity Sensor (HDC2080)
a Light Sensor (OPT3001), an Amplifier (PAM8304) a Buzzer (Audio Magnetic) to make sound and a RGB LED for having some blinking.

MicroPython X-Skin Adapter Board
----------------------

For connecting the sensor to the MicroPython pyboard plug in the X-Skin Adapter Board on the X-Position. On top you have 2 x 20-pin bus headers for connecting different types of sensor adapter boards. To make sure to have them in the correct orientation place the hole in the SensorTile over the nut on the X-Skin Adapter Board.

Running the first test programm
--------------------

To see, if the different Sensors on the Tile are working. Please use the driver in this repository named tile_one.py. Besides the driver you'll find a little program to run. Type into your REPL:

.. code-block:: python

	import tile_one
	s=tile_one.TILE_ONE()
	s.demo()
