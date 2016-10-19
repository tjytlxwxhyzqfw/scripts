#! /bin/python

import os
import sys

def freadlns(path, strip=True):
	inf = open(path, "r")
	lns = [x for x in inf]
	inf.close()

	lns = filter(lambda x:x.strip() != "", lns)
	if strip:
		lns = [x.strip() for x in lns]

	return lns

class Case(object):
	def __init__(self, path):
		self.lns = freadlns(path)
	def nxt(self):
		i, length = 0, len(self.lns)
		while i < length:
			size = int(self.lns[i])
			if size == 0:
				break
			case = "\n".join(self.lns[i+1:i+size+1])
			yield case
			i += size+1

def test(cmd, path):
	case = Case(path)
	for string in case.nxt():
		print string
		os.system("echo '%s' | %s"%(string, cmd))

if __name__ == "__main__":
	cmd, path = sys.argv[1:3]
	test(cmd, path)
