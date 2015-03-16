import ArduinoCarPi
ard = ArduinoCarPi.Arduino("/dev/tty.usbmodem14641")
ard.registerLEDs(9,10,11)
