#!/usr/bin/env python

import telnetlib
import time

ip_add = '184.105.247.70'
telnet_port = 23
telnet_timeout = 6

username = 'pyclass'
password = '88newclass'

remote_conn = telnetlib.Telnet(ip_add, telnet_port, telnet_timeout)

def imp_out():
	time.sleep(2)
	output = remote_conn.read_very_eager()
	print output

def cred(us, pas):
	remote_conn.write(us + '\n')
	remote_conn.write(pas + '\n')

cred(username, password)

imp_out()

output = remote_conn.write('show ip inter brief' + '\n')

imp_out() 

remote_conn.close()


