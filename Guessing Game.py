import random

tries = 5

while tries != 0:   # loop runs if the player at least has 1 try remaining
    player_guess = int(input('Guess a number from 0 to 10.'))  #input after loop start to guess a new number each try
    actual_num = random.randint(0, 10)  #random number sets after player guesses a number. New numer each try
    if player_guess == actual_num:
        print('You\'ve guessed', '{}'.format(str(player_guess)) + '.' '\n' 'The number was', '{}'.format(
            str(actual_num)) + '.' '\n' 'EXCELLENT!' '\n')
        tries += 1      # if the player guesses the right number, they get to play longer
    else:
        tries -= 1      #if player player picks the wrong number, they lose a try
        print('You\'ve guessed', '{}'.format(str(player_guess)) + '.' '\n' 'The number was', '{}'.format(
            str(actual_num)) + '.' '\n' 'You have', '{}'.format(tries), 'tries left.' '\n')
        continue  #loops returns to the beginning continuing to run again
    while tries == 0:   #if player guesses wrong too many consecutive times then they are out of tries and the game ends
        print(' You have', '{}'.format(tries), 'tries left.' '\n')
        break  #ends the program
