def is_member(el, lst):
	for num in lst:
		if num == el:
			return True
		else:
			return False


print(is_member('e', ['a','e','i','o','u']))