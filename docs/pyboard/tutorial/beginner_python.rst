Hello, pyboard!
--------
MicroPython is a reimplementation of the Python 3.x programing language. Most of your Python programming knowledge is directly useable in MicroPython. Please see the differences here: <http://docs.micropython.org/en/latest/pyboard/genrst/index.html>`_,

For making you familiar with the REPL and the Python programming language in general please try some of the following tasks:

After logging into the python promt on your machine, you can directly interact with your pyboard. Get into it and run the first lines of your code::

  >>> print("Hello, MicroPython pyboard!")

The code above will return::

  >>> Hello, MicroPython pyboard!

Variables and Types
------
Python supports three types of numbers: integers, floating point numbers and complex numbers – so does MicroPython. You can try it yourself with typing into the REPL::

  >>> oneint = 4
  >>> print(oneint)
  4

To define a floating point number::

  >>> onefloat = 4.0
  >>> print(onefloat)
  >>> onefloat=float(4)
  >>> print(onefloat)

Will return::

  >>> 4.0
  >>> 4.0
  
Strings
--------
Strings are defined either with a single quote or a double quotes.::

    mystring = 'hello'
    print(mystring)
    mystring = "hello"
    print(mystring)
  
Simple operators can be executed on numbers and strings
--------
::
    one = 1
    two = 2
    three = one + two
    print(three)
    hello = "hello"
    world = "world"
    helloworld = hello + " " + world
    print(helloworld)

Excercise
---------
::
  # change this code
  mystring = None
  myfloat = None
  myint = None

  # testing code
  if mystring == "hello":
    print("String: %s" % mystring)
  if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
  if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


