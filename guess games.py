from random import randint

num = randint(1,100)
guess = eval(input('Enter your guess: '))
if guess==num:
    print('You got it!')
