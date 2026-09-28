# class car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def driving(self):
#         print("The vehicle is driving")


# vehicle = car("Toyota", "red")

# print(vehicle.brand)
# print(vehicle.color)
# vehicle.driving()


# class Student:
#     def __init__(self, name, age, course, gpa):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.gpa = gpa

#     def introduce(self):
#         print(f"My name is {self.name}, I am {self.age} years old and I study {self.course}.")

#     def change_course(self, new_course):
#         self.course = new_course    

#     def birthday(self):
#         self.age += 1

#     def show_details(self):
#         print(f"My name is {self.name}, I am {self.age} years old and I study {self.course} with a gpa of {self.gpa}.")

#     def check_gpa(self):
#         if self.gpa >= 4.0:
#             print("Excellent GPA")
#         elif 3.0 <= self.gpa <= 3.99:
#             print("Good GPA")
#         elif self.gpa < 3.0:
#             print("Needs improvement")    
#         else:
#             print("Invalid gpa")      


# class ComputerScienceStudent(Student):
#     def __init__(self, name, age, course, gpa, programming_language):
#         super().__init__(name, age, course, gpa)
#         self.programming_language = programming_language

#     def what_lang(self):
#         print(f"{self.name} programs in {self.programming_language}") 

#     def introduce(self):
#         super().introduce()
#         print(f"My name is {self.name}, I am {self.age} years old and I major in {self.course}and I program in {self.programming_language}.")       
    

# student1 = ComputerScienceStudent("Ayo", 20, "Accounting", 3.03, "null")
# student2 = ComputerScienceStudent("Isaac", 19, "computer science", 2.90, "python")


# student2.introduce()
# student1.show_details()
# student1.check_gpa()
# student2.check_gpa()
# student1.what_lang()
# student2.what_lang()

# class BankAccount:
#     def __init__(self, account_name, balance):
#         self.account_name = account_name
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid amount") 

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Balance cannot be negative")               

# account1 = BankAccount("Ayo", 10000)    



# account1.set_balance(1000000)
# account1.set_balance(-12222)
# print(account1.get_balance())

class Vehicle:
    def move(self):
        print("the vehicles are moving")

class Car(Vehicle):
    def move(self):
        print("Drive")

class Bike(Vehicle):
    def move(self):
        print("ride")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.move()
                
   
        