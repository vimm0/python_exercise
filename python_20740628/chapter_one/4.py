def sum_list(lst):
	result = 0
	print("sum:")
	for num in lst:
		result+=num
	return result


def multiply_list(lst):
	result = 1
	print("Multiply:")
	for num in lst:
		result*=num
	return result
	
print(sum_list([1,2,3]))
print(multiply_list([1,2,3]))