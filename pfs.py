from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

cryptoline = cisco_cfg.find_objects(r"^crypto map CRYPTO")

j = 0

for i in cryptoline:


	cryptoline = cisco_cfg.find_objects(r"^crypto map CRYPTO")

	cryptoline = cryptoline[j]

	for x in cryptoline.children:
		
		cryptoline_1 = cryptoline.find_objects(r"^PFS group2")

		for k in cryptoline_1:
			print k.text

	j = j + 1

