if __name__ == "__main__":
	f = open("segtree", "r")
	result = []
	for ln in f:
		result.append(int(ln.strip()))
	f.close()
	q = -1
	total = 0
	for p in sorted(result):
		if p != q:
			i = 1
			total += 1
			print ""
		print "%d: %d\r"%(p, i),
		q = p
		i += 1
	print "total: %d"%total
