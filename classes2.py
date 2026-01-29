#classes
#creating a class
class Employee:
    #class variables
    no_of_emp=0
    sal_raise=1.05

    #constructor method
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+'.'+last+'@company.com'
        #class variable
        Employee.no_of_emp +=1

    #=========================
    #different methods
    #=========================

    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*self.sal_raise)
    

#instances
print(Employee.no_of_emp)
emp_1=Employee('Rohit','sharma',50000)
emp_2=Employee('Naresh','kumar',40000)
emp_3=Employee('Arijith','singh',60000)

print(emp_1.first)
print(emp_2.last)
print(emp_3.fullname())
print(Employee.no_of_emp,'Employees')

print(emp_2.sal_raise)

Employee.apply_raise(emp_2)
print(emp_2.pay)
emp_1.apply_raise()
print(emp_1.pay)
