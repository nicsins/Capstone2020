#create game of ro sham bo this is my updated version
__author__="DomiNic"

import random

# list of choices
roshambo=['rock', 'scissors', 'paper']

# get player name
def choose_name():
    return input('What is your name?').title()

# simple choice inout
def make_choice(name):
    return input(f'{name} please choose {roshambo[0]}, {roshambo[1]} or {roshambo[2]}').lower()

# choice validationb loop
def validate_choice(name):
    while True:
        choice=make_choice(name)

        if choice not in roshambo:
           pass
        else:
            break
    return choice,random.choice(roshambo)

def computers_choice(comp_choice):
    return f' The computer chooses {comp_choice}'

# game logic decide the winner
def who_wins(choice,comp_choice):
    if choice == comp_choice:
        return f'we both chose the same thing its a tie!'

    elif (choice == roshambo[0] and comp_choice == roshambo[1]) or (choice == roshambo[1] and comp_choice == roshambo[2]) or (choice == roshambo[2] and comp_choice == roshambo[0]) :
        # return print(f' {choice} beats {comp_choice} You win!')
        return (f' {choice} beats {comp_choice} You win!')

    else:
        # return f'{comp_choice} beats {choice} the computer wins!!'
        return f'{comp_choice} beats {choice} the computer wins!!'

# prints the winner
def print_winner(winner):
    print(winner)

# the game loop
def game_loop(name):

    while True:
        choice,comp_choice=validate_choice(name)

        computers_choice(comp_choice)

        winner=who_wins(choice,comp_choice)

        print_winner(winner)

        again=input('press "y" to play again any other key to stop').lower()

        if again != 'y':
            return False


if __name__ == '__main__':
    # exception handling on simple level
   # try:
       name = choose_name()
       game_loop(name)

   # except Exception as E:
   #     print(E)