import random

print('-----------------------------')
print('   GUESS THE RANDOM NUMBER')
print('-----------------------------')
print('')


def computer_guess():
    comp_guess = random.randint(0, 100)
    return comp_guess


def computer_guess_updated():
    pass


the_number = random.randint(0, 100)
guess = -1

player_name = input('Enter your name player: ')

while guess and computer_guess != the_number:
    guess_text = input('Guess a number between 0 and 100 :')
    guess = int(guess_text)
    print('My guess is ' + str(computer_guess))

    if guess < the_number:
        print('You guessed wrong, your guess is actually lower then the number I am thinking of')
        if computer_guess < the_number:
            computer_guess = random.randint(int(the_number), 100)
            print('My guess was also lower')
        elif computer_guess > the_number:
            computer_guess = random.randint(0, int(the_number))
            print('My guess was higher')
    elif guess > the_number:
        print('Sorry that is not correct, your guess is higher then the number I am thinking of')
    elif computer_guess == the_number:
        print('I win and you loose!')
    else:
        print('CONGRATS YOU WIN {}{} was what I was thinking of'.format(player_name, guess))
