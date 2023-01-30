#!/usr/bin/python3
#
# mad_libber.py - Generate a Mad Lib story given input CSV files. Story gets
#                 written to a text file.
# Author: <Jailynne Estevez>
# Date: <October 22, 2019>
#

# The master list of "lines" in the mad lib.

import csv
from random import *

mad_lib_lines = [
    "Dear <noun>,",
    "Greetings from <place> College. I am having a(n) <adjective> time so far.",
    "My professors are <adjective> and the food is <adjective>.",
    "I have only missed <number> classes so far, which has made me very <adjective>.",
    "In one class, I am learning to <verb> with <noun>(s), which is totally <adjective>.",
    "The wifi works <number> minutes per day, so I must now <verb>.",
    "I could use more <noun>(s), and would like to take a trip to <place> with my <noun>.",
    "Say '<verb>' to <noun> for me, and I will see you in <number> weeks.",
    "Yours truly,",
    "<noun> <noun>"
]

def read_list(file_name):
    """
    Opens and reads a single line from the given CSV file, splits the line up on commas
    into a nice tidy list, which it then returns to the caller.
    :param file_name: The name of the file to read from (should be a single-line CSV)
    :return: A list containing all of the words split out of the given CSV file.
    """

    my_file = open(file_name, 'r')

    line_from_file = my_file.readline().split(",")

    my_file.close()

    return line_from_file

def substitute_adjectives(adjective_list, mad_lib):
    """
    Substitute out placeholder values by iterating line by line through mad_lib, and replacing
    the placeholder with a randomly chosen word from word_list.  When done, return the updated
    mad lib.
    :param word_list: The list of adjectives to choose random words from.
    :param mad_lib: The master mad lib to iterate through and in which to replace placeholders for adjective.
    :return: An updated master mad lib list.
    """

    for i in range(0, len(mad_lib)):
        line_number = randint(0, len(adjective_list)-1)
        adjective = adjective_list[line_number]
        mad_lib[i] = mad_lib[i].replace("<adjective>", adjective, 1)
        if "<adjective>" in mad_lib[i]:
            ran_num = randint(0, len(adjective_list)-1)
            adjective = adjective_list[ran_num]
            mad_lib[i] = mad_lib[i].replace("<adjective>", adjective)


    return mad_lib

def substitute_nouns(noun_list, mad_lib):
    """
    Substitute out placeholder values by iterating line by line through mad_lib, and replacing
    the placeholder with a randomly chosen word from word_list.  When done, return the updated
    mad lib.
    :param word_list: The list of adjectives to choose random words from.
    :param mad_lib: The master mad lib to iterate through and in which to replace placeholders for adjective.
    :return: An updated master mad lib list.
    """

    for i in range(0, len(mad_lib)):
        line_number = randint(0, len(noun_list)-1)
        noun = noun_list[line_number]
        mad_lib[i] = mad_lib[i].replace("<noun>", noun, 1)
        if "<noun>" in mad_lib[i]:
            ran_num = randint(0, len(noun_list)-1)
            noun = noun_list[ran_num]
            mad_lib[i] = mad_lib[i].replace("<noun>", noun)

    return mad_lib

def substitute_verbs(verb_list, mad_lib):
    """
    Substitute out placeholder values by iterating line by line through mad_lib, and replacing
    the placeholder with a randomly chosen word from word_list.  When done, return the updated
    mad lib.
    :param word_list: The list of verbs to choose random words from.
    :param mad_lib: The master mad lib to iterate through and in which to replace placeholders for verb.
    :return: An updated master mad lib list.
    """

    for i in range(0, len(mad_lib)):
        line_number = randint(0, len(verb_list)-1)
        verb = verb_list[line_number]
        mad_lib[i] = mad_lib[i].replace("<verb>", verb)

    return mad_lib

def substitute_places(place_list, mad_lib):
    """
    Substitute out placeholder values by iterating line by line through mad_lib, and replacing
    the placeholder with a randomly chosen word from word_list.  When done, return the updated
    mad lib.
    :param word_list: The list of places to choose random words from.
    :param mad_lib: The master mad lib to iterate through and in which to replace placeholders for placee.
    :return: An updated master mad lib list.
    """

    for i in range(0, len(mad_lib)):
        line_number = randint(0, len(place_list)-1)
        place = place_list[line_number]
        mad_lib[i] = mad_lib[i].replace("place", place)

    return mad_lib

def substitute_numbers(number_list, mad_lib):
    """
    Substitute out placeholder values by iterating line by line through mad_lib, and replacing
    the placeholder with a randomly chosen word from word_list.  When done, return the updated
    mad lib.
    :param word_list: The list of numbers (as words) to choose random words from.
    :param mad_lib: The master mad lib to iterate through and in which to replace placeholders for number.
    :return: An updated master mad lib list.
    """

    for i in range(0, len(mad_lib)):
        line_number = randint(0, len(number_list)-1)
        number = number_list[line_number]
        mad_lib[i] = mad_lib[i].replace("number", number)

    return mad_lib

def write_mad_lib(mad_lib_file, mad_lib):
    """
    Write the updated mad lib to file_name as a text file, line by line.
    :param file_name: The file name to write to (e.g. madlib.txt)
    :param mad_lib: The list containing the updated mad lib.
    """

    mad_lib_file = open('mad_lib.txt', 'w')

    mad_lib_file.write(" ".join(mad_lib_lines))

    mad_lib_file.close()

################
# MAIN PROGRAM
# Calls read_list for each list type, and saves the output into appropriate list variables
# Next calls the various substitute_xxx functions to choose our random words and updates mad_lib_list
# Lastly calls write_mad_lib to write the generated mad lib to a text file

adjective_list = read_list("adjectives.csv")
mad_lib_lines = substitute_adjectives(adjective_list, mad_lib_lines)

noun_list = read_list("nouns.csv")
mad_lib_lines = substitute_nouns(noun_list, mad_lib_lines)

verb_list = read_list("verbs.csv")
mad_lib_lines = substitute_verbs(verb_list, mad_lib_lines)

place_list = read_list("places.csv")
mad_lib_lines = substitute_places(place_list, mad_lib_lines)

number_list = read_list("numbers.csv")
mad_lib_lines = substitute_numbers(number_list, mad_lib_lines)

write_mad_lib('mad_lib.txt', adjective_list)
write_mad_lib('mad_lib.txt', noun_list)
write_mad_lib('mad_lib.txt', verb_list)
write_mad_lib('mad_lib.txt', place_list)
write_mad_lib('mad_lib.txt', number_list)

################


