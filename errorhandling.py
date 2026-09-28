# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Enter a valid age")
# else:
#     print(f"you are {age} years old")
# finally:
#     print("End")            


# Make a small program that asks for two numbers and divides the first by the second.

# Handle the situation where the user enters 0 as the second number.

# Hint: the error you'll want to catch is:    



try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    answer = a / b
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(f"{a}/{b}= {answer}")
finally:
    print("End of program")            