import os

print(os.getcwd())

with open('data.txt', 'w') as file:
    file.write("My name is ayotunde")

with open('data.txt', 'a') as file:
    file.write("\nthis is a next line text\nanother line lol\nanother haha")   

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)     