#!/usr/bin/perl
use SOAP::Lite;

print SOAP::Lite                                             
  -> uri('urn:/Info')
  -> proxy('http://localhost:8081')
  -> CurrentTemp()
  -> result;
ricard@DB003285:~/python$ cat client2.perl
#!/usr/bin/perl         

use strict;          
use warnings;

use LWP::UserAgent;
use HTTP::Request;

my $message = '<SOAP-ENV:Envelope xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/1999/XMLSchema" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:CurrentTemp xmlns:ns1="urn:/Info" SOAP-ENC:root="1"></ns1:CurrentTemp></SOAP-ENV:Body></SOAP-ENV:Envelope>';

my $userAgent = LWP::UserAgent->new();
my $request = HTTP::Request->new(POST => 'http://localhost:8081/');
$request->header(SOAPAction => '"urn:/Info"');
$request->content($message);
$request->content_type("text/xml; charset=utf-8");

my $response = $userAgent->request($request);

if ($response->code == 200) {
  print $response->as_string;
}
else {
  print $response->error_as_HTML;
}
