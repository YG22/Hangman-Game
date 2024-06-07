
def print_hangman(num_of_tries):
    """The function prints one of the seven modes of the hanging man, using
    A variable called num_of_tries that represents the number 
    of failed user attempts so far And the variable HANGMAN_PHOTOS you set.
    :param num_of_tries: num_of_tries value
    :type num_of_tries: int
    :return: The function prints one of the seven modes of the hanging man.
    :rtype: value from dict
    """  
    HANGMAN_PHOTOS ={
1: """
x-------x
""",
2: """
x-------x
|
|
|
|
|
""",
3: """
x-------x
|       |
|       0
|
|
|
""",
4: """
x-------x
|       |
|       0
|       |
|
|
""",
5: """
x-------x
|       |
|       0
|      /|\\
|
|    
""",
6: """
x-------x
|       |
|       0
|      /|\\
|      /
|    
""",
7: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
}
    if(num_of_tries == 0):
        return HANGMAN_PHOTOS[1]
    elif(num_of_tries == 1):
        return HANGMAN_PHOTOS[2]
    elif(num_of_tries == 2):
        return HANGMAN_PHOTOS[3]
    elif(num_of_tries == 3):
        return HANGMAN_PHOTOS[4]
    elif(num_of_tries == 4):
        return HANGMAN_PHOTOS[5]
    elif(num_of_tries == 5):
        return HANGMAN_PHOTOS[6]
    elif(num_of_tries == 6):
        return HANGMAN_PHOTOS[7]



num_of_tries = 6
print(print_hangman(num_of_tries))