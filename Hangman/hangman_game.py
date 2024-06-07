import re
from collections import Counter
from sty import fg


def opening_screen():
    """The function displays the opening screen and the number of attempts.
    """
    HANGMAN_ASCII_ART = """
     __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.      _______      ___      .___  ___.  _______
    |  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |     /  _____|    /   \     |   \/   | |   ____|
    |  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__
    |   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
    |  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____
    |__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|     \______| /__/     \__\ |__|  |__| |_______|\n

"""
    MAX_TRIES = "Several attempts: 6\n"
    print('\033[94m', HANGMAN_ASCII_ART, MAX_TRIES)
    print('\033[0;37;40m ')


def print_pictures_hangman(num_of_tries):
    """The function prints one of the seven modes of the hanging man, using
    A variable called num_of_tries that represents the number
    of failed user attempts so far And the variable HANGMAN_PHOTOS you set.
    :param num_of_tries: num_of_tries value
    :type num_of_tries: int
    :return: The function prints one of the seven modes of the hanging man.
    :rtype: value from dict
    """
    HANGMAN_PHOTOS = {
        1: '\033[92m' + """
        x-------x
        """,
        2: fg(255, 255, 153) + """
        x-------x
        |
        |
        |
        |
        |
        """,
        3: '\033[93m' + """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        4: fg(255, 178, 102) + """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        5: fg(255, 128, 0) + """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        6: '\033[91m' + """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
        7: fg(255, 10, 10) + """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    }
    hangman_status = HANGMAN_PHOTOS[num_of_tries]
    return hangman_status + "\033[0;37;40m "


def choose_word(file_path, index):
    """The function accepts as parameters:
    1.A string (file_path) that represents a path to the text file.
    2.An integer (index) that represents the location of a
    particular word in a file.
    The function returns a tuple consisting of two members in
    the following order:
    1.The number of different words in the file, that is, does not
    include repetitive words.
    2.A word in a position obtained as an argument to a function
    (index), which will
    be used as the secret word for guessing.
    :param file_path: file_path value
    :param index: index value
    :type file_path: string
    :type index: int
    :return: The function returns a tuple consisting of two members
    in the following order:
    1.The number of different words in the file, that is, does not
    include repetitive words.
    2.A word in a position obtained as an argument to a function
    (index), which will
    be used as the secret word for guessing.
    :rtype: The function returns a tuple consisting of two members.
    """
    with open(file_path, "r") as my_file:
        file_data_list = my_file.read().split(' ')
    file_data_list = list(map(lambda x: x.lower(), file_data_list))
    list_length = len(file_data_list)
    amount_different_words = len(Counter(file_data_list))
    chosen_word = ""
    while (index > list_length):
        index = index - list_length
    chosen_word = file_data_list[index-1]
    return chosen_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check the correctness of the input and whether it is legal
    to guess this signal.
    The function receives a character and a list of letters that
    the user has previously
    guessed. The function checks if the input is only 1 character long
    and whether the user has not guessed this signal before.
    :param letter_guessed: The string represents the character
    received from the user.
    :type letter_guessed: str
    :param old_letters_guessed: The list contains the letters the
    player has guessed so far.
    :type old_letters_guessed: list
    :return: return True if it is a legal input, else return False
    :rtype: bool
    """
    if(not letter_guessed.isalpha() or len(letter_guessed) > 1):
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


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
    blank = ['\033[96m' + '_ '] * len(secret_word)

    for i, c in enumerate(secret_word):
        if c in old_letters_guessed:
            count += 1
            blank.insert(count - 1, '\033[94m' + c + '\033[0m')
            blank.pop(count)
            if count == len(secret_word):
                return ' '.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count - 1, '\033[96m' + '_')
            blank.pop(count)
            if count == len(secret_word):
                return ' '.join(str(e) for e in blank) + '\033[0m'


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function update old_letters_guessed list.
    This function uses the function check_valid_input() to know if
    the character is incorrect and not previously guessed or the
    character is invalid and / or already in the guess list.
    If it false print "X" to the user and also print a sorted
    string made from
    old_letters_guessed character.
    :param letter_guessed: The string represents the character
    received from the user.
    :type letter_guessed: str
    :param old_letters_guessed: The list contains the letters the
    player has guessed so far.
    :type old_letters_guessed: list
    :return: returns False if it already exist or if check_valid_input is
    False, else returns True.
    :rtype: bool
    """
    if(not check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = "\033[95m -> \033[0m".join(old_letters_guessed)
        print(fg(255, 10, 10) + "X" + '\033[0m')
        print("\033[0;37;40m", old_letters_guessed, "\n")
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


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
    for letter in secret_word:
        if letter in old_letters_guessed:
            count = count + 1
    if count == len(secret_word):
        return True
    else:
        return False


def main():
    """This is a standart game of hangman.
    The function print a welcome screen, and than ask the
    player to enter (1) a word file path and (2) a location (index)
    for a word in the file.
    According to the player's input, the secret word for
    the game will be selected.
    Ask the player to enter one character input per round.
    After every good guess, introduce the secret word to the
    player in a lower-line structure. In case of a failed guess.
    Print the player the output ":(" and below it print a picture
    of the man hanging in the "advanced" mode.
    End of game:
    If the player guessed the whole word correctly - Printed on the
    screen his name and that he won the game.
    If the player guessed seven failed attempts - Printed on the
    screen his name and that he lost the game.
    """
    MAX_TRIES = 7
    num_of_tries = 1
    old_letters_guessed = []
    FIRST_NAME = input("Enter your first name: ").capitalize()
    print(FIRST_NAME, ",Welcome to the HANGMAN game")
    opening_screen()
    file_path = input("Enter a path to a word file: ")
    index = int(input("Enter index: "))
    print(print_pictures_hangman(num_of_tries))
    secret_word = choose_word(file_path, index)
    print(show_hidden_word(secret_word, old_letters_guessed), "\n")
    while(num_of_tries < 7):
        letter_guessed = input("Guess a letter: ").lower()
        check_valid_letter = check_valid_input(letter_guessed, old_letters_guessed)
        if(check_valid_letter and letter_guessed in secret_word):
            old_letters_guessed += [letter_guessed]
        elif(check_valid_letter and letter_guessed not in secret_word):
            old_letters_guessed += [letter_guessed]
            print('\033[93m', ":(" + '\033[0m')
            num_of_tries += 1
            print(print_pictures_hangman(num_of_tries))
        elif(not check_valid_letter):
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed), "\n")
        win_or_lose = check_win(secret_word, old_letters_guessed)
        if(win_or_lose and num_of_tries < 7):
            print('\033[92m', FIRST_NAME, "WON the game")
            break
        elif(not win_or_lose and num_of_tries == 7):
            print(fg(255, 10, 10) + FIRST_NAME, "LOST the game")
            break
        else:
            pass

if __name__ == "__main__":
    main()