import random

def play():
    user = input('Enter r for rock, p for paper and s for scissor: \n')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"Computer is {computer}. It's a tie...!!!"
    
    if is_win(user, computer):
        return f"Computer is {computer}. You Won..!!!"
    
    return f"Computer is {computer}. You lost..!!!"

def is_win(user, computer):
    
    if (user == 'p' and computer == 'r') or (user == 'r' and computer == 's') or \
        (user == 's' and computer == 'p'):
        return True
    
    
print(play())