class Person :
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        print('Hello,', self.name)

p1 = Person('Amy')
greet = p1.sayHello

# 三個寫法意義相同
p1.sayHello()
Person.sayHello(p1)
greet()
