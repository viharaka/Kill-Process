import commands
import sys
import re

arg_list = sys.argv
arg_num = len(sys.argv)

for x in xrange(1,arg_num):
	status, output = commands.getstatusoutput("ps -A | grep "+arg_list[x])
	print "Found proces : %s"%output
	fi = re.findall(r'\d+',output)
	print "found %s"%fi
	if fi:
		k = filter(lambda x:re.search(r'\d{4}',x) , fi)
		for pid in k:
			print "Going to kill process having pid: "+pid
			status, output = commands.getstatusoutput("sudo kill -9 "+pid)
			print "Status:"+str(status)
	else:
		print "Not able to kill the defined process"
