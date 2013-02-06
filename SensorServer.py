#!/usr/bin/python
import SOAPpy
import os

def CurrentTemp():
        File = open("/sys/bus/w1/devices/28-00000400b7b5/w1_slave")
        TextFile = File.read()
        File.close()
        SecondLine = TextFile.split("\n")[1]
        TemperatureData = SecondLine.split(" ")[9]
        Temperature = float(TemperatureData[2:])
        Temperature = Temperature / 1000
        return Temperature

Server = SOAPpy.SOAPServer(("192.168.1.100",8081))
Server.registerFunction(CurrentTemp)

os.system("clear")

Server.serve_forever()
