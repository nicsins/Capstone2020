def getInput():
    words=input('Please Enter a SenTence').lower()
    return words.split()

def printOutput(words):
    [ print(word.title(),end='')if word != words[0] else print(word.lower(),end='') for word in words]

# stuff
if __name__ == '__main__':
    words=getInput()
    printOutput(words)
