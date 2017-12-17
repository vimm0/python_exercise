vowels = ['a','e','i','o','u']

def vowelornot(str):
	if str in vowels:
		return True
	else:
		return False

print(vowelornot('a'))
print(vowelornot('b'))