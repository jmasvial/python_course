#!/usr/bin/env python

import pexpect
import sys
from getpass import getpass

def main():
	ip = '184.105.247.71'
	username = 'pyclass'
	password = getpass()
	port = 22

	ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip, port))
	ssh_conn.timeout = 3
	ssh_conn.expect('ssword:')
	ssh_conn.sendline(password)

	ssh_conn.expect('#')
	ssh_conn.sendline('show ip inter brief')
	ssh_conn.expect('#')
	
	print ssh_conn.before

if __name__ == "__main__":
	main()

