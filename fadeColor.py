import time
import test
test.ard.lightRGB(255,255,255)

def fade(colorA, colorB, ignore_color):
    ignore_color(0)
    for i in range(0,255):
	    colorA(255-i)
	    colorB(i)
	    time.sleep(0.1)
	
while True:
    fade(test.ard.setR, test.ard.setG, test.ard.setB)
    fade(test.ard.setG, test.ard.setB, test.ard.setR)
    fade(test.ard.setB, test.ard.setR, test.ard.setG)
