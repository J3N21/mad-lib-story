#!/usr/bin/python3
#
# list_maker.py - Populate noun, verb, adjective lists and write them to CSV files
# Author: <Jailynne Estevez>
# Date: <October 22, 2019>
#

def get_adjectives():
    """
    Get a list of adjectives by prompting the user for the number of items to
    add to the list, then repeatedly collect and append the items to a list which
    is returned from this function.
    :return: A list containing all of the adjectives retrieved.
    """

    user_input_adj = int(input("How many adjectives would you like: "))
    my_list_adj = []
    for i in range(user_input_adj):
        adj = input("What adjective? ")
        my_list_adj.append(adj)
    return my_list_adj

def get_nouns():
    """
    Get a list of nouns by prompting the user for the number of items to
    add to the list, then repeatedly collect and append the items to a list which
    is returned from this function.
    :return: A list containing all of the nouns retrieved.
    """
    user_input_nouns = int(input("How many nouns would you like: "))
    my_list_nouns = []
    for i in range(user_input_nouns):
        noun = input("What noun? ")
        my_list_nouns.append(noun)
    return my_list_nouns

def get_verbs():
    """
    Get a list of verbs by prompting the user for the number of items to
    add to the list, then repeatedly collect and append the items to a list which
    is returned from this function.
    :return: A list containing all of the verbs retrieved.
    """
    user_input_verbs = int(input("How many verbs would you like: "))
    my_list_verbs = []
    for i in range(user_input_verbs):
        verb = input("What verb? ")
        my_list_verbs.append(verb)
    return my_list_verbs

def get_places():
    """
    Get a list of places by prompting the user for the number of items to
    add to the list, then repeatedly collect and append the items to a list which
    is returned from this function.
    :return: A list containing all of the placees retrieved.
    """
    user_input_places = int(input("How many places would you like: "))
    my_list_places = []
    for i in range(user_input_places):
        place = input("What place? ")
        my_list_places.append(place)
    return my_list_places

def get_numbers():
    """
    Get a list of numbers (as words) by prompting the user for the number of items to
    add to the list, then repeatedly collect and append the items to a list which
    is returned from this function.
    :return: A list containing all of the numbers (as words) retrieved.
    """
    user_input_numbers = int(input("How many numbers would you like: "))
    my_list_numbers = []
    for i in range(user_input_numbers):
        number = input("What number? ")
        my_list_numbers.append(number)
    return my_list_numbers

def write_list(file_name, word_list):
    """
    Write a list of words as a single-line CSV to the given file name.
    :param file_name: The file name to write to (e.g. nouns.csv)
    :param word_list: The list containing the words to write to the given file.
    """
    import csv

    my_file = open(file_name, 'w')

    my_file.write(",".join(word_list))

    my_file.close()

################
# MAIN PROGRAM
# calls each get_xxx() function above, and saves the results into a list variable


adjectives = get_adjectives()
write_list("adjectives.csv", adjectives)

nouns = get_nouns()
write_list("nouns.csv", nouns)

verbs = get_verbs()
write_list("verbs.csv", verbs)

places = get_places()
write_list("places.csv", places)

numbers = get_numbers()
write_list("numbers.csv", numbers)

################

