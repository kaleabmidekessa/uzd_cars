# # # class Vehicle:
# # #     def __init__(self,name,max_speed,mileage):
# # #         self.name = name
# # #         self.max_speed = max_speed
# # #         self.mileage = mileage

# # # vehicle1 = Vehicle('Tesla Model S', 250, 18)
# # # print(f'Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}')


# # #Rectangle Class with Area & Perimeter
# # # class Rectangle:
# # #     def __init__(self,length,width):
# # #         self.length = length
# # #         self.width = width

# # #     def get_area(self):
# # #         area = self.length*self.width
# # #         return area

# # #     def get_perimeter(self):
# # #         perimeter = 2*(self.length + self.width)
# # #         return perimeter

# # # rect = Rectangle(10,4)
# # # print(f'Area= {rect.get_area()}')
# # # print(f'Perimeter= {rect.get_perimeter()}')

# # # Student class with Average Grade
# # # class Student:
# # #     def __init__(self, name, marks):
# # #         self.name = name
# # #         self.marks = marks

# # #     def average(self):
# # #         average = sum(self.marks) / len(self.marks)
# # #         return average

# # # aver = Student('Alice', [85,90,78,92,88])
# # # print(f'{aver.name}"s Average Grade :{aver.average()}')

# # # Product class with stock value calculator
# # # class Product:
# # #     def __init__(self, name, price, quantity):
# # #         self.name = name
# # #         self.price = price
# # #         self.quantity = quantity

# # #     def total_value(self):
# # #         return self.price*self.quantity

# # # p1 = Product('Laptop', 899.99, 5)
# # # print(f'Total stock value of {p1.name}: ${p1.total_value():.1f}')

# # # Bank Account with Deposit & Overdaw Protection

# # # class BankAccount:
# # #     def __init__(self, balance):
# # #         self.balance = balance

# # #     def deposit(self, amount):
# # #         return self.balance+amount
# # #     def withdraw(self, amount):
# # #         return self.balance-amount

# # # ba = BankAccount(1000, 500)
# # # print(f'Balance after deposit: {ba.deposit(amount)}')

# # # 70 to 128 is corey schauffers course
# # # class Employee:

# # #     num_of_employees=0  # to keep track of how many employees we have

# # #     raise_amount = 1.04

# # #     def __init__(self,first, last, pay):
# # #         self.first = first
# # #         self.last = last
# # #         self.pay = pay
# # #         self.email = first + '.' + last + '@company.com'
# # #         Employee.num_of_employees += 1

# # #     def fullname(self):
# # #         return f'{self.first} {self.last}'

# # #     def apply_raise(self):
# # #         return int(self.pay*self.raise_amount)

# # #     @classmethod
# # #     def set_raise_amount(cls, amount):
# # #         cls.raise_amount = amount


# # #     @classmethod
# # #     def new_data(cls,empstr):
# # #         first,last,pay = empstr.split('-')
# # #         return cls(first,last,pay)
# # # emp1 = Employee('kaleab', 'midekessa', 50000)
# # # emp2 = Employee('Helen', 'Tilahun', 100000)
# # # # emp2.raise_amount=1.08
# # # # emp1.set_raise_amount(2)
# # # # Employee.set_raise_amount(1.09)
# # # # emp1.raise_amount = 1.09
# # # # print(Employee.fullname(emp1))
# # # # print(Employee.apply_raise(emp1))
# # # # print(emp1.apply_raise())
# # # # print(Employee.raise_amount)
# # # # print(emp1.raise_amount)
# # # # print(emp2.raise_amount)
# # # # print(Employee.raise_amount)
# # # # print(Employee.num_of_employees)
# # # # print(Employee.__dict__)

# # # empstr1 = 'John-Doe-70000'
# # # empstr2 = 'Steven-Smith-30000'

# # # # first,last,pay = empstr1.split('-')
# # # # firstt,lastt,payy = empstr2.split('-')
# # # # newemp3=Employee(first,last,pay)
# # # # newemp4=Employee(firstt,lastt,payy)
# # # # print(newemp3.email)
# # # # print(newemp4.email)

# # # newemp3=Employee.new_data(empstr1)
# # # newemp4=Employee.new_data(empstr2)

# # # print(newemp3.email)
# # # print(newemp4.email)


# # # class Light:
# # #     def __init__(self):
# # #         self.is_on = False

# # #     def turn_on(self):
# # #         self.is_on=True
# # #         print('lights are on')

# # #     def turn_off(self):
# # #         self.is_on=False
# # #         print('lights are off')

# # #     def status(self):
# # #         if self.is_on==True:
# # #             print('Current status: ON')
# # #         else:
# # #             print('Current status: Off')

# # # light=Light()
# # # light.turn_on()
# # # light.status()
# # # light.turn_off()
# # # light.status()

# # #user class with password validation
# # # class User:
# # #     def __init__(self, username, password):
# # #         self.username = username
# # #         self.password = password

# # #     def check_password(self,input_password):
# # #         return input_password == self.password
          
# # # user=User('alice', 'secure123')
# # # x=input('password: ') 
# # # print(user.check_password(x))
# # # print(user.check_password(x))



# # #Temperature class with unit converters
# # # class Temperature:
# # #     def __init__(self, celsius):
# # #         self.celsius=celsius

# # #     def to_fahrenheit(self):
# # #         return (self.celsius*9/5)+32

# # #     def to_kelvin(self):
# # #         return self.celsius + 273.15

# # # temp=Temperature(100)
# # # print(temp.to_fahrenheit())
# # # print(temp.to_kelvin())

# # class Notebook:
    
# #     def __init__(self):
# #         self.notes=[]

# #     def add_note(self, note):
# #         self.notes.append(note)

# #     def show_notes(self):
# #         for i,note in enumerate(self.notes, start = 1):
# #             print(f'{i} {note}')

# # n = Notebook()
# # n.add_note('kaleab')
# # n.add_note('sucks')
# # n.add_note('yeeah')
# # n.show_notes()



# x = ["abebe","temerta", "meseret", "mid"]
# for j,i in enumerate(x, start=1):
#     print(f'{i} is child {j}')
        

# x = [1,58,3,29,36,77,93,4,11]

# counter= 0
# for i in x:
#     if i>50:
#         counter+=1

# print(counter)
    
# class Notebook:
#     def __init__(self):
#         self.notes=[]

#     def add_note(self,note):
#         self.notes.append(note)
        
#     def show_note(self):
#         for j,i in enumerate(self.notes):
#             print(f'{j+1}, {i}')

    

# n=Notebook()
# n.add_note('kaleab')
# n.add_note('helen')
# n.show_note()    

# Coffee Machin with Multi_Resource Tacking    
# class CoffeeMachine:
#     def __init__(self,water,coffee,milk):
#         self.water = water
#         self.coffee = coffee
#         self.milk = milk

#     def make_latte(self):
#         if self.water>=200 and self.coffee>=20 and self.milk >= 150:
#             print(f'Latte made! Remaining - Water: {self.water - 200}ml, Coffee: {self.coffee - 20}g, Milk: {self.milk - 150}ml')
#         else:
#             print('Not enough resources to make a latte')

# c = CoffeeMachine(300,100,200)
# c.make_latte()

#Shared Class Attribute Across Instances
# class Vehicle:
#     color = 'White'
#     def __init__ (self, model, speed):
#         self.model = model
#         self.speed = speed

#     def car(self):
#         return f'{self.model} - color:{self.color}, speed: {self.speed}'
            

# v1 = Vehicle('Tesla', 250)
# v2 = Vehicle('BMW', 200)
# print(v1.car())
# print(v2.car())
# Vehicle.color = 'Red'
# print(v1.car())
# print(v2.car())

# class Vehicle:
#     color = 'White'

#     def __init__(self, model, speed):
#         self.model = model
#         self.speed = speed

# v1 = Vehicle('Tesla', 250)
# v2 = Vehicle('BMW', 200)
# print(f'{v1.model} - Color: {v1.color}, Speed: {v1.speed}')
# print(f'{v2.model} - Color: {v2.color}, Speed: {v2.speed}')
# Vehicle.color = 'Red'
# print(f'{v1.model} - Color: {v1.color}, Speed: {v1.speed}')
# print(f'{v2.model} - Color: {v2.color}, Speed: {v2.speed}')

# class Vehicle:
#     def vehicle_info(self):
#         print('Inside Vehicle class')


# class Car(Vehicle):
#     def car_infro(self):
#         print('Inside Car Class')

# c = Car()
# c.vehicle_info()
# c.car_infro()

#Hierarchical Inheritance
# class Vehicle():
#     def info(self):
#         print('This is a vehicle')

# class Car(Vehicle):
#     def carinfo(self, name):
#         print(f'this car is: {name}')

# class Truck(Vehicle):
#     def truckinfo(self, name):
#         print(f'This truck is: {name}')

# t = Truck()
# t.truckinfo('Scania')
# t.info()

# c = Car()
# c.info()
# c.carinfo('BMW')

#Multilevel Inheritance
# class Vehicle():
#     def info(self):
#         print('This is a vehicle')

# class Car(Vehicle):
#     def carinfo(self, name):
#         print(f'this car is: {name}')

# class Truck(Car):
#     def truckinfo(self, name):
#         print(f'This truck is: {name}')

# t = Truck()
# t.truckinfo('Scania')
# t.info()
# t.carinfo('BMW')

#Hybrid Inheritance
# class Vehicle():
#     def info(self):
#         print('This is a vehicle')

# class Car(Vehicle):
#     def carinfo(self, name):
#         print(f'this car is: {name}')

# class Truck(Vehicle):
#     def truckinfo(self, name):
#         print(f'This truck is: {name}')

# class Ship(Truck):
#     def shipinfo(self, name):
#         print(f'This ship is: {name}')

# s = Ship()
# s.shipinfo('cargo')
# s.info()
# s.truckinfo('cargo')


# super()function
# class Company:
#     def company_name(self):
#         return 'Google'

# class Employee(Company):
#     def info(self):
#         return super().company_name()

# emp = Employee()
# print(f'kaleab works at {emp.info()}')
# print(f'kaleab works at {emp.company_name()}')
# print(issubclass(Employee, Company))

# class Company():
#     def company_name(self):
#         return 'Microsoft'

# class Emplooyee(Company):
#     def company_name(self):
#         return 'Google'

# emp = Emplooyee()
# name = input('What is your name:')
# print(f'{name} works at {emp.company_name()}')
# print(issubclass(Emplooyee, Company))
# print(Emplooyee.mro())

# class Company():
#     def company_name(self):
#         return 'Microsoft'

# class Emplooyee(Company):
#     def company_name(self, name):
#         print(f'{name} works at {super().company_name()}')

# emp = Emplooyee()
# name = input('What is your name:')
# emp.company_name(name)
# print(issubclass(Emplooyee, Company))
# print(Emplooyee.mro())

# class methods, static methods
# class Company:
#     works_at = 'Microsoft'

#     def __init__(self,name,skill):
#         self.name = name
#         self.skill = skill

#     def show(self):
#         print(f'{self.name} works at {Company.works_at} as a {self.skill}')

#     def change_skill(self,nskill):
#         self.skill = nskill

#     @classmethod
#     def changeworkplace(cls, nplace):
#         cls.works_at = nplace

    

# emp = Company('Kaleab', 'beginner programmer')
# emp.show()
# emp.change_skill('senior AI engineer')
# emp.show()
# Company.works_at = 'Googl'
# emp.show()
# Company.changeworkplace('Google')
# emp.show()
# emp.changeworkplace('G') 
# emp.show()

#Using getattr(object, 'instance_variables') method to access instance variables
# class Company:
#     works_at = 'Microsoft'

#     def __init__(self,name,skill):
#         self.name = name
#         self.skill = skill

#     def show(self):
#         print(f'{getattr(emp, 'name')} works at {Company.works_at} as a {getattr(emp, 'skill')}')

#     def change_skill(self,nskill):
#         self.skill = nskill

#     @classmethod
#     def changeworkplace(cls, nplace):
#         cls.works_at = nplace

    

# emp = Company('Kaleab', 'beginner programmer')
# emp.show()
# emp.change_skill('senior AI engineer')
# emp.show()
# Company.works_at = 'Googl'
# emp.show()
# Company.changeworkplace('Google')
# emp.show()
# emp.changeworkplace('G') 
# emp.show()

#Bank Account with Deposit & Overdraw Protection

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance+=amount
#         print(f'{self.balance}')

#     def withdraw(self, amount):
        
#         if amount<= self.balance:
#             self.balance-=amount
#             print(f'{self.balance}')
#         else:
#             print(f'Insufficient balance')


# b = BankAccount(1000)
# b.deposit(500)
# b.withdraw(1500)


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

# class Deposit(BankAccount):

#     def deposit(self, amount):
#         return self.balance+amount

# class Withdraw(Deposit):

#     def withdraw(self, wamount):
#         nb =  super().deposit()- wamount
#         if nb<=0:
#             print(f'Insufficient funds. Current balance: {self.deposit()}')
#         else:
#             print(f'{nb}')


# b = Deposit(1000)
# print(b.deposit(500))
# c = Withdraw(1000)
# c.withdraw(200)

# Bus Subclass Inheriting fromVehicle
# class Vehicle():
#     def __init__(self, name, max_speed):
#         self.name = name
#         self.max_speed = max_speed

#     def display(self):
#         print(f'Vehicle: {self.name}, Max Speed: {self.max_speed}')

# class Bus(Vehicle):
#     pass

# b = Bus('School Bus', 120)
# b.display()
# Override parent Method Using super()
# class Vehicle:
#     def __init__(self, name, capacity):
#         self.capacity = capacity
#         self.name = name

#     def seating_capacity(self, capacity):
#         print(f'{self.name} seating capacity is: {capacity}')

# class Bus(Vehicle):
#     def seating_capacity(self):
#         super().seating_capacity(50)

# b = Bus('School Bus', 120)
# b.seating_capacity()


# Add Maintenance Fee in Child Class via super()
# class Vehicle():
#     def __init__(self, base_fare):
#         self.base_fare = base_fare

  
# class Taxi(Vehicle):
#     def __init__(self, maintenance_fee):
#         super().__init__(maintenance_fee)
#         self.maintenance_fee = maintenance_fee
#         self.maintenance_fee *=0.1

#     def total_fare(self):
#         return self.base_fare + self.maintenance_fee

# t = Taxi(500)
# print(f'Total fare with maintenance fee: {t.total_fare()}')

#polymorphism exercise
# class Ferrari:
#     def ftype(self):
#         print('Petrol')

#     def speed(self):
#         print('Max speed is 350')

# class BMW:
#     def ftype(self):
#         print('Diesel')

#     def speed(self):
#         print('Max Speed is 300')

# def cardetail(c):
#     c.ftype()
#     c.speed()

# ferrari = Ferrari()
# bmw = BMW()

# cardetail(ferrari)
# cardetail(bmw)

# #Polymorphism with Dog & Cat speak()
# class Animal:
#     def speak(self):
#         pass

# class Dog:
#     def speak(self):
#         print('Dog says: Woof')

# class Cat:
#     def speak(self):
#         print('Cat says: Meow!')

# dog = Dog()
# cat = Cat()

# for sound in (dog,cat):
#     sound.speak()

# #Full-Time vs Part_Time Employee Pay Logic
# class Employee:
#     def __init__(self, name, pay,):
#         self.name = name
#         self.pay = pay
        

# class FullTimeEmployee(Employee):
#     def fpay(self):
#         return self.pay/12

# class PartTimeEmployee(Employee):
#     def __init__(self, name, pay,days):
#             self.name = name
#             self.pay = pay
#             self.days = days

#     def ppay(self):
#          return self.pay*self.days

# fte = FullTimeEmployee('Alice', 60000)
# pte = PartTimeEmployee('Bob', 500, 20)
# print(f'Alice"s monthly pay: {fte.fpay()}')
# print(f'Bob"s monthly pay: {pte.ppay()}')       


# #Shape Subclasses with Custom area() Methods
# class Shape:
#     def __init__(self, base, height, radius):
#         self.base = base
#         self.height = height
#         self.radius = radius

#     def area(self):
#         return 0

# class Circle(Shape):
#     def area(self, radius):
#         self.radius = radius
#         super().area()
#         return 3.14159*radius**2

# class Square(Shape):
#     def area(self,base):
#         self.base = base
#         super().area()
#         return base**2

# class Triangle(Shape):
#     def area(self,base,height):
#         self.base = base
#         self.heigh = height
#         super().area()
#         return 0.5*base*height


# c = Circle(0,0,7)
# sa = Square(4,0,0)
# t = Triangle(6,8,0)
# print(c.area(7))
# print(sa.area(4))
# print(t.area(6,8))

# class Media:
#     def __init__(self, title, price, y):
#         self.title = title
#         self.price = price
#         self.y = y

# class Book(Media):
#     def describe(self, author):
#         self.author = author
#         super().__init__()
#         print(f'{self.title} by {author} - {self.price} birr')

# book = Book('Clean Code',499, 'Robert C.Martin')
# book.describe('Robert C.Martin')

# #another method for Shape Subclasse with Custom area() Methods
# class Shape:
#     def __init__(self, base, height, radius):
#         self.base = base
#         self.height = height
#         self.radius = radius

#     def area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self,base,height,radius):
#         super().__init__(base,height,radius)

#     def area(self):
#         return 3.14159*self.radius**2

# class Square(Shape):
#     def __init__(self,base,height,radius):
#         super().__init__(base,height,radius)

#     def area(self):
#         return self.base**2

# class Triangle(Shape):
#     def __init__(self,base,height,radius):
#         super().__init__(base,height,radius)

#     def area(self):
#         return 0.5*self.base*self.height

# c = Circle(0,0,7)
# sa = Square(4,0,0)
# t = Triangle(6,8,0)
# for shape in (c,sa,t):
#     print(shape.area())

# #Media Subclasse with Type_specific attributes
# class Media:
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price

#     def describe(self):
#         print(f'This is a test for media price')

# class Book(Media):
#     def __init__(self,title,price, author):
#         super().__init__(title,price)
#         self.author = author
#     def describe(self):
#         print(f'Book: {self.title} by {self.author} - {self.price} birr')

# class Magazine(Media):
#     def __init__(self,title,price,per):
#         super().__init__(title,price)
#         self.per = per

#     def describe(self):
#         print(f'Magazine: {self.title} ({self.per}) - {self.price} birr')

# class DVD(Media):
#     def __init__(self,title,price,duration):
#         super().__init__(title,price)
#         self.duration = duration

#     def describe(self):
#         print(f'DVD: {self.title}, {self.duration} mins - {self.price} birr')


# book = Book('Clean Code', 499, 'Robert C.Martin')
# mag = Magazine('Wired', 150, 'Monthly')
# dvd = DVD('Inception', 299, 148)

# for med in (book,mag,dvd):
#     med.describe()

# # # Discounted Order Subclass with 10% off
# class Order:
#     def __init__(self, id, og):
#         self.id = id
#         self.og = og

#     def total_amount(self):
#         return self.og
# class DiscountedOrder(Order):
#     def __init__(self,id,og):
#         super().__init__(id,og)
#         self.oog=self.og-(self.og*0.1)

#     def total_amount(self):
#         print(f'Discounted Total: {self.oog}')


# do = DiscountedOrder('ORD001', 1200)
# print(f'Order ID: {do.id}')
# print(f'Original Total: {do.og}')
# do.total_amount()

# #Vehicle Class Hierarchy with Bike, Truck & Bus
# class Vehicle:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
        
#         max_speed = 0

#     def decribe(self):
#         print(f'{type(self).__name__} max speed: {self.max_speed}')

# class Bike(Vehicle):
#     def __init__(self, max_speed):
#         super().__init__(max_speed)
        

#     def describe(self):
#         print(f'{type(self).__name__} max speed: {self.max_speed}')

# class Truck(Vehicle):
#     def __init__(self, max_speed):
#         super().__init__(max_speed)
        

#     def describe(self):
#         print(f'{type(self).__name__} max speed: {self.max_speed}')

# class Bus(Vehicle):
#     def __init__(self, max_speed):
#         super().__init__(max_speed)
        

#     def describe(self):
#         print(f'{type(self).__name__} max speed: {self.max_speed}')

# bi,t,b = Bike(120),Truck(90),Bus(100)
# for speed in bi,t,b:
#     speed.describe()



# #Identify Object's Class Using type()
# class Dog:
#     def __init__(self):
#         pass

# class Cat:
#     def __init__(self):
#         pass

# class Vehicle:
#     def __init__(self):
#         pass

# d,c,v = Dog(), Cat(), Vehicle()
# objects = {'d' : d, 'c' : c, 'v' : v}
# for key, values in objects.items():
#     print(f'{key} is of type: {type(values).__name__}')

# #Type Checking with isinstance() & issubclass()
# class Animal():
#     pass
# class Dog(Animal):
#     pass
# a = Animal()
# d = Dog()
# print(f'Is d an instance of a  {type(d).__name__} ? {isinstance(d, Dog)}')
# print(f'Is d an instance of a  {type(a).__name__} ? {isinstance(d, Animal)}')
# print(f'Is {type(d).__name__} a subclass of {type(a).__name__} ? {issubclass(Dog, Animal)}')


#Vector Addition Using add Overlaoding
class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        t = self.x + other.x
        m = self.y + other.y
        return (t,m)

v1 = Vector(2,3)
v2 = Vector(4,1)

result = v1 + v2
print(f'Vector{result}')     


#Cart Length using len Overloading
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        print(f'Number of items in the cart: {len(self.items)}')


cart = Cart()
cart.add_item('apple')
cart.add_item('banana')
cart.add_item('mango')
cart.__len__()