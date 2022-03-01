class Employee:
    count = 0
    company = '巨匠電腦'
    phone = '(02)2311-4537'

    def __init__(self, name, salary=20000):
        Employee.count+=1
        self.id = Employee.count
        self.name = name
        self.salary = salary        
        
    def printInfo(self):
        print('==員工資訊==')
        print('員工編號:', self.id)
        print('姓名:', self.name)
        print('薪水: ', self.salary)
        print('電話:', self.phone)

    def getTotal():
        return Employee.count

emp1 = Employee("Sean", 50000)

print(Employee.company+'員工資訊')
print('員工人數:', Employee.getTotal())
emp1.printInfo()

print("\n新增員工............")
emp2 = Employee("David")
print(emp2.company+'員工資訊')
#print('員工人數:', emp2.getTotal())
print('員工人數:', Employee.getTotal())
emp1.printInfo() 
emp2.printInfo()
