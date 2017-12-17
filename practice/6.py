# Find the charachter in the word and append in the list.

def find(strng, ch, start=0, step=1):
	index = start
	lst = []
	while 0 <= index < len(strng):
		if strng[index] == ch:
			lst.append(index)
			# return lst
		index += step
	return lst

print(find("yelolw","l"))