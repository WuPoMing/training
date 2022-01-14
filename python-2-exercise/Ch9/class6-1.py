class Employee:
    company = '巨匠電腦'
    phone = '(02)2311-4537'

    def __init__(self, name, salary=20000):
        self.name = name
        self.salary = salary 
        
    def printInfo(self):
        print('==員工資訊==')
        print('姓名:', self.name)
        print('薪水:', self.salary)        
        #print('電話:', Employee.phone)
        print('電話:', self.phone)
        
emp1 = Employee("Sean", 50000)
emp2 = Employee("David")

print(Employee.company+'員工資訊')
emp1.printInfo() 
emp2.printInfo()
print('')

emp1.phone = "0987-654-321"
print(emp1.company+'員工資訊')
emp1.printInfo()
emp2.printInfo()
