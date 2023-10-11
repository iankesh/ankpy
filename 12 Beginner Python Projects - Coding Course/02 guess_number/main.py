import random

def guess(x):
    n = random.randint(1, x)
    guess = 0
    while (guess != n):
        guess = int(input(f"Guess an integer between 1 and {x}: "))
        if (1 > guess) or (guess > x):
            print(f"Enter a number between 1 and {x}.")
        elif guess < n:
            print("Too low!!")
        elif guess > n:
            print("Too High!!")
    
    print(f"You have found the number.. {n}!!")

# guess(10)

def computer_guess(x):
    n = int(input("Enter a number you want computer to guess: "))
    guess = ''
    while (guess != n):
        guess = random.randint(1, x)
        if (1 > n) or (n > x):
            print(f"Enter a number between 1 and {x}.")
            exit(0)
        elif guess < n:
            print(f"{guess} Too low!!")
        elif guess > n:
            print(f"{guess} Too High!!")
    
    print(f"You have found the number.. {n}!!")

computer_guess(10)