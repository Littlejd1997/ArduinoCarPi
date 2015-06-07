import serial
class Arduino:
	def __init__(self, port):
		self.port = port;
		self.socket = serial.Serial(self.port);
		self.socket.baudrate = 115200
		self.R = 0
		self.G = 0
		self.B = 0;
	def registerLEDs(self,R,G,B):
		self.R = R
		self.G = G
		self.B = B
		self.socket.write("1 "+str(R)+" "+str(G)+" "+str(B)+"\n");
	def lightRGB(self,R,G,B):
		R = 255 if (R > 255) else R 
		G = 255 if (G > 255) else G
		B = 255 if (B > 255) else B
		message = "2 "+str(int(R))+" "+str(int(G))+" "+str(int(B))+"\n"
		self.socket.write(message);
		print message;
