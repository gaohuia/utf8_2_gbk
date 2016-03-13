# -*- coding: utf8 -*-

from subprocess import Popen, PIPE
import sys

if len(sys.argv) == 1:
	print "python utf8_2_gbk.py [py file]"
	exit(0)

proc = Popen(["python", "-u", sys.argv[1]], stdin=sys.stdin, stdout=PIPE)

while True:
	try:
		result = proc.stdout.readline()
	except KeyboardInterrupt:
		break

	if len(result) == 0:
		break
	sys.stdout.write(result.decode("utf8").encode("gbk"))

proc.wait()