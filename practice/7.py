def remove_extension(name):
	"""
	>>> remove_extension("tst.txt")
	'tst'
	>>> remove_extension("tst.2.txt")
	'tst.2'
	"""
	if name:
		return name[:-4]

if __name__ == "__main__":
	import doctest
	doctest.testmod()

remove_extension("tst.txt")