#!/usr/bin/env python

import json
import yaml

with open("example_json_file.json") as f:
	new_list = json.load(f)
	print new_list

with open("example_yaml_file.yml") as f:
	new_list_1 = yaml.load(f)
	print new_list_1


