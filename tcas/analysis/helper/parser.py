#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:07:46 2017

@author: michael
"""






# from parsimonious.grammar import Grammar
#
# goal_enumerators = [
#     'one',
#     'first',
#     'firstly',
#     'two',
#     'second',
#     'secondly',
#     'three',
#     'third',
#     'thirdly',
#     'four',
#     'fourth',
#     'fourthly',
#     'five',
#     'fifth',
#     'six',
#     'sixth',
#     'seven',
#     'seventh',
#     'eight',
#     'eighth',
#     'nine',
#     'ninth'
# ]

#(goal)?(one|first|firstly|two|second|secondly|three|third|thirdly|four|fourth|fourthly|five|fifth|six|sixth|seven|seventh|eight|eighth|nine|ninth)?(\s{,}\#?([n][o]\.?\s)?)?[0-9](\:\s|\s\-\s|\,\s)?[a-z0-9\s]{,}\.
#(goal|\d)?\s*\#*\w*(\s?\-\s?)?(\,\s)?(\.\s\d(\:\-)?)?\:?

# goal_set_articulation = Grammar(
#     """
#     demarcator1             = ~"goal([Nn][Oo]\.)?\d(\s\#)?(\s?\-?\s?)?(\,\s)?"i
#     goal_content            = ~"[a-z0-9\s]*"i
#     last_demarcator         = ~"\."
#     demarcators             = demarcator1? goal_content last_demarcator
#     """
# )

# goal_set =
#
# goal_enumerator =
#
# goal_enumerator_numeric =
#
# qualification = ~"[-][\s]*([A-Z0-9]*[\s]*)*\."
# ix
#
# quotation = "'"
# goal_content
# "'"
#
# parenthetical = "("
# goal_content
# ")" / "-" "goal_content"
