'''
- Everything is an object.
- Objects have ATRIBUTES(variables) and BEHAVIORS(methods[functions in classes]).
- Class is a DESIGN.
'''


class Computer:
    
    def config(self):
        print("i7, 64gb, 1TB")
        
comp1 = Computer()
comp2 = Computer()
Computer.config(comp1)  # i7, 64gb, 1TB
Computer.config(comp2)
comp1.config()  # i7, 64gb, 1TB



# __INIT__ METHOD

class Computer1:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print(f"Config is {self.cpu}, {self.ram}")
        
comp3 = Computer1("i5", 16)
comp4 = Computer1("i3", 32)

comp3.config() 
comp4.config()



# CONSTRUCTOR AND SELF

class Computer2:
    
    def __init__(self):
        self.name = "Bob"
        self.age = 34
        
    def update(self):
        self.age = 30
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
c5 = Computer2()
c5.age = 30
c6 = Computer2()




# TYPES OF VARIABLES
'''
- Instance variables (declared inside __init__)
- Class/static variables (declared outside __init__)
'''

class Car:
    
    wheels = 4  # class variable
    
    def __init__(self): # instance variables
        self.mill = 10
        self.com = "BMW"
        
c1 = Car()
c2 = Car()

print(c1.com, c1.mill, c1.wheels)



# TYPES OF METHODS 
'''
-Instance methods
-Class methods
-Static methods
'''

class Student:
    
    school = "UON"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3
    
    def get_m1(self):
        return self.m1
    
    @classmethod
    def info(cls):
        return cls.school
    
s1 = Student(36, 98, 47)
s2 = Student(83, 56, 92)

print(s1.average())  # 60.333333333333336
print(s2.average())  # 77.0
print(Student.info()) # UON



# INNER CLASS

class Student1:
    
    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollno)
        
    class Laptop:
        
        def __init__(self):
                self.brand = "Lenovo"
                self.cpu = "i7"
                self.ram = 128
        
s1 = Student1("Kate", 356)
s2 = Student1("John", 379)

s1.show()

lap1 = Student1.Laptop()
lap2 = Student1.Laptop()

print(lap1.brand)



# INHERITANCE

class A:
    
    def __init__(self):
        # super().__init__()
        print("In A __init__")
    
    def feature1(self):
        print("Featuer 1 working")
        
    def feature2(self):
        print("Featuer 2 working")
        
        
class B(A):
    
    def __init__(self):
        # super().__init__()
        print("In B __init__")
        
    def feature3(self):
        print("Featuer 3 working")
        
    def feature4(self):
        print("Featuer 4 working")
        
a1 = A()
b1 = B()
print(a1.feature1())
print(a1.feature2())

print(b1.feature4())



# POLYMORPHISM
'''
Duck typing
Operator overloading
Method overloading
Method overriding
'''



# DUCK TYPING

class PyCharm:
    
    def execute(self):
        print("Compiling")
        print("Running")
    

class Laptop(PyCharm):
    
    def code(self, ide):
        ide.execute()
        
ide = PyCharm()
laptop1 = Laptop()
print(laptop1.execute())



# OPERATOR OVERLOADING

