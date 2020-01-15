author='Nic'
"""Write a 'guess the number' game. The computer should 'think' of a random number within a certain range, and challenge the user to guess the number. Provide feedback and hints for the user; such as "too high" or "too low"""

from random import randint

def posPutInt(prompt,low,hi):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(f"Value must be between {low} and {hi}")
            continue

        if value < (low-1) or value> hi:
            print("Sorry, your response is not valid.")
            continue
        else:
            break
    return value

def get_number():
    return randint(1,99)

def get_guess():
    return posPutInt('please guess a number between 1 and 99',1,99)

# make guesses here usinging nested functions in a loop

def get_clue():
    number=get_number()
    while True:
        guess=get_guess()

        if guess < number:
            print('guess is low')
            continue
        elif guess > number:
            print('guess is high')
            continue
        else:
            print("you guessed it!")

            return False


if __name__ == '__main__':
    get_clue()




