# from user import User, Admin
# from user import *
import user
import math

user01 = user.User('andisiregar', '12345', 'Andi', 'Siregar')
user01.greet_user()

admin01 = user.Admin('budi', 'qwerty', 'Budi', 'Gunawan')
admin01.greet_user()

print(math.sin(math.radians(60)))