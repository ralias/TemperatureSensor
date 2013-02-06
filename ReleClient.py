#!/usr/bin/python
import SOAPpy
import time
import os

#server = SOAPpy.SOAPProxy("http://192.168.1.100:8080/")
Rele = SOAPpy.SOAPProxy("http://192.168.1.110:8081/")

while 1 :
	os.system("clear")
	print "Insert the desired temperature: "
	number = input()
	Rele.PutDesiredTemp(number)
