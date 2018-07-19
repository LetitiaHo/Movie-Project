#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:57:57 2018

@author: letitiaho
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:42:52 2018

@author: letitiaho
"""

import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk



""" Importing the capsuled script as a list """

def import_script(filename):
    """ Open the script and create a list with each word as an item """
    file = open(str(filename), 'r',  encoding = 'utf8')

    # Set each line into an item in a list
    content = file.readlines()
    content_split = []
    for line in content:
        line_split = line.split()
        content_split.append(line_split)
    file.close()   
    
    # Split each list of words into a list per word
    content_split_again = []
    for word_list in content_split:
        if len(word_list) >= 2:
            for i in range(len(word_list)):
                word = [word_list[i]]
                content_split_again.append(word)
        elif len(word_list) == 1:
            content_split_again.append(word_list)
        elif len(word_list) == 0:
            content_split_again.append(['-'])

#    print(content_split_again)    
    return content_split_again



""" Tag POS of each word """

def get_pos(text):
    """ Get the part of speech of each word in the text, from treebank """
    pos_list = []
    for word in text:
        word_list = nltk.pos_tag(word)
        word_list[0] = list(word_list[0])
        word_list[0][1] = get_wordnet_pos(word_list[0][1])
        word_list[0] = tuple(word_list[0])
        pos_list.append(word_list)
    return pos_list

def get_wordnet_pos(tag):    
    if tag.startswith('NN'):
        return wordnet.NOUN
    elif tag.startswith('VB'):
        return wordnet.VERB
    elif tag.startswith('JJ'):
        return wordnet.ADJ
    elif tag.startswith('RB'):
        return wordnet.ADV



""" Disambiguating with LESK using POS """

#def get_wordnet_meaning(text_pos, text):
#    meanings = []
#    for tup in text_pos:
#        word = tup[0]
#        wordnet_pos = get_wordnet_pos(tup[1])
#        if wordnet_pos != None:
#            entry = []
#            entry.append(word)
#            syn = lesk(text, word, pos=wordnet_pos)
#            entry.append(syn)
#            entry.append(syn.definition())
#            meanings.append(entry)
#        else:
#            meanings.append(['none'])
#    return meanings

def get_wordnet_meaning(text_pos, text):
    """ Input list of words and pos, output list of words and lesk sense """
#    meanings = []
    
    for i in range(len(text_pos)):
        print(i)
        tup = text_pos[i][0]
        word = tup[0]
        pos = tup[1]
        sentence = get_sentence(text, i)
        
        print(word)
        print(pos)
        print(sentence)
        
#        if pos !=
        
    
#    for syn_list in text_pos:
#        for syn_tup in syn_list:
#            tup_word = syn_tup[0]
#            tup_pos = syn_tup[1]
#            if tup_pos != None:
#                entry = []
#                entry.append(tup_word)
#                print(syn_tup)
##                entry.append(syn_tup.definition())
#                meanings.append(entry)
#        else:
#            meanings.append(['none'])

    return (word, pos, sentence)


def get_sentence(text, index):
    """ Input index of a word in text, return the 10 words before and after """ 
    sentence = []
    start = index - 10
    end = index + 10
    
    for i in range(10):
        if text[index + i] != ['-']:
            sentence.append
    
    
    if start < 0:
        start = 0
    if end > len(text):
        end = len(text)
            
    return(text[start:end])


""" Main """

def main():    
    text = import_script('1_speeched_capsules copy.txt')
#    print(text)
    
    text_pos = get_pos(text)
#    print(text_pos)
    
    text_pos_meanings = get_wordnet_meaning(text_pos, text)
    print(text_pos_meanings)
    
    # write output into file
#    disambiguation_output = open('10_output.txt', 'w', encoding = 'utf8')
#    for item in text_pos_meanings:
#    disambiguation_output.join('\n'.join(text_pos_meanings))
    
    return 'ganbatte'

#print(main())






