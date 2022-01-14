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

    def getCompany():
        return Employee.company

    @staticmethod
    def getTotal():
        return Employee.count

    @classmethod
    def setPhone(cls, phone):
        cls.phone = phone
        

emp1 = Employee("Sean", 50000)

print(Employee.getCompany()+'員工資訊')
print('員工人數:', emp1.getTotal())
emp1.printInfo()
print()

emp2 = Employee("David")
Employee.setPhone("(02)2382-6015")
print(Employee.getCompany()+'員工資訊')
print('員工人數:', Employee.getTotal())
emp1.printInfo() 
emp2.printInfo()



