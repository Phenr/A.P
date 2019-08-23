import base64
import serial
import mysql.connector

class verify():
	def __init__(self):
		self.arduinoData = serial.Serial('/dev/ttyACM0', 9600) 	#Conexion placa aruino
		self.c="MTIzNDU2"
		self.connection=mysql.connector.connect(				#Conexion base de datos mysql
			host='localhost',
			user='arduino',
			password=base64.b64decode(self.c),
			db= 'iega'
			)
		self.t = ('2DB17D83\r\n')									#Serial tarjeta
			
	def my_ar(self):
		#dt = self.connection.cursor()
		print ("Waiting targets...")
		data = self.arduinoData.readline()						#Lee los datos del arduino
		print data
		if data == self.t:
			print ("Ok")
		else:
			print ("Denied")
					
v = verify()
v.my_ar()


