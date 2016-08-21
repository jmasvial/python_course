#!/usr/bin/env python

import telnetlib
import time

'''-------------------------------------------'''

ip_add = raw_input('Wellcome to Telnet \nPlease, enter the ip address: ')
telnet_port = 23
telnet_timeout = 6

username = raw_input('\nUsername: ')

password = raw_input('\nPassword: ')

remote_conn = telnetlib.Telnet(ip_add, telnet_port, telnet_timeout)

print 'enter the command you want to issue'

command = raw_input()

def imp_out():
	time.sleep(2)
	output = remote_conn.read_very_eager()
	print output

def cred(us, pas):
	remote_conn.write(us + '\n')
	remote_conn.write(pas + '\n')

cred(username, password)

imp_out()

output = remote_conn.write(command + '\n')

imp_out() 

remote_conn.close()
