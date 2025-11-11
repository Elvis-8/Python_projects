import random

rock ='r'
paper ='p'
scissors ='s'

mapp = {rock: '🪨', paper: '📃', scissors:'✂️'}
choices = tuple(mapp.keys())

def get_user_choice():
    while True:
        player = input("Rock, paper or scissors? (r/p/s):").lower()
        if player in choices:
            return  player
        else:
            print(f'Invalid choice!\nTry Again')
            continue

def print_choices(computer, player):
    print(f'I chose {mapp[computer]}\nYou chose{mapp[player]}')

def logic(computer, player):
    while True:                 
        if computer == player :
            print("Tie!\nLet's play again")
        elif (computer == rock and player == paper) or (computer == paper and player == scissors) or (computer == scissors and player == rock):
                print('You won')
        else:
                print('You lose')

        contd = input('Continue? (y/n):').lower()
        if contd == 'n':
            print('Thanks for playing!')
        return contd
    
while True:
    player = get_user_choice()
    computer = random.choice(choices)
    print_choices(computer, player)
    contd = logic(computer, player)
    if contd == 'n':
         break
    


