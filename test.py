from time import sleep
import ArduinoCarPi
ard = ArduinoCarPi.Arduino("/dev/ttyAMA0")
ard.registerLEDs(9,10,11)
#while True:
#	ard.lightRGB(255,10,10)
#	sleep(0.05)
#	ard.lightRGB(255,255,255)
#	sleep(0.05)
#	ard.lightRGB(10,10,255)
#	sleep(0.05)

