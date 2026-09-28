# for i in range(5):
#     print(i)


# name = ["ayo", "isaac", "ponche"]  

# for n in name:
#     print(n)


# numbers = [2, 4, 6, 8, 10]    

# for number in numbers:
#     print(number * number)


# age = int(input("Enter your age: "))

# while age <= 5:
#     print(age)
#     age += 1




# while True:
#     number = int(input("Guess the number: "))
#     if number == 7:
#         print("you won")
#         break
#     else:
#         print("Wrong try again")    


# number = int(input("Enter a number: "))

# count = 1
# while count <= number:
#     print(count * count)
#     count += 1


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult")
# elif age >= 13 and age <= 17:
#     print("You are a teenager")
# else:
#     print("you are a child")        

# number = int(input("Enter a number"))

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negativee")
# else:
#     print("0")        

# numbers = [10, -5, 0, 7, -2, 15]

# for number in numbers:
#      if number > 0:
#       print(f"{number} is positive")
#      elif number < 0:
#       print(f"{number} is negativee")
#      else:
#       print(f"{number} is 0")  

balance = 10000


while True:
    print("1. Check balance\n2. Withdraw \n3. Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        print(f"Your balance is #{balance}")
    elif option == 2: 
        withdraw = int(input("How much do you want to withdraw: "))
        if withdraw <= balance:
            balance = balance - withdraw
            print(f"WIthdrawal succesful your new balance is {balance}")
        else:
            print("Insufficient funds")
    elif option == 3:
        print("Thanks for banking with us")
        break
    else:
        print("Enter valid option")                
      

    


