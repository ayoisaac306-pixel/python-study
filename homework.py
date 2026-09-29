import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create the table

cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
account_name TEXT NOT NULL,
account_number INTEGER UNIQUE,
balance REAL NOT NULL DEFAULT 0,
account_type TEXT
)
''')

conn.commit()
conn.close()

#model class

class Account:
    def __init__(self, account_name, account_number, balance, account_type):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __str__(self):
        return f"{self.account_name} | {self.account_number} | {self.balance} | {self.account_type}"






# CRUD FUNCTIONS

# Creating an account(Insert)

def create_account(account_name, account_number, balance, account_type):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('''
INSERT INTO accounts (account_name, account_number, balance, account_type)
VALUES (?, ?, ?, ?)
''', (account_name, account_number, balance, account_type))

    conn.commit()
    conn.close()

def view_accounts():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM accounts')
    rows = cursor.fetchall()

    conn.close()
    return rows

def find_account(account_id):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM accounts WHERE id = ?', (account_id,))
    account = cursor.fetchone()

    conn.close()
    return account

def deposit(account_id, deposit_amount, balance):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

     
    if deposit_amount > 0:
        new_balance = deposit_amount + balance

        cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))

        conn.commit()
        conn.close()
        return new_balance
    else:
        print("Balance cannot be less than 1")

def withdraw(account_id, withdraw_amount, balance):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    
    if withdraw_amount <= balance and withdraw_amount > 0:
        new_balance = balance - withdraw_amount

        cursor.execute('UPDATE accounts SET balance = ? WHERE id = ?', (new_balance, account_id))

        conn.commit()
        conn.close()
        return new_balance
    elif withdraw_amount > balance:
        print("Insufficient fund in account")
    else:
        print("Enter valid number")    


def delete_account(account_id):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM accounts WHERE id = ?', (account_id,))
    conn.commit()
    conn.close()

# console app 
while True:
    print("--- BANK ACCOUNT SYSTEM ---")

    print(" 1. Create Account")
    print(" 2. View Accounts")
    print(" 3. Find Account")
    print(" 4. Deposit Money")
    print(" 5. Withdraw Money")
    print(" 6. Delete Account")
    print(" 7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account_name = input("Account name: ")
        account_number = int(input("Account number: "))
        balance = float(input("Enter initial balance: "))
        account_type = input("Account type: ")

        account = Account(account_name, account_number, balance, account_type)
        create_account(account.account_name, account.account_number, account.balance, account.account_type)
        print("Account created successfully")

    elif choice == "2":
        accounts = view_accounts()
        for a in accounts:
            print(a)    

    elif choice == "3":
        account_id = int(input("Enter account id: "))
        account = find_account(account_id)
        if account is None:
            print("Account not found")
        else:
            print("Account details", account)   

    elif choice == "4":
        account_id = int(input("Enter account id: "))
        account = find_account(account_id)
        if account is None:
            print("Account not found")
        else:
            deposit_amount = float(input("Enter amount you want to deposit: "))
            balance = account[3]
            if deposit_amount > 0:
               new_balance = deposit(account_id, deposit_amount, balance)
               print("New balance", new_balance)
            else:
               print("Deposit amount must be greater than 0") 

    elif choice == "5":
            account_id = int(input("Enter account id: "))  
            account = find_account(account_id)
            if account is None:
                print("Account not found")
            else:
                withdraw_amount = float(input("Enter amount you want to withdraw: "))
                balance = account[3]
                if withdraw_amount <= balance and withdraw_amount > 0:
                        new_balance = withdraw(account_id, withdraw_amount, balance)
                        print("New balance", new_balance)
                else:
                    print("Insufficient fund")

    elif choice == "6":
        account_id = int(input("Enter account id: "))
        account = find_account(account_id)
        if account is None:    
            print("Account not found")
        else:
            delete_account(account_id)

    elif choice == "7":
        print("Goodbye")
        break

    else:
        print("Enter valid option")                            



