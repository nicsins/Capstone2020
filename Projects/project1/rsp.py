#create game of ro sham bo made in first semester pldc
import random# call random library



#create your main function
def main():
    #call yopur functions
    name, YOU, COMP=get_Info()
    Play(name, YOU, COMP)


def Play(name, YOU, COMP):
    choice=getInput()
    choice2=getChoice2()
    YOU,COMP=getWinner(choice,choice2,name,COMP,YOU)
    getContinue(name, YOU, COMP)

def get_Info():
    name = input("What is Your Name?")
    YOU=0
    COMP=0
    return name,YOU,COMP
#create your input function
def getInput():
    choice = input('Please choose rock paper of scissors:')
    choice=choice.lower()
    return choice
#create a function for computer to randomly generate response
def getChoice2():
    choices=['rock','scissors','paper']
    choice2=(random.choice(choices))
    return choice2
#create a function that choses winner and displays results
def getWinner(choice,choice2,name,COMP,YOU):
    print('Computer chooses',choice2)

    if (choice=='rock' and choice2 =='paper')\
        or(choice=='paper' and choice2=='scissors')\
        or(choice=='scissors'and choice2=='rock'):
        COMP+=1
        print('computer wins ')
    elif (choice=='paper'  and choice2=='rock')\
        or(choice=='scissors'and choice2=='paper')\
        or(choice=='rock'and choice2=='scissors'):
        YOU+=1
        print(name.title(),' wins!!')
    else :
        print( name.title(),' ties with computer')
    print('Computer :',COMP,name,' : ',YOU)
    return YOU,COMP
#ask user if they want to play again
def getContinue(name, YOU, COMP):
      cont=input('do you want to play again?press n for no anything else is yes ')
      cont=cont.lower()
      if cont=='n':
        'break'
      else:
        Play(name, YOU, COMP)
#call your main
main()