# import heapq
# class PriorityQueue:
# 	def __init__(self):
# 		self._queue = []
# 		self._index = 0
# 	def push(self, item, priority):
# 		heapq.heappush(self._queue, (-priority, self._index, item))
# 		self._index += 1
# 	def pop(self):
# 		return heapq.heappop(self._queue)[-1]

# class Item:
# 	def __init__(self, name):
# 		self.name=name
# 	def __repr__(self):
# 		return 'Item({!r})'.format(self.name)

#use list if u want to preserve the insertion order of the items
#use set if u want to eliminate duplicate

# heap=list(nums)
# heapq.heapify(heap)

# >>> q=PriorityQueue()
# >>> q.push(Item('foo'),1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Item' is not defined
# >>> from data_structure import Item
# >>> q.push(Item('foo'),1)
# >>> q
# <data_structure.PriorityQueue object at 0x7f20478e3c88>
# >>> print(q)
# <data_structure.PriorityQueue object at 0x7f20478e3c88>
# >>> q.push(Item('bar'),11)
# >>> q.push(Item('buzz'),21)
# >>> q
# <data_structure.PriorityQueue object at 0x7f20478e3c88>
# >>> q.count()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'PriorityQueue' object has no attribute 'count'
# >>> q.pop()
# Item('buzz')

from collections import defaultdict
# defaultdict
d = defaultdict(list)
d['a'].append(1)#{'a': [1]}
d['a'].append(2)#{'a': [1,2]}
d['b'].append(4)#{'a': [1, 2], 'b': [4]}
#implementation
d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)

# setdefault()
d = {}
d.setdefault('a', []).append(1)#{'a': [1]}
d.setdefault('a', []).append(2)#{'a': [1,2]}
d.setdefault('b', []).append(4)#{'a': [1, 2], 'b': [4]}

d = {}
for key, value in pairs:
	if key not in d:
		d[key] = []
	d[key].append(value)


#preserve order of items in dictionary.
# >>> from collections import OrderedDict
# >>> d=OrderedDict()
# >>> d['a']=1
# >>> d
# OrderedDict([('a', 1)])
# >>> d['b']=2
# >>> d['c']=3
# >>> d
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# >>> import json
# >>> json.dumps(d)
# '{"a": 1, "b": 2, "c": 3}'

#implementation
for key in d:
print(key, d[key])

#calculate dictionary values
# >>> prices = {
# ... 'ACME': 45.23,
# ... 'AAPL': 612.78,
# ... 'IBM': 205.55,
# ... 'HPQ': 37.20,
# ... 'FB': 10.75
# ... }
# >>> min_price = min(zip(prices.values(), prices.keys()))
# >>> min
# min(       min_price  
# >>> min_price
# (10.75, 'FB')
# >>> max_price = max(zip(prices.values(), prices.keys()))
# >>> max_price
# (612.78, 'AAPL')
# >>> prices_sorted = sorted(zip(prices.values(), prices.keys()))
# >>> prices_sorted
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
# zip() creates an iterator that can only be consumed once.
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names))# OK
# print(max(prices_and_names))# ValueError: max() arg is an empty sequence
#if u want to get min or max in one line
min(prices, key=lambda k: prices[k]) # Returns 'FB'
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'
prices[min(prices, key=lambda k: prices[k])]#10.75

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}
# Find keys in common
a.keys() & b.keys()
# { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys()
# { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
#if you want to eliminate duplicate values in sequence but preserve
# the order of remaining items
#makesure they are hashable
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)
# >>> a = [1, 5, 2, 1, 9, 1, 5, 10]
# >>> list(dedupe(a))
# [1, 5, 2, 9, 10]
#for unhashable type such as dict 
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)
# most frequently occuring items in a sequence
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]