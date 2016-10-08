#! /bin/python

import sys

if __name__ == "__main__":
	x, y = [int(x) for x in sys.argv[1:]]
	print "%16d B"%(x * y)
	print "%16d KB"%(x * y / 1024)
	print "%16d MB"%(x * y / 1024 / 1024)
