#aribitrary keyword arguments

def build_profile(**user_info):
	# user_info = {}
	# user_info['first_name'] = first_name
	# user_info['last_name'] = last_name
	return user_info

user_01 = build_profile(first_name='kenny', last_name='matady', school='SMP IGS', hobby='gelud')

print(user_01)

#jadikan method di class User 