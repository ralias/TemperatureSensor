#!/usr/bin/python
import SOAPpy
import time
import os,sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

#Server Config Definition
Server = SOAPpy.SOAPServer(("192.168.1.110",8081))

#Sensor Config Definition
Sensor = SOAPpy.SOAPProxy("http://192.168.1.100:8081/")
SenSorStatus = 1
try:
        CurrentTemperature = Sensor.CurrentTemp()
except:
        e = sys.exc_info()[0]
        CurrentTemperature = 50
        SensorStatus = 0
DesiredTemperature = 0

def GetCurrentTemp():                                                                                               
        global SensorStatus                                                                                         
        SensorStatus = 1                                                                                            
        global CurrentTemperature                                                                                   
        try:                                                                                                        
                CurrentTemperature = Sensor.CurrentTemp()                                                           
        except:                                                                                                     
                e = sys.exc_info()[0]                                                                               
                SensorStatus = 0                                                                                    
        return CurrentTemperature                                                                                   
                                                                                                                    
def PutDesiredTemp(x):                                                                                              
        global DesiredTemperature                                                                                   
        DesiredTemperature = x
        return

def GetDesiredTemp():
        global DesiredTemperture
        return DesiredTemperature

def GetStatusSensor():
        global SensorStatus
        return SensorStatus

def RefreshBoiler(x):
        global CurrentTemperature
        global DesiredTemperature
        global SensorStatus

        if SensorStatus:
                if CurrentTemperature < DesiredTemperature:
                        GPIO.output(18, GPIO.HIGH)
                        return 1
                else:
                        GPIO.output(18, GPIO.LOW)
                        return 0
        else:
                if x == 1:
                        GPIO.output(18, GPIO.HIGH)
                        return 1
                else:
                        GPIO.output(18, GPIO.LOW)
                        return 0
Server.registerFunction(GetCurrentTemp)
Server.registerFunction(PutDesiredTemp)
Server.registerFunction(GetDesiredTemp)
Server.registerFunction(GetStatusSensor)
Server.registerFunction(RefreshBoiler)
os.system("clear")
Server.serve_forever()
