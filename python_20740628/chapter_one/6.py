def check_palindrome(str):
	return str == str[::-1]


print(check_palindrome('palpa'))
print(check_palindrome('radar'))