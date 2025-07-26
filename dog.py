class Dog:
	#simple model of dog

	def __init__(self, name, dog_type, fav_meals):
		self.name = name #attribute
		self.type = dog_type #attribute
		self.fav_meals = fav_meals
		self.sit()

	def sit(self):
		print(f"{self.name.title()} is sitting now.")


Willie = Dog(dog_type ='Kintamani', name= 'Willie', fav_meals= ['Salt Cheese', 'Salt Egg'])
Sam = Dog(dog_type='husky', name='sam', fav_meals=['Wiskas'])

print(Willie.name)
print(Willie.fav_meals)
# Willie.sit()