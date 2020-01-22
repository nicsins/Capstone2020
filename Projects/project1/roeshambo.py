import random

def main():
    name=choose_name()
    game_loop(name)



roshambo=['rock', 'scissors', 'paper']


def choose_name():
    return input('what is your name?')


def make_choice(name):
    return input(f'{name} please choose {roshambo[0]}, {roshambo[1]} or {roshambo[2]}').lower()

def validate_choice(name):
    while True:
        choice=make_choice(name)

        if choice not in roshambo:
           pass
        else:
            break
    return choice

def computers_choice(choices):

    return print(f' The computer chooses {str(random.choices(choices))}')

def who_wins(choice,comp_choice):
    if choice == comp_choice:
        return print(f'we both chose the same thing its a tie!')
    elif (choice == roshambo[0] and comp_choice == roshambo[1]) or (choice == roshambo[1] and comp_choice == roshambo[2]) or (choice == roshambo[2] and comp_choice == roshambo[0]) :
        return print(f' {choice} beats {comp_choice} You win!')
    else:
        return print(f'{comp_choice} beats {choice} the computer wins!!')

def print_winner(winner):
    print(winner)

def game_loop(name):
    while True:
        choice=validate_choice(name)
        comp_choice=computers_choice(roshambo)
        winner=who_wins(choice,comp_choice)
        print_winner(winner)
        again=input('press "y" to play again any other key to stop').lower()
        if again != 'y':
            return False
        else:
            continue






if __name__ == '__main__':
    main()