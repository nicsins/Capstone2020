def getInput():
    words=input('Please Enter a SenTence').lower()
    return words.split()

def printOutput(words):
    for word in words :
        if (word != words[0]):
            print(f'{word.title()}',end='')
        else:
            print(f'{word.lower()}',end='')
# stuff
if __name__ == '__main__':
    words=getInput()
    printOutput(words)
