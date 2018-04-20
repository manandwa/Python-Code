# Mobin Anandwala
# Date created: 4/19/2018
# Purpose to save the chracter created from the Character class

from Character import Character
from random import choice

gender = choice(['male','female'])

character = Character(gender)

# write the new character to a test file
with open('test.txt','w') as test:
	test.write(character.charname)
	test.write('\n')
	test.write('is born on: ' + str(character.birthday))
	test.write('\n')
	test.write('is ' + str(character.age) + ' years old')
	test.write('\n')
	test.write('has ' + character.haircolor + ' hair')
	test.write('\n')
	test.write('has ' + character.eyecolor + ' eyes')
	test.close()
