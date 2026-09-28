try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:    
    print("Enter valid number")



maxInvite = 20
invite_no = ""

invite_no = int(input("Enter invit_no: "))

if invite_no <= 20 and invite_no > 0:
    print("Valid invite number")
else:
    print("Invalid")    