# class Addition:
# 	def __init__(self,x,y):
# 		self.x=x
# 		self.y=y

# 	def __add__(self,x,y):
# 		return (self.x+self.y)	


# d = {}
# d["joe"] = 20
# d["bill"] = 20.232
# d["tom"] = 0.0

# a=Addition(2,3)
# print(a)
# d1 = dict((k, v) for k, v in d.iteritems() if v > 0) //outdated
# d1 = {k: v for k, v in d.items() if v > 0}
# d1 = {k:v for k,v in d.items() if v > 0}
# y = filter(lambda x:dict[x] > 0.0,dict.keys())

# print(y)

# def foo(x,y,z):
# 	print('x=',str(x))
# 	print('y=',str(y))
# 	print('z=',str(z))

# myList=[1,2,3]
# myDict={'x':1,'y':2,'z':3}
# foo(*myList)
# foo(**myDict)

def foo(param1,*param2):
	print(param1)
	print(param2)

def bar(param1,**param2):
	print(param1)
	print(param2)

foo(1,2,3,4)
bar(1,a=2,b=3,c=4)