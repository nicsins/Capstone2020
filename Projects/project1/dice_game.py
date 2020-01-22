from random import randint as r

class Die():
    roll=r(1,6)



def __getattr__():
    return input('please enter your name')

def player_roll():
    return Die.roll

def computer_roll():
    return Die.roll
def outcome(name,player,computer):
    print(f'{name} you rolled a {player} and the computer rolled a {computer}')
def game_loop(name):

    while True:
        player=player_roll()
        computer=computer_roll()
        outcome(name, player, computer)

        if player > computer:
            print(f'{name} you win')
        elif player<computer:
            print(f'The computer wins :(')
        else :
            print("Tie Game!")

        again=input('would you like to play again? press y to continue any other key to quit').lower()
        if again!='y':
            return False


if __name__ == '__main__':

    game_loop(name=__getattr__())
