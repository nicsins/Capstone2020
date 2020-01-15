from enum import Enum
from library import inUtils
class Numth(Enum):
    first=1
    second=2
    third=3
    fourth=4
    fifth=5
    sixth=6
    seven=7
    eight=8
    nine=9
#data validation loop
def posPutInt(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Value must be a whole number")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

# pretty self explaining
def getNumCourses():

    return posPutInt('how many courses are you taking this semester?')

def getCourseName(count):
    count+=1
    return  input(f'What is the name of {Numth(count).name } class you are taking ?')

def getInstructor(course):
    return input(f'who is your instructor for {course } ? ')


def getSchedule(numCourses):
    schedule=[]
    instructors=[]
    for count in range(numCourses):
        course=getCourseName(count)
        schedule.append(course)
        instructor=getInstructor(course)
        instructors.append(instructor)
    return dict(zip(schedule,instructors))

def printSchedule(courseDict):
    print("Here is an overview of the classes you are taking" )
    print(f'{"Course":<60}{"Instructor":>20}')
    print('_'*80)

    for  key in courseDict:
        print(f'{key.title():<50}{courseDict[key].title():>30}')


if __name__ == '__main__':
    numCourses=getNumCourses()
    courseDict=getSchedule(numCourses)
    printSchedule(courseDict)
