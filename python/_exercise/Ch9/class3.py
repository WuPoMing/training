class Employee:
    def __init__(self, name, salary=20000):
        self.name = name
        self.salary = salary

emp1 = Employee("Sean", 50000)
print('==員工一資訊==') 
print('Name: ', emp1.name)
print('Salary: ', emp1.salary)

emp2 = Employee("David")
print('==員工二資訊==') 
print('Name: ', emp2.name)
print('Salary: ', emp2.salary)
