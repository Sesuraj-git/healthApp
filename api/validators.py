from django.core.exceptions import ValidationError

def valid_mob(value):
	print ("In valid_mob")
	print ("val is ",value)
	try:
		if (int(value) >=7000000000 and int(value)<=9999999999):
			return value
		else:
			raise ValidationError("Not a valid Number")
	except:
		pass


# 