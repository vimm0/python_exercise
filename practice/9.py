def add_lists(a, b):
	"""
	>>> add_lists([1, 1], [1, 1])
	[2, 2]
	>>> add_lists([1, 2], [1, 4])
	[2, 6]
	>>> add_lists([1, 2, 1], [1, 4, 3])
	[2, 6, 4]
	>>> list1 = [1, 2, 1]
	>>> list2 = [1, 4, 3]
	>>> sum = add_lists(list1, list2)
	>>> list1 == [1, 2, 1]
	True
	>>> list2 == [1, 4, 3]
	True
	"""
	len_a = len(a) -1
	len_b = len(b) -1
	sum_list = []
	i=0
	if len_a == len_b:
		while i <= len_a:
			sum_list.append(a[i]+b[i])
			i += 1
			# import pdb 
			# pdb.set_trace()
			# print(sum_list)
	return sum_list

if __name__ == "__main__":
	import doctest
	doctest.testmod()
