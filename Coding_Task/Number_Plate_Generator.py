import random
from datetime import * 
import string
from symbol import parameters

#ASSUMPTION: Cars with the year XX50 or greater cannot be registered

INVALID_LETTERS = ['I', 'Q']

VALID_RESPONSE = ['y', 'n']

def gen_plate (memory_tag, month, year):
    """
    Generates a new number plate for a vehichle and stores it the file 'License_Plates.txt'

    Parameters
    -----------
    memory_tag: string
        a string made from two letters chosen by a user
    
    month: string
        denotes which month the car was registered 
    
    year: string
        denotes which year the car was registered.
        Note: 'year' is a string for string manipulation purposes.
    
    Examples
    ---------
    >>> gen_plate([], 'PJ', 10, '2025')
    [PJ75 ABC]
    >>> gen_plate([PJ75 ABC], 'YC', 7, '2019')
    [PJ75 ABC, YC19 DEF]
    >>> gen_plate([], 'LT', 1, '2003')
    [LT52 GHJ]

    Notes
    -----
    Each number plate must be unique\n
    The last three letters are randomly generated and cannot include I or Q\n
    Three examples taken from question sheet already in file

    """
    file = open("License_Plates.txt", "r")

    age_identifier = get_age_identifier(month, year)

    # the random letters are generated and checked to see if they contain any illegal letters (I/Q)
    ran_letters = ''.join(random.choice(string.ascii_uppercase) for i in range (3))
    while 'I' in ran_letters or 'Q' in ran_letters:
        ran_letters = ''.join(random.choice(string.ascii_uppercase) for i in range (3))

    # all pieces information to make the number plate are now valid so all the compnents are concatinated in the correct order
    plate_number = memory_tag.upper() + age_identifier + ' ' + ran_letters

    # check to see if number plate already exists and if it does random numbers are re-generated and re-concatinated until the plate number is unique
    while (plate_number+'\n') in file:
        ran_letters = ''.join(random.choice(string.ascii_uppercase) for i in range (3))
        while 'I' in ran_letters or 'Q' in ran_letters:
            ran_letters = ''.join(random.choice(string.ascii_uppercase) for i in range (3))
        plate_number =  memory_tag.upper() + age_identifier + ' ' + ran_letters

    # unique number plate is added to the file
    file.close()
    file = open("License_Plates.txt", "a")
    file.write(plate_number + '\n')
    file.close()
    
def get_age_identifier(month, year):
    """
    Checks what month the car was registered and carries out the correct calculation to give the correct age identifier

    Parameters
    -----------
    month: string
        denotes which month the car was registered 
    
    year: string
        denotes which year the car was registered.
        Note: 'year' is a string for string manipulation purposes.
    
    Returns
    -------
    age_identifier: str
        a 2 character long string of digits that is usedto tell what year and what time of year the car was registered
    
    Examples
    ---------
    >>> get_age_identifier('02', 2019)
    58
    """
    if int(month)<3:
        age_identifier = str((int(year[2:4])-1) + 50)
    elif int(month)>8:
        age_identifier = str(int(year[2:4]) + 50)
    else:
        age_identifier = str(int(year[2:4]))
    return age_identifier



# check to see if user wants to enter any number plates at all
new_plate = input('Enter information for a new number plate?[y/n]')
while new_plate not in VALID_RESPONSE:
    new_plate = input('Invalid response. Enter information for a new number plate?[y/n]')


while new_plate == 'y':
    # mt_valid becomes true if the memory tag (MT) is valid - valid memory tags are two letters long
    # date_valid becomes true if the user eneters a plausible date
    mt_valid = False
    date_valid = False

    while mt_valid == False:
        memory_tag = input("Enter a memory tag:  ")
        # .isalpha checks to see if the string contains only letters and returns true if they are and false otherwise
        # if statement also checks to see if MT is the correct lenth
        if memory_tag.isalpha() == True and len(memory_tag) == 2:
            mt_valid = True
        else:
            print("The memory tag you entered is inavlid. Memory tags should on consist of 2 characters and and only letters, no symbols or numbers. Please try again.")

    while date_valid == False:
        date = input("Enter the date the car was registered(Format DD/MM/YYYY):   ")
        #attempt to split the date entered by the user using '/' as the delimiter  
        try:
            day, month, year = date.split('/')
        except ValueError:
            #system throws ValueError if the string cannot be split so it is handled like this so the user knows the inputed data is invalid
            print("The date you entered is invalid. The date should be in the format of DD/MM/YYYY(eg 01/01/2001 for the 1st of january 2001). Please use '/' as a seperator and try again.")
        else:
            try:
                #use of the datetime library ensures that the date entered is plausible
                full_date = datetime(int(year), int(month), int(day))
                date_valid = True
            except ValueError:
                #system throws ValueError if invalid values are passed into the datetime function so it is handled like this so the user knows the inputed data is invalid
                print("The date you entered is invalid. The date should be in the format of DD/MM/YYYY(eg 01/01/2001 for the 1st of january 2001).\n Please ensure that you are only using digits for your dates and try again.")
    
    # generate a plate with the given information
    if int(year[2:4])>=50:
        print("Unfortunately this date cannot be registered. Please enter a year that falls before the 50th year in a century(eg 01/01/2049)")
    else:
        gen_plate(memory_tag, month, year)
        print('Number plate registered successfully!')

    new_plate = input('Enter information for a new number plate?[y/n]')
    while new_plate not in VALID_RESPONSE:
        new_plate = input('Invalid response. Enter information for a new number plate?[y/n]')