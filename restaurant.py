class Restaurant:

	def __init__(self, restaurant_name, cuisinte_type):
		self.restaurant_name = restaurant_name
		self.cuisinte_type = cuisinte_type
		self.number_served = 0
		self.number_attempts = 0

	def describe_restaurant(self):
		print(f"Restoran {self.restaurant_name.title()} menyediakan makanan {self.cuisinte_type} ")

	def open_restaurant(self):
		print(f"Restoran {self.restaurant_name.title()} sudah buka dan dapat melayani Anda.")

	def set_number_served(self, new_number):
		self.number_served = new_number

	def increment_number_attempts(self):
		self.number_attempts += 1

class IceCreamFlavor:
	def __init__(self):
		self.list_rasa_es_krim = ['rasa coklat', 'rasa vanila', 'rasa stroberi', 'rasa blueberry', 'rasa anggur']
	def show_flavor(self):
		print('=== Rasa Es Krim ===')
		for rasa_es_krim in self.list_rasa_es_krim:
			print(rasa_es_krim.title())
		print('====================')

class IceCream(Restaurant):
	def __init__(self,restaurant_name, cuisinte_type):
		super().__init__(restaurant_name,cuisinte_type)
		self.rasa_es_krim = IceCreamFlavor()

RestaurantIceCream = IceCream('kedai es krim', 'ice cream\t')
RestaurantIceCream.rasa_es_krim.show_flavor()


PagiSore = Restaurant("\nPagi Sore", "Masakan Padang")

print(PagiSore.restaurant_name)
print(PagiSore.cuisinte_type)
PagiSore.describe_restaurant()
PagiSore.open_restaurant()
print(PagiSore.number_served)
PagiSore.set_number_served(8)
print(PagiSore.number_served)
PagiSore.increment_number_attempts()
print(PagiSore.number_served)


SelatanIndah = Restaurant("Selatan Indah", "Makanan Chinese")

print(SelatanIndah.restaurant_name)
print(SelatanIndah.cuisinte_type)
SelatanIndah.describe_restaurant()
SelatanIndah.open_restaurant()
print(SelatanIndah.number_served)
SelatanIndah.set_number_served(8)
print(SelatanIndah.number_served)
SelatanIndah.increment_number_attempts()
print(SelatanIndah.number_served)