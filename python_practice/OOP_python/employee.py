class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' +last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        print(self.first +' '+ self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def isworkday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
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
            print(emp.fullname())
            print('-->')

#emp1 = Employee("Amir","khan", 10001)
#emp2 = Employee("Sarukh","khan", 110001)
#print(emp1.first)
#print(emp1.email)

dev1 = Developer("Aaron","swartz", 10001, 'Python')
dev2 = Developer("Alok","mitchel", 10001, 'Java')

mgr_1 = Manager('Sue','Smith',90000, [dev1])
print(mgr_1.email)
#mgr_1.add_emp(dev2)

Manager.print_emps(mgr_1)
#mgr_1.remove_emp(dev1)
#mgr_1.print_emps()
#print(dev1.email)
#print(dev1.prog_lang)
#print(dev2.prog_lang)
#
#
#print(Employee.num_of_emps)
##print(help(Developer))
#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)



#import datetime
#my_date = datetime.date(2016, 7, 10)
#print(Employee.isworkday(my_date))



#emp_str_1 = 'Julia-Doe-20000'
#emp_str_2 = 'Anna-Smith-60000'
#emp_str_3 = 'James-Cobain-70000'
#emp_str_4 = 'John-Angle-50000'
#emp_str_5 = 'Jack-Hendrix-40000'
#
#
#new_emp_1 = Employee.from_string(emp_str_1)
#new_emp_2 = Employee.from_string(emp_str_2)
#new_emp_3 = Employee.from_string(emp_str_3)
#new_emp_4 = Employee.from_string(emp_str_4)
#new_emp_5 = Employee.from_string(emp_str_5)
#print(new_emp_1.email)
#print(new_emp_2.email)
#print(new_emp_3.email)
#print(new_emp_4.email)
#print(new_emp_5.email)


#print(emp1.fullname())
#print(emp1.pay)
#print(emp2.raise_amount)
#print(Employee.set_raise_amount(1.08))
#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp1.pay)
#print(Employee.__dict__)
#print(Employee.num_of_emps)
#emp2.num_of_emps = 0
#print(emp2.num_of_emps)
#print(emp2.__dict__)

#emp3 = Employee("Salman","khan", 1110001)
#print(Employee.num_of_emps)
