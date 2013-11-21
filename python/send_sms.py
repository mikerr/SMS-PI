#!/usr/bin/python
#-----------------------------------
# Send SMS Text Message
#
# Author : Robert Wiggins
# Site   : http://www.smspi.co.uk
# Date   : 01/10/2013
#
# Altered Script from Matt Hawkins of http://www.raspberrypi-spy.co.uk/
# 
#
#-----------------------------------

# Import required libraries
import urllib      # URL functions
import urllib2     # URL functions
import sys		   # System Function

# Arguments Taken from command line

number = sys.argv[1]
message = sys.argv[2]


#-----------------------------------
# No need to edit anything below this line
#-----------------------------------

values = {
          'message' : message,
          'number'    : number,
          'hash' : "xxxxxxxxxxxxxxxxxxxxxxxxxx"} # Grab your hash from http://www.rwsupport.info

url = 'http://www.smspi.co.uk/send/'

postdata = urllib.urlencode(values)
req = urllib2.Request(url, postdata)

print 'Attempt to send SMS ...'

try:
  response = urllib2.urlopen(req)
  response_url = response.geturl()
  if response_url==url:
    print 'SMS sent!'
    print message
    print number
except urllib2.URLError, e:
  print 'Send failed!'
  print e.reason