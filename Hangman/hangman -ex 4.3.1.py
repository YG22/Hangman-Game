import re

letter = input("Guess a letter: ").lower()
if((bool(re.match('^[a-zA-Z0-9]*$', letter)) == True) and (len(letter) == 1)):
    print(letter)
elif((bool(re.match('^[a-zA-Z0-9]*$', letter[0])) == False) and (len(letter) == 1)):
    print("E2")
elif((bool(re.match('^[a-zA-Z0-9]*$', letter)) == True) and (len(letter) > 1)):
    print("E1")
elif((bool(re.match('^[a-zA-Z0-9]*$', letter)) == False)):
    print("E3")

