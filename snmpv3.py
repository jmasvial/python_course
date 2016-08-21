#!/usr/bin/env python

import snmp_helper

ip = '184.105.247.70'
a_user = 'pysnmp'
auth_key = 'galileo1'
encry_key = 'galileo1'
snmp_user = (a_user, auth_key, encry_key)
pynet_rtr1 = (ip, 161)

snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.1.5.0')
#print snmp_data
output = snmp_helper.snmp_extract(snmp_data)
print output

