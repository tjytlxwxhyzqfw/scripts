#! /bin/python

import sys
if __name__ == "__main__":
	n = int(sys.argv[1])
	for i in range(32):
		if pow(2, i) >= n:
			break
	print "%8s: %d"%("n", n)
	print "%8s: %d"%("round", pow(2, i))
	print "%8s: %d"%("size", pow(2, i+1))
	print "%8s: %d"%("offset", i+1)
