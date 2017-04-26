# -*- coding: utf-8 -*-
import nltk
from nltk.data import load
from nltk.tokenize.regexp import RegexpTokenizer

from tcas.config import ENGLISH_PICKLE

pattern = r'''(?x)    # allow verbose
([A-Z]\.)+        # provide for abbreviations
| \w+(-\w+)*        # provide for hyphens
| \$?\d+(\.\d+)?%?  # provide for currency and percentages
| \w+[\x90-\xff]  # provide for weird unicode
| [][.,;"'?():-_`]  # etc.
'''

sentencer = load(ENGLISH_PICKLE)
worder = RegexpTokenizer(pattern)

print(
    nltk.wordpunct_tokenize(
        'i am a goal.'))

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  PP -> P NP
  VP -> 'slept' | 'saw' NP | 'walked' PP
  Det -> 'the' | 'a'
  N -> 'Patient' | 'park' | 'dog'
  P -> 'in' | 'with' | 'toward' | 'inside'
""")


# print(grammar)

def part_of_speech_tagger():
    """

    Returns
    -------

    """
    return grammar
