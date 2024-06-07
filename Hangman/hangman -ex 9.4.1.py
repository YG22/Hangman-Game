

from collections import Counter
def choose_word(file_path, index):
    """The function accepts as parameters:
    1.A string (file_path) that represents a path to the text file.
    2.An integer (index) that represents the location of a particular word in a file.
    The function returns a tuple consisting of two members in the following order:
    1.The number of different words in the file, that is, does not include repetitive words.
    2.A word in a position obtained as an argument to a function (index), which will 
    be used as the secret word for guessing.
    :param file_path: file_path value
    :param index: index value
    :type file_path: string
    :type index: int
    :return: The function returns a tuple consisting of two members in the following order:
    1.The number of different words in the file, that is, does not include repetitive words.
    2.A word in a position obtained as an argument to a function (index), which will 
    be used as the secret word for guessing.
    :rtype: The function returns a tuple consisting of two members.
    """
    with open (file_path, "r") as my_file:
        file_data_list = my_file.read().split(' ')
    file_data_list = list(map(lambda x: x.lower(), file_data_list))
    list_length = len(file_data_list)
    amount_different_words = len(Counter(file_data_list))
    chosen_word = ""
    while (index > list_length):
        index = index - list_length
    chosen_word = file_data_list[index-1]
    return (amount_different_words , chosen_word)



print(choose_word(r"C:\words.txt", 3))
print(choose_word(r"C:\words.txt",15))
  
