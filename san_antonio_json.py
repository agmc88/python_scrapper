#!/usr/bin/python3
# -*- coding: utf8 -*-

# Imports
from random import *
import json

# Functions
def get_random_item(arg):
    index = randint(0, len(arg)-1)
    return arg[index]

def read_values_from_json(file, tag):
    values = []
    #with open("characters.json") as f:
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[tag])
        return values

def random_character():
    all_values = read_values_from_json("s_characters.json", "character")
    return get_random_item(all_values)

def random_quote():
    all_values = read_values_from_json("quotes.json", "quote")
    return get_random_item(all_values)

def message(character, quote):
    return "{} says : {}".format(character, quote)

#Variables
user_answer = input("Veuillez appuyer sur \"B\" pour quitter le programme ou sur une autre touche pour voir une nouvelle citation : ")
# Main program
while user_answer.capitalize() != "B":
    print(message(random_character(), random_quote()))
    user_answer = input("Veuillez appuyer sur \"B\" pour quitter le programme ou sur une autre touche pour voir une nouvelle citation : ")
