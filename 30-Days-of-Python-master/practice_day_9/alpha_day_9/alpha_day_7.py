class Animal():
	name='Andy'
	color='Brown'
	noise="ruff!!"
	gene="Dog"
	hair="small"
	size="Big"
	@property
	def animal_name(self):
		return self.name
	@property
	def animal_color(self):
		return self.color
	@property
	def animal_noise(self):
		return self.noise
	@property
	def animal_gene(self):
		return self.gene
	@property
	def animal_hair(self):
		return self.hair
	@property
	def animal_size(self):
		return self.size

a=Animal()
print("I have a pet having properties")
print("	name=",a.animal_name)
print("	color=",a.animal_color)
print("	noise=",a.animal_noise)
print("	gene=",a.animal_gene)
print("	hair=",a.animal_hair)
print("	size=",a.animal_size)