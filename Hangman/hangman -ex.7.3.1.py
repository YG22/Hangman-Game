
def show_hidden_word(secret_word, old_letters_guessed):
    """The function returns a string which consists of letters
    and lower hopes. The string displays the letters from the
    old_letters_guessed list that are in the secret_word string
    in their appropriate position, and the rest of the letters
    in the string (which the player has not yet guessed) as underlines.
    :param secret_word: secret_word value
    :param old_letters_guessed : old_letters_guessed value
    :type secret_word: string
    :type old_letters_guessed: list
    :return: The function returns a string which consists of letters
    and lower hopes.
    :rtype: string
    """
    count = 0
    blank = ['_ '] * len(secret_word)

    for i, c in enumerate(secret_word):
        if c in old_letters_guessed:
            count += 1
            blank.insert(count - 1, c)
            blank.pop(count)
            if count == len(secret_word):
                return ' '.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count - 1, '_')
            blank.pop(count)
            if count == len(secret_word):
                return ''.join(str(e) for e in blank)




secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word , old_letters_guessed))