# -*- coding: utf-8 -*-
"""
.. module:: task
   :platform: idk
   :synopsis: Module for administering computationally intensive and periodic tasks.

.. moduleauthor:: Michael E. Nelson <michael.nelson@fulbrightmail.org>


"""
import os
import re
import string
import pandas as pd
import random
import nltk.tokenize.punkt
from nltk.stem.porter import PorterStemmer
from tcas.config import CONTRACTIONS
from tcas.config import ENGLISH_PICKLE
from tcas.config import GOAL_TOKENS
from tcas.config import GOALS_OUT
from tcas.config import NUMERALS
from tcas.config import MASTER_CSV
from tcas.analysis.helper.goal_provider import goal_provider


def goal_extractor():
    """Tokenize goals from goal provider and write to txt file for training.

    Returns
    -------

    """
    rv = set()
    goals_in, test_goals_out = goal_provider(
        MASTER_CSV,
        GOALS_OUT
    )
    goal_set = set()

    def cleaner(obj):
        """

        Parameters
        ----------
        obj

        Returns
        -------

        """
        obj = re.sub(r'\sassist\spt\s', ' assist patient ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt\swill\s', ' patient will ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt\sknowledge\s', ' patient knowledge ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt\shas\s', ' patient has ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt\'?s?\s', ' patient ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sfor\spt\.\s', ' for patient ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)cg\s', ' caregiver ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sd/c\s', ' discharge ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)msw\s', ' social worker ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)swcm\s', ' social worker ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\smeds(\s|\.)', ' medication ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)hx\s', ' history ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)dx\s', ' diagnosis ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\soutpt\s', ' outpatient ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sappt(\.|s)?\s?', ' appointment ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sadls(\s|\.|$)', ' activities of daily living ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt/\s?cg\s', ' patient/caregiver ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)pt/\s?caregiver\s', ' patient/caregiver ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)goal\d\s', '', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sneuro\s', ' neurology ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sst\.', ' st ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sie\.', ' ie ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sex\:', ' for example ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sbs\s', ' blood sugar ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sca\s', ' cancer ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)mrs\.', ' mrs ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)mr\.', ' mr ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(^|\s)dr\.', ' dr ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'(\s|\/)slp(\s|\.)', ' speech-language pathology ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sspl\s', ' speech-language pathology ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\spcp\s', ' primary care provider ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sva\s', ' veterans affairs ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sss\s', ' social security ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\smri\s', ' magnetic resonance imaging ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sbpsa\s', ' biopsychosocial assessment ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'cargiver', 'Caregiver', obj, flags=re.IGNORECASE)
        obj = re.sub(r'paitent', 'patient', obj, flags=re.IGNORECASE)
        obj = re.sub(r'physiatr', 'psychiatr', obj, flags=re.IGNORECASE)
        obj = re.sub(r'pt\/ot', 'physical/occupational therapy', obj, flags=re.IGNORECASE)
        obj = re.sub(r'pt\.ot', 'physical/occupational therapy', obj, flags=re.IGNORECASE)
        #        obj = re.sub(r'\sPT\s', ' physical therapy ', obj)
        #        obj = re.sub(r'\spt\/', ' physical therapy ', obj)
        #        obj = re.sub(r'^PT(\s|\.)', ' physical therapy ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sfrom\spt\.', ' from physical therapy ', obj, flags=re.IGNORECASE)
        obj = re.sub(r'\sot(\s|\.)', ' occupational therapy ', obj, flags=re.IGNORECASE)

        obj = re.sub(r'(^|\s)goal\s*\#?\w*\d?\:', '', obj, flags=re.IGNORECASE)

        obj = re.sub(r'\d*\/\d*\/\d*', ' a certain date ', obj)

        obj = re.sub(r'000', 'zero', obj)

        obj = re.sub(r'\s?mg\s', ' milligrams ', obj, flags=re.IGNORECASE)

        obj = re.sub(r'\d*', '', obj, flags=re.IGNORECASE)

        obj = obj.replace(' -', ' ')
        obj = obj.replace('- ', ' ')
        obj = obj.replace(' - ', ' ')
        obj = obj.replace(' : ', '')
        #        obj = obj.replace('Goal 1', '')
        #        obj = obj.replace('Goal 2', '')
        #        obj = obj.replace('Goal 3', '')
        #        obj = obj.replace('Goal 1.', '')
        #        obj = obj.replace('Goal 2.', '')
        #        obj = obj.replace('Goal 3.', '')
        obj = obj.replace('1)', '')
        obj = obj.replace('2)', '')
        obj = obj.replace('3)', '')
        obj = obj.replace('4)', '')
        obj = obj.replace('5)', '')
        obj = obj.replace('1.', '')
        obj = obj.replace('2.', '')
        obj = obj.replace('3.', '')
        obj = obj.replace('4.', '')
        obj = obj.replace('1,', '')
        obj = obj.replace('2,', '')
        obj = obj.replace('3,', '')
        obj = obj.replace('4,', '')
        obj = obj.replace('a.', '')
        obj = obj.replace('b.', '')
        obj = obj.replace('c.', '')
        obj = obj.replace('\'', '')
        obj = obj.strip()
        obj = obj.lower()
        #        obj = obj.replace()
        return ' '.join(obj.split())

    def add_to_set(obj):
        """Grow goal set.
    
        Parameters
        ----------
        obj
        
        Returns
        -------
        str
        """
        pattern = re.compile('\d{1,2}-[A-Za-z]{3}')
        if isinstance(obj, float):
            return
        if pattern.match(obj):
            return
        if obj.isnumeric():
            return
        else:
            cleaned_obj = cleaner(obj)
            goal_set.add(cleaned_obj)

    goals_in.apply(lambda x: x.apply(add_to_set))

    goal_set = '\n'.join(goal_set)

    for goal in goal_set.split('\n'):
        rv.add(goal)

    return list(rv)

    # with open(goal_tokens_text_file, 'w') as gttf:
    #     gttf.writelines(goal_set_text)


def tokenizer_trainer():
    """Train sentence tokenizer.
    """

    # def goal_abbrev_types_generator():
    #     """
    #
    #     Returns
    #     -------
    #     set
    #     """
    #     goal_abbrev_types = set()
    #     for alpha in list(string.ascii_lowercase[:6]):
    #         goal_abbrev_types.add(alpha)
    #     for number in range(1, 16):
    #         goal_abbrev_types.add(str(number))
    #         goal_abbrev_types.add(str(number) + '.')
    #     return goal_abbrev_types

    pkl_tokenizer = nltk.data.load(ENGLISH_PICKLE)
    # goal_sent_starters = pkl_tokenizer._params.sent_starters
    # goal_sent_starters = {
    #     'GOAL',
    #     'Goal',
    #     '1',
    #     '2',
    #     '3',
    #     '4',
    #     '1.',
    #     '2.',
    #     '3.',
    #     '4.'
    # }

    # goal_collocations = pkl_tokenizer._params.collocations
    # goal_collocations = {
    #     ('Goal 1. ', 'Improve'),
    #     ('1. ', 'Patient'),
    #     ('2. ', 'Patient'),
    #     ('3. ', 'Patient')
    # }

    # goal_abbrev_types = pkl_tokenizer._params.abbrev_types
    # goal_abbrev_types = {
    #     'apt',
    #     'mr',
    #     'dr',
    #     '1',
    #     '2',
    #     '3',
    #     '4',
    #     '5',
    #     'a',
    #     'b',
    #     'c',
    #     'd',
    #     'e'
    # }
    # goal_ortho_context = pkl_tokenizer._params.ortho_context
    parameters = nltk.tokenize.punkt.PunktParameters()
    # with open(NUMERALS) as n:
    #     parameters = set([numeral.strip() for numeral in n.readlines()])
    # parameters.abbrev_types = goal_abbrev_types
    # parameters.collocations = goal_collocations
    # parameters.ortho_context = goal_ortho_context
    # parameters.sent_starters = goal_sent_starters

    # trainer = nltk.tokenize.punkt.PunktTrainer()  # params=parameters)
    # with open(goal_tokens_text_file) as gttf:
    #     goal_tokens_text_file_contents = gttf.read()
    # trainer.train(goal_tokens_text_file_contents, finalize=False, verbose=True)
    # trainer.finalize_training(verbose=True)

    return nltk.tokenize.punkt.PunktSentenceTokenizer(parameters)


goals = goal_extractor()
# tokenizer = tokenizer_trainer()

pkl_tokenizer = nltk.data.load(ENGLISH_PICKLE)

# def goal_collocations_generator():
#     goal_collocations = set()
# {('S.', 'Bach'), ('S.', 'Bachs')}


# parameters.abbrev_types = goal_abbrev_types_generator()
# parameters.collocations = collocations
# parameters.sent_starters = sent_starters
# tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer(parameters)

tokenized_goals = list()


for g in goals:
    tokens = pkl_tokenizer.tokenize(g)
    for i in tokens:
        tokenized_goals.append(i)

with open(GOAL_TOKENS, 'w') as the_tokenized:
    for each in tokenized_goals:
        for nl in each.split('\n'):
            the_tokenized.write(nl + '\n')
#
#
# print(1)

# trainer.train_tokens(list(goal_set), verbose=True, finalize=False)

# nltk.tokenize.punkt.demo(goal_set_text)

# trainer.finalize_training(verbose=True)
