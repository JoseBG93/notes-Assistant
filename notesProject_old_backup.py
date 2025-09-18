
'''We are going to produce an app that allows us to create, modify, consult and delete our own notes.

STEP 1: REQUIREMENTS. 
The content of these notes is as follows:
    - ID
    - Title
    - Content
    - Date of creation

For we should be able to list and modify our notes, the script must print a menu with the actions we can choose and execute.
So, each list should only display the ID and the title of the note.

STEP 2: NOTES STRUCTURE CREATION.
We will create the structure of the note.

STEP 3: CRUD FUNCTIONS CREATION (Create, Read, Update and Delete)

STEP 4: MENU CREATION
We will create a menu that allows the user to fill his own choose in the console. 

STEP 5: UPLOAD THE PROJECT TO GITHUB
'''

# GOING IN THE APP: USERNAME AND MENU OPTIONS

from datetime import datetime
import time
from matplotlib import colors
import re

def introducing():
    print('\nHello! I\'m your personal notes assistant.\n')
    time.sleep(1)
introducing()

def userName():
    name = input('Please, give your name so I can check if you\'re registered.\n \
    NAME: ')
    time.sleep(1)
    return name
name = userName()

def greeting(name):
    print('\nHi, again, ' + name + '!')

usersDict = {}
surnameDict = {}
birthdayDict = {}
colourDict = {}

def userAccess(name,dict):
    if name not in dict:
        userAnswer = nonRegisteredUser()
        return userAnswer
    else: 
        if tuple(name) in dict:
            greeting(name)
            time.sleep(1)
            menu()
userAnswer = userAccess(name, usersDict)

usersIDCounter = 0
def userNum():
    global usersIDCounter
    usersIDCounter += 1
    return usersIDCounter

def nonRegisteredUser():
    answer = input('You\'re not registered. Would you like to create a personal account?\n \
        YES: Y \n \
        NO: N \n \
        Your choice: ')
    return answer.lower()

def answerYes(usersDict,userIDNumber,name):
        usersDict[userIDNumber] = name
        userSurname, userBirthday, userColour = personalInfo()
        for userIDNumber in usersDict:
            surnameDict[userIDNumber] = userSurname
            birthdayDict[userIDNumber] = userBirthday
            colourDict[userIDNumber] = userColour
        time.sleep(2)
        menu()
if userAnswer == 'y' or userAnswer == 'yes': 
    userIDNum = userNum()
    answerYes(usersDict,userIDNum,name)

def answerNo():
    if userAnswer == 'n' or userAnswer == 'no':
        print('Good. Let me know if you change your mind. See you soon! \n')
answerNo(userAnswer)


def personalInfo(): # This function returns 4 variables: answer, surname, age and favourite colour.
    print('Good. Tell me something about you so I could know you better, please.\n')
    time.sleep(1)
    surname = input('What\'s your surname?\n')
    while surname.isdigit(): # I need to avoid user inputs a string with numbers, even if it's only one.
        print('This is not a valid answer.\n')
        time.sleep(1)
        surname = input('What\'s your surname?\n')
        time.sleep(1)
    birthday = input('When is your birthday?\n') # I want to automatically enter a hyphen between each part of the date.
    time.sleep(1)
    birthdayPattern1 = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    birthdayPattern2 = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    while not birthdayPattern1.match(birthday) and not birthdayPattern2.match(birthday):
        print('This is not a valid answer.\n')
        time.sleep(1)
        birthday = input('When is your birthday?\n')
    coloursList = list(colors.CSS4_COLORS.keys())
    colour = input('What\'s your favourite colour?\n')
    time.sleep(1)
    while colour not in coloursList:
        print('I\'m sorry. I can\'t keep this colour in my database.')
        time.sleep(1)
        colour = input('Choose another one:\n')
        time.sleep(1)
    print ('Thanks a lot for your personal information!\n\n')
    return surname.title(), birthday, colour.lower()

def menu():
    option = input('What would you like to do?\n\n \
    CREATE: press C \n\n \
    UPDATE: press U \n\n \
    READ: press R \n\n \
    DELETE: press D \n\n \
    SHOW ME MY INFO: INFO \n\n \
    EXIT: press E \n\n \
    Your choice: ')
    return option
menuOption = menu



time.sleep(1)


#------------------------------------------------------------------------#

# DATE AND ID FUNCTIONS
def date():
    datetimeObject = datetime.now()
    dateNote = datetimeObject.strftime('%d/%m/%y %H:%M:%S')
    return dateNote

notesIDCounter = 0
def IDNum():
    global notesIDCounter
    notesIDCounter += 1
    return notesIDCounter


# CRUD FUNCTIONS
def create():
    title = input('\nWhat should be the note\'s title?\n')
    content = input('\nWrite anything you want:\n')
    idNumber = IDNum()
    return title, content, idNumber  # Create a titles list

def update():
    option = input('What would you like to modify?\n\n \
    TITLE: press T \n\n \
    CONTENT: press C \n\n \
    EXIT: E')
    modifyAnswOptions = ('t', 'title' 'c', 'content', 'e', 'exit')
    while option not in modifyAnswOptions:
        print('I\'m sorry, this is not a valid answer.')
        time.sleep(1)
        update()
    return option.lower()

def read():
    readNote = input('Which note would you like to read?\n')

    return readNote, date()


def delete():
    option = input('What do you want to delete?\n\n \
    TITLE: press T \
    CONTENT: press C \
    EXIT: press E')
    return option.lower()

def showInfo():
    info = {
    'Name': userName(),
    'ID: ': userNum(),
    'Surname: ': personalInfo([0]),
    'Birthday: ': personalInfo([1]),
    'Colour: ': personalInfo([2])
    }
    for key, value in info.items():
        print(f'{key}: {value}')

def exit():
    print('Good. See you soon!\n')

# DICTIONARIES OF VALUES: USERS, NOTEID AND NOTETITLE
dictOfID = {}
dictOfTitles = {}


# MENU CONDITIONAL STRUCTURE

# 1. Note creation
while userAnswer == 'y' or userAnswer == 'yes':
    if menuOption.lower() == 'c' or menuOption.lower() == 'create': 
        noteTitle, noteContent, noteID = create()
        noteDate = date()
        print(f'Here is the information about your note:\n \
            Title: {noteTitle}\n \
            Content: {noteContent}\n \
            ID number: {noteID}\n \
            Date of creation: {noteDate}')
        time.sleep(2)
        menuOption = menu()

    # 2. Note reading
    elif menuOption.lower() == 'r' or menuOption.lower() == 'read': 
        readingNote, dateNote = read()
        print(f'Note: {readingNote}\nDate: {dateNote}')
        time.sleep(2)
        menuOption = menu()

    # 3. Note update
    elif menuOption.lower() == 'u' or menuOption.lower() == 'update':
        modifiedNote = update()
        if modifiedNote == 't' or modifiedNote == 'title':
            newTitle = input('What should be the new title of your note?\n')
            # Add logic to update the title in the dictionary
        elif modifiedNote == 'c' or modifiedNote == 'content':
            newContent = input('What should be the new content of your note?\n')
            # Add logic to update the content in the dictionary
        elif modifiedNote == 'e' or modifiedNote == 'exit':
            menuOption = menu()
        ######################## Must search the index related to the title that the user wants to replace with a new one.

    # 4. Note delete
    elif menuOption.lower() == 'd' or menuOption.lower() == 'delete': 
        deletedNote = delete()
        if deletedNote == 't' or deletedNote == 'title':
            titleToDelete = input('Which title of the note do you want to delete?\n')
            # Add logic to delete the note by title from the dictionary
        elif deletedNote == 'c' or deletedNote == 'content':
            contentToDelete = input('Which content of the note do you want to delete?\n')
            # Add logic to delete the note by content from the dictionary
        elif deletedNote == 'e' or deletedNote == 'exit':
            menuOption = menu()
        #################### Must search and remove the index related to the title that the user wants to delete.

    # 5. Personal info option
    elif menuOption.lower() == 'info':
        print('Here is your personal information: \n')
        showInfo()
        time.sleep(2)
        menuOption = menu()

    # 6. Exit option
    elif menuOption.lower() == 'e' or menuOption.lower() == 'exit':
        exit()
    else:
        print('This is not a valid option. Please, choose another one.')
        menuOption = menu()
