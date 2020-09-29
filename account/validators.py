from django.core.exceptions import ValidationError

class ConsecutivelyRepeatingCharacterValditor:
	def __init__(self, length=3):
		self.length = length 

	def validate(self, password, user=None):
		for character in password:
			if password.count(character) >= self.length:
				check_character = character * self.length
				if check_character in password:
					raise ValidationError(
					('رمز عبورتون یک سری حروف داره که داره تکرار میشه.(:')

				)


	def get_help_text(self):from django.core.exceptions import ValidationError
class ConsecutivelyIncreasingIntegarValidator:    
	def __init__(self, length=3):
		self.length = length 

	def validate(self, password, user=None):
		for character in password:
			if character.is_digit():
				count = 0 
				number = int(character)
				index = password.index(character)

				try:
					for i in range(1, self.length + 1):
						if password[index+i].is_digit():
							if int(password[index+i]) == number + 1:
								number +=1
								count +=1

								while count >= self.length:
									raise ValidationError(
									"اعداد داخل رمز عبور به صورت افزایشی ان! . /n این باعث میشه امنیتش کم شه :( مث ۱۲۳۴"
								
								)
				except IndexError:
					pass
		

	def get_help_text(self):
		return (' اعداد داخل رمز عبور نمیتونن به صورت اقزایشی باشن مثل ۵۶۷۸ ')




class ConsecutivelyDecreasingIntegerValidator:
	def __init__(self, length=3):
		self.length = length 

	def validate(self, password, user=None):
		for character in password:
			if character.is_digit():
				count = 0 
				number = int(character)
				index = password.index(character)

				try:
					for i in range(1, self.length + 1):
						if password[index+i].is_digit():
							if int(password[index+i]) == number - 1:
								number -=1
								count +=1

								while count >= self.length:
									raise ValidationError(
									"اعداد داخل رمز عبور به صورت کاهشیه. /n این باعث میشه امنیتش کم شه :( مث 4321"
								
								)
				except IndexError:
					pass
		

	def get_help_text(self):
		return (' اعداد داخل رمز عبور نمیتونن به صورت کاهشی باشن مثل 9876 ')
                                      
class ContextValidator:
	def validate(self,password,user=None):
		with open('./prozesh.txt') as file:
			context = file.read().splitlines()
			for word in context:
				if word in password:
					raise ValidationError(
				'مرد باش رمز ربط دار به سایت  نزار !'
				)


	def get_help_text(self):
		return ('')