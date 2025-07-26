
class Mouth:

	def __init__(self, body, *syndrom, color="red"):
			self.body = body
			self.color = color
			self.syndrom = syndrom

	def speak_about_body(self):
		print(f"\nWeight = {self.body.weight} and height = {self.body.height}")

	def explain_my_body(self):
		print(self.body)


class Body:

	def __init__(self, weight, height):
		self.weight = weight
		self.height = height

		#other parts
		self.mouth = Mouth(self, "bengkak", "nyeri", "berdarah", color="blue")

	def something(self):
		print(self.weight)

my_body = Body(80, 171)
my_body.mouth.speak_about_body()
my_body.mouth.explain_my_body()