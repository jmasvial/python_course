!#/usr/bin/env python

import paramiko
#from getpass import getpass

ip_addr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'

port = 22

remote_conn_pre = paramiko.SSHClient()

print remote_conn_pre

#ssh keys
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#init conection
remote_conn_pre.connect(ip_addr, username = username, password = password, look_for_keys = False,  allow_agent = False, port = port)

remote_conn = remote_conn_pre.invoke_shell()

remote_conn = remote_conn.recv(5000)
remote_conn = remote_conn.send("terminal length 0\n")
remote_conn = remote_conn.send("show ver\n")
remote_conn = remote_conn.recv(5000)
print remote_conn


'''
print var

var = remote_conn.send("show ip inter brief\n")
var = remote_conn.recv(3000)
print var '''
