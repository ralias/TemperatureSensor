#!/usr/bin/python
import SOAPpy
import time
import os

#server = SOAPpy.SOAPProxy("http://192.168.1.100:8080/")
Rele = SOAPpy.SOAPProxy("http://192.168.1.110:8081/")

#Rele.PutDesiredTemp(30)
#print Rele.GetDesiredTemp()
while 1 :
	os.system('clear')
	print ("Actual Temperature " + str(Rele.GetCurrentTemp()))
	print ("Desired Temperature " + str(Rele.GetDesiredTemp()))
	if Rele.GetStatusSensor():
		print "Sensor Status sending data..."
	else:
		print "No sensor data received..."

	if Rele.RefreshBoiler(0):
		print "Boiler Running..."
	else:
		print "Boiler Stopped..."
	time.sleep(1)
