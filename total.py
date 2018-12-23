class Employee:
	def __init__(self,first,last):
		self.first = first
		self.last  = last

	@property
	def email(self):
		return '{}.{}@mail.com'.format(self.first.lower(),self.last.lower())

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)


	@fullname.setter
	def fullname(self,name):
		first,last = name.split(' ')
		self.first = first.title()
		self.last  = last.title()



emp1 = Employee('John','Smith')

emp1.fullname = "LEONARD MANGU"

print(emp1.first)
print(emp1.email)

print(emp1.fullname)
