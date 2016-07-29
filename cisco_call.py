from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

cryptoline = cisco_cfg.find_objects(r"^crypto map CRYPTO")

j = 0

for i in cryptoline:
	print i.text

	cryptoline = cisco_cfg.find_objects(r"^crypto map CRYPTO")

	cryptoline = cryptoline[j]

	for x in cryptoline.children:
		print x.text 

	j = j + 1




