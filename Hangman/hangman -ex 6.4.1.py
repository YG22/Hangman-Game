import re

old_letters = []
letter_guessed = input("Guess a letter: ").lower()
def check_valid_input(letter_guessed , old_letters_guessed):
    if((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) == 1) and not(letter_guessed in old_letters_guessed)):
        old_letters_guessed += [letter_guessed]
        return True
    elif(letter_guessed in old_letters_guessed):
        return False
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed[0])) == False) and (len(letter_guessed) == 1)):
        return False
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) > 1)):
        return False
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == False)):
        return False

print(check_valid_input(letter_guessed ,old_letters))
