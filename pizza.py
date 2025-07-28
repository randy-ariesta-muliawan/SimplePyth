#arbitrary number of arguments

# *toppings -> tuples (list yg tdk bisa dimodifikasi)

def make_pizza(size, *toppings):
	# print(toppings)
	print(f"\nMaking a {size}cm pizza with the following toppings")
	for topping in toppings:
		print(f" - {topping}")

make_pizza(12,'pepperoni')
make_pizza(15,'pepperoni', 'pineapple', 'green peppers')

#buatkan kelas baru dgn nama Pizza, lalu tambahkan method make pizza

class Pizza:



	def __init__(self, name):
		self.name = name

	def make_pizza(self, size, *toppings):
		self.size = size
		self.toppings = toppings
		print(f"\nMaking a {self.size} cm {self.name} pizza with the following toppings")
		for topping in toppings:
			print(f" - {topping}")

pizza01 = Pizza("Meat Lovers")
pizza01.make_pizza(15, 'pepperoni', 'sausage', 'cheese')