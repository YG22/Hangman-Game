import re

letter_guessed = input("Guess a letter: ").lower()
def is_valid_input(letter_guessed):
    if((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) == 1)):
        return True
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed[0])) == False) and (len(letter_guessed) == 1)):
        return False
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) > 1)):
        return False
    elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == False)):
        return False

print(is_valid_input(letter_guessed))