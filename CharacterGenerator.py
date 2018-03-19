# Mobin Anandwala
# Date Created: 2/19/2018
# Purpose: Create a character generator based on Rick Riordian's character worksheet found here:  http://rickriordan.com/about/advice-for-writers/
# Birthday year generation based on the following stack overflow: https://stackoverflow.com/questions/4759223/python-select-random-date-in-current-year found from the following google search: creating a random date in python

# libraries needed
import names # generating names for use
from datetime import date # generating birthday
import random # generating random birthday based on age

# Generate first names
def genName(gender):
    if gender == 'male':
        firstname = names.get_first_name(gender)
    elif gender == 'female':
        firstname = names.get_first_name(gender)
    return firstname

# Generate a last name
lastname = names.get_last_name()

# Generate full name using results from genName
def genCharName(firstname,lastname):
    CharName = firstname + ' ' + ' ' + lastname
    return CharName

# Generate birthday based on age
def genBirthday(age):
    age_year = date.today().year - age
    start_date = date.today().replace(day=1,month=1,year=age_year).toordinal()
    end_date = date(day=31, month=12, year=age_year).toordinal()
    birthday_date = date.fromordinal(random.randint(start_date,end_date))
    return birthday_date.strftime('%m-%d-%Y')

# Generate Physical Characteristics (hair color, eye color, height, weight)
def physicalChar():
    hair_color = ['Black', 'Brown', 'Blond', 'Auburn', 'Red'] # using wikipedia hair color article found here: https://en.wikipedia.org/wiki/Human_hair_color
    eye_color = ['Amber', 'Blue', 'Brown', 'Gray', 'Green', 'Hazel'] # using wikipedia eye color article found here: https://en.wikipedia.org/wiki/Eye_color
    height = ['tall', 'average', 'short']
    weight = ['thin', 'average', 'fat']
    char_hair_color = random.choice(hair_color)
    char_eye_color = random.choice(eye_color)
    char_height = random.choice(height)
    char_weight = random.choice(weight)
    char_physical = {'hair':char_hair_color, 'eyes': char_eye_color, 'height':char_height, 'weight':char_weight}
    return char_physical
