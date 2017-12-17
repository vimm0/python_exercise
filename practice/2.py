# def compare(a, b):
# 	"""
# 	Returns 1 if a>b, 0 if a equals b, and -1 if a<b
# 	>>> compare(5, 4)
# 	1
# 	>>> compare(7, 7)
# 	0
# 	>>> compare(2, 3)
# 	-1
# 	>>> compare(42, 1)
# 	1
# 	"""
# 	if a > b:
# 		return 1
# 	elif a == b:
# 		return 0
# 	elif a < b:
# 		return -1
# if __name__ == "__main__":
# 	import doctest
# 	doctest.testmod()

import math
def hypotenuse(a, b):
	"""
	Compute the hypotenuse of a right triangle with sides of length a
	and b.
	>>> hypotenuse(3, 4)
	5.0
	>>> hypotenuse(12, 5)
	13.0
	>>> hypotenuse(7, 24)
	25.0
	>>> hypotenuse(9, 12)
	15.0
	"""
	h = math.sqrt(a*a + b*b)
	return h

if __name__ == "__main__":
	import doctest
	doctest.testmod()

