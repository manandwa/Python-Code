# Mobin Anandwala
# Date Created: 4/17/2018
# Purpose: Generate a character using a class instead of separate functions
# Updated on 4/18/2018 with random age generation and random hair color
# Updated on 4/19/2018 with eye color

# Libaries to import
from names import get_first_name, get_last_name
from datetime import date
import random

# Start code
class Character:
    def __init__(self,gender):
        self.gender = gender
        self.charname = ''
        self.charname = self.genName()
        self.birthday = self.genBirthday()
        self.haircolor = self.genHaircolor()
        self.eyecolor = self.genEyecolor()
        # print(self.charname)
        # print('is born on: ' + str(self.birthday))
        # print('is ' + str(self.age) + ' years old')
        # print('Has ' + self.haircolor + ' hair')
        # print('Has ' + self.eyecolor + ' eyes')

    def genName(self):
        if self.gender == 'male':
            self.firstname = get_first_name(self.gender)
        elif self.gender == 'female':
            self.firstname = get_first_name(self.gender)
        self.lastname = get_last_name()
        self.charname = self.firstname + ' ' +  self.lastname
        return self.charname

    def genBirthday(self):
        self.age = random.randint(10,18)
        age_year = date.today().year - self.age
        start_date = date.today().replace(day=1,month=1,year=age_year).toordinal()
        end_date = date(day=31, month=12, year=age_year).toordinal()
        self.birthday_date = date.fromordinal(random.randint(start_date,end_date))
        return self.birthday_date.strftime('%m-%d-%Y')

    def genHaircolor(self):
        hair_color = ['Black', 'Brown', 'Blond', 'Auburn', 'Red'] # using wikipedia hair color article found here: https://en.wikipedia.org/wiki/Human_hair_color
        self.haircolor = random.choice(hair_color)
        return self.haircolor

    def genEyecolor(self):
        eye_color = ['Amber', 'Blue', 'Brown', 'Gray', 'Green', 'Hazel'] # using wikipedia eye color article found here: https://en.wikipedia.org/wiki/Eye_color
        self.eyecolor = random.choice(eye_color)
        return self.eyecolor
