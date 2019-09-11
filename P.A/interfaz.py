# -*- coding: utf-8 -*-

import hashlib, base64
import os
import serial
import mysql.connector

class interface():
	def __init__(self):
		self.u=("58acb7acccce58ffa8b953b12b5a7702bd42dae441c1ad85057fa70b")
		self.p=("58acb7acccce58ffa8b953b12b5a7702bd42dae441c1ad85057fa70b")
		self.arduinoData = serial.Serial('/dev/ttyACM0', 9600)
		self.c="MTIzNDU2"
		self.connection=mysql.connector.connect(
			host='localhost',
			user='arduino',
			password=base64.b64decode(self.c),
			db= 'iega'
			)

	def my_ar(self):
		dt = self.connection.cursor()
		os.system("clear")
		print("Waiting targets...")
		data = self.arduinoData.readline()
		print("[*]Id arduino -->",data)
		g = raw_input("Ingrese la id: ")
		n = raw_input("Ingrese el nombre: ")
		sqlFormula = "INSERT INTO listados (ID, Nombre) VALUES (%s, %s)"
		student1 = (g, n)
		dt.execute(sqlFormula, student1)
		self.connection.commit()

	os.system("clear")
	def login(self):
		m=1;
		while m < 2:
			user = raw_input("Username: ")
			password = raw_input("Password: ")
			
			e1_u=hashlib.sha224(user).hexdigest();
			e2_p=hashlib.sha224(password).hexdigest();
			
			if(e1_u == self.u and e2_p == self.p):
				m=3;
				i.my_ar()
			else:
				print("[-]Incorrect user or password")  
				os.system("clear")

i = interface()
i.login()

