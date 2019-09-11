import base64
import serial
import mysql.connector
import time

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
		self.t1 = ('2DB17D83\r\n')									#Serial tarjeta
		#self.t2 = ('507D85A6\r\n')
			
	def my_ar(self):
		dt = self.connection.cursor()
		sql = "SELECT * FROM listados".format(0)
		dt.execute(sql)
		results = dt.fetchall()
		for row in results:
			id = row[0]
			name = row[1]
			#print ("id = {0}, name = {1}".format(id,name))
		print ("Waiting targets...")
		data = self.arduinoData.readline()						#Lee los datos del arduino
		if data == self.t1 or self.t2:
			print data
			self.arduinoData.close()
			print ("Ok")
			i = 1
			while i < 2:
				self.arduinoData.write(str(180).encode())
				for s in range(0, 5):
					time.sleep(1)
				self.arduinoData.write(str(0).encode())
				for s in range(0, 5):
					time.sleep(1)
				i=2
		else:
			print data
			print ("Denied")
					
v = verify()
v.my_ar()


