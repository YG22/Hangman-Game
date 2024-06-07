letter = input("Guess a letter: ").lower()

word =  input("Please enter a word: ")
secret = word.replace(word[0:len(word)] , "_ ")
print(secret * len(word))