author="Nic"
""" a program that asks for your name and the month you were born in.
Then, your program will print
    A greeting to you, using your name
    A message with the number of letters in your name
    A 'Happy birthday month!' message if you were born in January
"""



from datetime import date
from enum import Enum

# create enum to help deal with figuring out months and interact with the program
class Month (Enum):
    January=1
    February=2
    March=3
    April=4
    May=5
    June=6
    July=7
    August=8
    September=9
    October=10
    November=11
    December=12



#this is a function to help with  data valiodation
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

# next few functions are pretty self explaining
def getNicName():
    return input('What name do you like do by?').capitalize()


def getYear(nicName):

    byear=posPutInt(f'{nicName}, what year where you born?',1900,2020)

    return byear

#  nic way to figure out if it is a leap year
def isLeapYear(byear):
    leapYear=False
    if byear % 4  == 0:
        if byear % 100== 0:
           if byear % 400 == 0:
                return True

    return leapYear

def select_birth_Month(nicName):

    print(f'{nicName} Pleeeeze choose the number of the Month you where born')

    for name, member in Month.__members__.items():
        print(f' for {str(name)} type {str(member.value)} ')

    month=posPutInt('PLEASE ENTER YOUR CHOICE HERE',1,12)

    return month

def getBDay(month,leapYear):
    # validation for number of days in a month
    while True:
        try:
            monthsW30=[Month.September.value,Month.April.value,Month.June.value,Month.November.value]
            day=int(input('What is the day you where born'))

        except ValueError:
            print('Must be a valid date')
            continue
        if day < 0 or day > 31:
            print("Sorry, your response is not valid.")
            continue
        if month==2  and leapYear and day>29:
            print('too many days for that month')
            continue
        elif month==2  and not leapYear and day>28:
            print('too many days for that month and its not leap year!')
            continue


        if (month in monthsW30) and day > 30:
                print('too mant days for that month')
                continue
        else :
            break

    return day
# use datetime to get age
def getAge(byear, bmonth, bday):
    born=[byear, bmonth, bday]
    today=date.today()
    extra_year = 1 if ((today.month, today.day) < (born[1], born[0])) else 0
    age=today.year-born[2]-extra_year

    return  age

# you can see what this is
def printOutput(nicName,bday,bmonth,byear,age):

    print(f'Hey there {nicName} !\n'
          f'you where born on {str(Month(bmonth).name)} {bday} , {byear} \n'
          f'that would make you {age} years old')
    if (bmonth==1):
        print("and By the way Happy Birthday")





if __name__ == '__main__':
    nicName=getNicName()
    byear=getYear(nicName)
    bmonth=select_birth_Month(nicName)
    leapYear=isLeapYear(byear)
    bday=getBDay(bmonth,leapYear)
    age=getAge(bday,bmonth,byear)
    printOutput(nicName,bday,bmonth,byear,age)



