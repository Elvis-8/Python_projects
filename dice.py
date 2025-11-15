import random

def dice():
    answer = input(str('Roll the dice? (y/n):')).lower()
    if answer == 'y':
        diec = random.randint(1,6)
        dieb = random.randint(1,6)
        print(f'({diec},{dieb})')
        dice()
    elif answer == 'n':
        print('Thanks for playing!')
        exit()
    else: 
        print('Invalid choice!')
        dice()

dice()
