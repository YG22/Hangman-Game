

def check_win(secret_word, old_letters_guessed):
    """The function returns true if all the letters that make up the 
    secret word are included in the list of letters the user 
    guessed. Otherwise, the function returns False.
    :param secret_word: secret_word value
    :param old_letters_guessed : old_letters_guessed value
    :type secret_word: string
    :type old_letters_guessed: list
    :return: The function returns true or false.
    :rtype: boolean
    """
    count = 0
    blank = ['_ '] * len(secret_word)
    for i, c in enumerate(secret_word):
        if(c in old_letters_guessed):
            count += 1
            blank.insert(count - 1, c)
            blank.pop(count)
            if count == len(secret_word):
                ' '.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count - 1, '_')
            blank.pop(count)
            if count == len(secret_word):
                ' '.join(str(e) for e in blank)
    
    count = 0
    for i, c in enumerate(secret_word):
        if c in old_letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False
    
  


secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(check_win(secret_word , old_letters_guessed))