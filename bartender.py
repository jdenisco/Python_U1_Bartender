#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: bartender
#   date: 2014-09-29
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

# TODO cleanup, Add documention, more error checking

"""
Description:
"""
import random

like = {}
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def ask():
    try:
        print('Please anwser with a y or yes for what you like.')
        print('any key if you don\'t like it ')
        for x in questions.keys():
            respond = raw_input(questions[x])
            if respond.lower() == 'y' or respond.lower() == 'yes':
                like[x] = 'True'
        return like

    except Exception:
        pass


def createdrink(like):
    try:
        if len(like) == 0:
            print('\n\nLooks like someone is not thirty!')

        print('\n\n')
        for y, z in like.items():
            print random.choice(ingredients[y])

        print('\n\n')

    except Exception:
        pass


def __main__():
    for x in questions.keys():
        if random.choice(['True', 'False']) == 'True':
            like[x] = 'True'
    createdrink(like)


if __main__ == '__main__':
    __main__()

ask()
createdrink(like)
