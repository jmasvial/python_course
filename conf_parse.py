from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")


cryptoline = cisco_cfg.find_objects(r"^crypto map CRYPTO")


for i in cryptoline:
	print i.text


