class Animal():
	name='Andy'
	color='Brown'
	noise="ruff!!"
	@property
	def make_noise(self):
		return self.noise

	def get_color(self,abc):
		return self.color+" "+ abc
#Positional arguments and Keyword arguments
	def some_func(*args, **kwargs): 
		print(args)
		print(kwargs)

# some_func(12,15,6,79,76,68,87,66,a="a")
Dog=Animal()
print(Dog.make_noise)
print(Dog.get_color('yellow'))
