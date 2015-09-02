import ArduinoCarPi
from time import sleep
ard = ArduinoCarPi.Arduino("/dev/ttyAMA0")
ard.registerLEDs(9,10,11)
currentR = 0
currentG = 0
currentB = 0
while True:
	for c in range(0,3):
		for i in range(0,250):
			R = 0
			G = 0
			B = 0
			if c == 0:
				R = i
				currentR = i
			elif c == 1:
				G = i
				currentG = i 
			else:
				B = i 	
				currentB = i		
			ard.lightRGB(R,G,B)
			sleep(0.05)
                for i in range(250,0,-1):
                        R = 0
                        G = 0
                        B = 0
                        if c == 0:
                                R = i
                                currentR = i
                        elif c == 1:
                                G = i
                                currentG = i
                        else:
                                B = i
                                currentB = i
                        ard.lightRGB(R,G,B)
                        sleep(0.05)

