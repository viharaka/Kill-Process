#!/usr/bin/env python

import json
import sys
import time

string = sys.argv
number = len(string)

s = string[1]

parse_json = json.loads(s)
total_keys = len(parse_json.keys())
event = parse_json['type']
print "*"*100
print "%s is having total key %d"%(event,total_keys)
print 
for k,v in parse_json.items():
	print k,
	if k == "timestampMilliseconds" or k == "programPosition":
		epoch=float(v[0:10])
		print ": ",
		print time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime(epoch))
	else:
		print ": %s"%(v)
print "*"*100
