class User:

	def __init__(self, username, password, f_name, l_name):
		self.username = username
		self.password = password
		self.f_name = f_name
		self.l_name = l_name
		self.login_attempts = 0 #DEFAULT VALUE ON ATTRIBUTES

	def build_profile(**user_info):
	# user_info = {}
	# user_info['first_name'] = first_name
	# user_info['last_name'] = last_name
		return user_info

	user_01 = build_profile(first_name='kenny', last_name='matady', school='SMP IGS', hobby='gelud')
	print(user_01)

	def greet_user(self):
		print(f"Hello my name is {self.f_name.title()} {self.l_name.title()}, nice to meet you ...")

	def increment_login_attempts(self):
		self.login_attempts += 1
		# self.login_attempts = self.login_attempts + 1

	def decrement_login_attempts(self):
		self.login_attempts -= 1

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("Login sudah direset ...")

class Privileges:

	def __init__(self, privileges=[]):
		self.list_privileges = privileges

	def show_privileges(self):
		print('Privileges')
		for privileges in self.list_privileges:
			print(privileges.title())


class Admin(User):

	def __init__(self, username, password, f_name, l_name, is_active=True):
		super().__init__(username, password, f_name, l_name)
		self.is_active = is_active
		self.privileges = Privileges(privileges = ['can create post', 'can delete post', 'can edit post', 'can share post', 'can ban user'])



userAdmin = Admin('tono', '12345', 'Tono', 'Subagio')
userAdmin.privileges.show_privileges()
"""
user1 = User('budi', '12345', 'Budi', 'Siregar')
print(user1.f_name)
print(user1.l_name)
user1.greet_user()

print(user1.login_attempts) #0
user1.increment_login_attempts()
print(user1.login_attempts) #1
user1.reset_login_attempts()
print(user1.login_attempts) #0
user1.decrement_login_attempts()
print(user1.login_attempts)
"""