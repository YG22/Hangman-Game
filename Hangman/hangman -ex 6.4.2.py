import re

old_letters = ["a", "p", "c", "f"]
i = 0
# letter_guessed = input("Guess a letter: ").lower()

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        if((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) == 1) and not(letter_guessed in old_letters_guessed)):
            old_letters_guessed += [letter_guessed]
            return True
        elif(letter_guessed in old_letters_guessed):
            print("X")
            old_letters_guessed.sort()
            old_letters_guessed = " -> ".join(old_letters_guessed)
            print(old_letters_guessed)
            return False
        elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed[0])) == False) and (len(letter_guessed) == 1)):
            return False
        elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == True) and (len(letter_guessed) > 1)):
            return False
        elif((bool(re.match('^[a-zA-Z0-9]*$', letter_guessed)) == False)):
            return False

while i < 10:
    letter_guessed = input("Guess a letter: ").lower()
    print(try_update_letter_guessed(letter_guessed , old_letters))
    print(old_letters)
    i += 1
