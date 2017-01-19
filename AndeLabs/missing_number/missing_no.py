def find_missing(a,b):
	for num in a:
		b.remove(num)
	return 0 if len(b) is 0 else b[0]
