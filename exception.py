student = {"name":'Leonard','student_id':15163,'feedback':None}

student['last_name'] = 'mangu'

try:
	last_name = student['last_name']
	numbered_last_name = 3 + last_name
except KeyError:
	print("Error finding last name")
except TypeError as error:
	print("The type is not supported")
	print(error)
except Exception:
	print("Unknown error")

print("This code execute")
