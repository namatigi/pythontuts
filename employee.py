class Employee:

	raise_amount = 1.04
	num_emps = 0
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@phronetech.com'
		Employee.num_emps +=1	
	

	def fullname(self):
		return self.first +' '+ self.last

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True

class Developer(Employee):
	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		#Employee.__init__(self,first,last,pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self,first,last,pay,employees =None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)


	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.fullname())
		


#print(Employee.num_emps)

emp1 = Employee('leonard','mangu',50000)
 
emp2 = Employee('alex','paul',1000000)


#Employee.set_raise_amt(1.05)

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

#print(Employee.__dict__)

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

#print(Employee.num_emps)


emp_str_1 = 'John-Doe-700000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3  = 'Jane-Doe-900000'


first,last,pay = emp_str_1.split('-')

new_emp1 = Employee(first,last,pay)

new_emp2 = Employee.from_string(emp_str_2)

print(new_emp1.fullname())

print(new_emp2.fullname())


import datetime
my_date = datetime.date(2018,12,23)

print(Employee.is_workday(my_date))


dev1 = Developer('John','Levi',563000,'Python')
dev2 = Developer('Salim','Said',754000,'JAVA')



mgr1 = Manager('Sue','Smith',90000,[dev1])

print(mgr1.email)

mgr1.add_emp(dev2)

mgr1.remove_emp(dev1)

mgr1.print_emps()

print(issubclass(Developer,Employee))



#print(dev1.fullname())

#print(help(Developer))

#print(dev1.prog_lang)
#print(dev1.email)

#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)
