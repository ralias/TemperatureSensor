#!/usr/bin/python
import SOAPpy

class Info:
        def CurrentTemp(self) :
#tfile = open("/sys/bus/w1/devices/28-*/w1_slave")
                File = open("./w1_slave")
                TextFile = File.read()
                File.close()
                SecondLine = TextFile.split("\n")[1]
                TemperatureData = SecondLine.split(" ")[9]
                Temperature = float(TemperatureData[2:])
                Temperature = Temperature / 1000
                return Temperature

Server = SOAPpy.SOAPServer(("localhost",8081))
Server.registerObject(Info(),"urn:/Info")
Server.config.dumpSOAPOut = 1
Server.config.dumpSOAPIn  = 1
Server.serve_forever()
