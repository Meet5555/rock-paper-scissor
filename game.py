from operator import truediv
import random

def game(computer, you):
    if computer == you:
        return None
    elif computer == 'r':
        if you == 'p':
            return True
        else:
            return False
    elif computer == 'p':
        if you == 's':
            return True
        else:
            return False
    elif computer == 's':
        if you == 'r':
            return True
        else:
            return False


user = ''
while user!='q':
    
    randNum = random.randint(1, 3)
    if randNum == 1:
        computer = 'r'
    elif randNum == 2:
        computer = 'p'
    else:
        computer = 's'

    user = input('Your turn! Rock(r), Paper(p) or Secissior(s),q for exit: ')

    print(f"Computer chose {computer}")
    print(f"You chose {user}")

    winner = game(computer, user)
    if winner:
        print("You win!")
    elif winner == None:
        print("Tie!")
    else:
        print("You Lose!")