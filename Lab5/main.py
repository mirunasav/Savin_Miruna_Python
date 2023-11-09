# 1. class hierarchy for shapes + area, perimeter
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# 2 account classes

class Account:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Not enough money in your account")

    def checkBalance(self):
        print(f"balance: {self.balance}")

    def calculate_interest(self):
        pass


class SavingsAccount (Account):
    def __init__(self, accountNumber, balance=0, interestRate=0.1):
        super().__init__(accountNumber,balance)
        self.interestRate = interestRate

    def calculate_interest(self):
        interest = self.balance * self.interestRate
        self.deposit(interest)
        print(f"Interest of ${interest} credited to account.")


class CheckingAccount(Account):
    def __init__(self, accountNumber, balance=0, limit=100):
        super().__init__(accountNumber, balance)
        self.limit = limit

    def withdraw(self, amount):
        if self.balance + self.limit >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds and limit reached.")


# 3. vehicles + towing capacity, calculate mileage

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self, miles_driven, liters_used):
        pass

    def calculate_towing_capacity(self):
        pass

class Car(Vehicle):
    def calculate_mileage(self, miles_driven, liters_used):
        mileage = miles_driven / liters_used
        return mileage

    def calculate_towing_capacity(self):
        return 0


class Motorcycle(Vehicle):
    def calculate_mileage(self, miles_driven, liters_used):
        mileage = miles_driven / liters_used + 1
        return mileage

    def calculate_towing_capacity(self):
        return 0


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity

    def calculate_mileage(self, miles_driven, liters_used):
        mileage = miles_driven / liters_used - 10
        return mileage


car = Car("Toyota", "Corolla", 2020)
car_mileage = car.calculate_mileage(300, 10)
print(f"Car Mileage: {car_mileage} miles per litre")

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
motorcycle_mileage = motorcycle.calculate_mileage(300, 10)
print(f"Motorcycle Mileage: {motorcycle_mileage} miles per litre")

truck = Truck("Ford", "F-150", 2019, towing_capacity=8000)
towing_capacity = truck.calculate_towing_capacity()
truck_mileage = truck.calculate_mileage(300,10)
print(f"Truck mileage: {truck_mileage} miles per litre")
print(f"Truck Towing Capacity: {towing_capacity} kg")


# 4. employee hierarchy
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team.")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Sales Target: ${self.sales_target}")

    def meet_sales_target(self):
        print(f"{self.name} is working to meet the sales target of ${self.sales_target}.")


manager = Manager("John Doe", "M123", 80000, "Sales")
manager.display_info()
manager.manage_team()

engineer = Engineer("Alice Smith", "E456", 75000, "Python")
engineer.display_info()
engineer.write_code()

salesperson = Salesperson("Bob Johnson", "S789", 70000, 1000000)
salesperson.display_info()
salesperson.meet_sales_target()


# 5.
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def make_sound(self):
        return "Woof (even though not all mammals are dogs)"

    def give_birth(self):
        return f"{self.name} gives birth to puppies and others."


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def make_sound(self):
        return "Peste pod trecea bascula, cip cirip ... etc"

    def lay_eggs(self):
        return f"{self.name} lays eggs."


class Fish(Animal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color

    def make_sound(self):
        return "Help I'm under the water"

    def swim(self):
        return f"{self.name} swims."


lion = Mammal("Lion", "Grasslands", "Yellow")
print(lion.make_sound())
print(lion.give_birth())

sparrow = Bird("Sparrow", "Forests", "Small")
print(sparrow.make_sound())
print(sparrow.lay_eggs())

shark = Fish("Shark", "Oceans", "Blue")
print(shark.make_sound())
print(shark.swim())


# 6. library items
class LibraryItem:
    def __init__(self, title, item_id, available=True):
        self.title = title
        self.item_id = item_id
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Status: {'Available' if self.available else 'Checked Out'}")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, available=True):
        super().__init__(title, item_id, available)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, available=True):
        super().__init__(title, item_id, available)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, available=True):
        super().__init__(title, item_id, available)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


# Example usage
book = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald")
book.display_info()
book.check_out()
book.check_out()
book.display_info()
book.return_item()
book.display_info()

dvd = DVD("Inception", "D001", "Christopher Nolan")
dvd.display_info()
dvd.check_out()
dvd.display_info()

magazine = Magazine("National Geographic", "M001", "March 2023")
magazine.display_info()
magazine.return_item()
magazine.display_info()
