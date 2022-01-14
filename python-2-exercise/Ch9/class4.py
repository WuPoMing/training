class Employee:
    def __init__(self, name, salary=20000):
        self.name = name
        self.salary = salary
        
    def printInfo(self, title):
        print(title)
        print('Name: ', self.name)
        print('Salary: ', self.salary)    

emp1 = Employee("Sean", 50000)
emp1.printInfo('==員工一資訊==') 
emp2 = Employee("David")
emp2.printInfo('==員工二資訊==')
