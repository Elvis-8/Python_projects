import random

answer = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100:"))

        if guess > answer: 
            print('Your guess is too high! Please try again.')
        elif guess < answer:
            print('Your guess is too low! Please try again.')
        else: 
            print('Congratlations, you guessed the right number.')
            break
    except ValueError:
        print("Invalid Input")
        break

