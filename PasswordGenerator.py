import random
import string
import time
import os


def clear():
    os.system('cls')


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()-_/")
characters2 = list(string.hexdigits)


def questions1():
    global length
    length = 0
    try:
       length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input, please use numbers!")
        time.sleep(0.5)
        questions1()
    if length <= 4:
        clear()
        print("A password can't contain 4 or less characters!")
        time.sleep(0.5)
        questions1()


def hexadecimals():
    random.shuffle(characters2)
    print("Password: ", *characters2, sep='')


def generate_random_password():
    questions1()
        
    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    random.shuffle(password)
    print("Password: ", *password, sep='')


def multiple():
    length2 = 0
    amount = 0 
    try:    
        amount = int(input("How many passwords do you want to generate?: "))
        length2 = int(input("Enter passwords length: "))
    except ValueError:
        print("Invalid input, please use numbers!")
        time.sleep(0.5)
        multiple()
    if (amount < 2) or (length2 <= 4):
        clear()
        print("Brhu u sutpi?d P.S due to bad developing and 0$ budget,\nyou will go to main menu cry abt it")
        time.sleep(1.5)
        operation()
    

    password = []
    for x in range(length2):
        password.append(random.choice(characters))
        
    for i in range(amount):
        random.shuffle(password)
        print(f"Password #{(i + 1)}: ", *password, sep='')


def operation():
    choice = input('''1.Generates a password with the character limit set by user input 
2.Generates X? amounts of passwords based on user input 
3.Generates a password only based on HexaDecimal digits: ''').lower()


    if choice == "1":
        clear()
        generate_random_password()
    elif choice == "2":
        clear()
        multiple()
    elif choice == "3":
        clear()
        hexadecimals()

    else:
        clear()
        print("Invalid option")
        time.sleep(0.5)
        operation()
    print(" ")
    end()


def end():
    time.sleep(0.5)
    play_again = input("Do you want to use the password generator again?: ").lower()

    if (play_again == "y") or (play_again == "yes"):
        clear()
        operation()
    elif (play_again == "n") or (play_again == "no") or (play_again == "c"):
        clear()
        print("SELF DESTRUCTION IN...")
        for x in range(5, 0, -1):
            print(x)
            time.sleep(1)
        print("SELF DESTRUCTION BOOM")
        time.sleep(0.5)
        exit()
    elif play_again == "1":
        clear()
        generate_random_password()
        print(" ")
        end()
    elif play_again == "2":
        clear()
        multiple()
        print(" ")
        end()
    elif play_again == "3":
        clear()
        hexadecimals()
        print(" ")
        end()
    else:
        clear()
        print("Invalid option")
        end()


while True:
    operation()