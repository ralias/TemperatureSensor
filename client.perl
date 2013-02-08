#!/usr/bin/perl                                                                     
use SOAP::Lite;                                                                     
                                                                                    
print SOAP::Lite                                                                    
  -> uri('urn:/Info')                                                               
  -> proxy('http://localhost:8081')                                                 
  -> CurrentTemp()                                                                  
  -> result;
