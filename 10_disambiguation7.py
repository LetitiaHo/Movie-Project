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
    print("Running import_script")
    
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

    return content_split_again



""" Tag POS of each word """

def get_pos(text):
    """ Get the part of speech of each word in the text, from treebank """
    print("Running get_pos")
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

def get_wordnet_meaning(text_pos, text):
    """ Input list of words and pos, output list of words and lesk sense """
    print("Running get_wordnet_meaning")
    meanings = []
    
    for i in range(len(text_pos)):
        tup = text_pos[i][0]
        word = tup[0]
        pos = tup[1]
        sentence = get_sentence(text, i)

        if pos != None:
            entry = []
            entry.append(word)
            syn = lesk(sentence, word, pos)
            if syn is None:
                entry.append(None)
            else:
                string_syn = str(syn)
                entry.append(string_syn[6:])
                entry.append(syn.definition())
            meanings.append(entry)
        else:
            meanings.append(['None'])
            
    return meanings

def get_sentence(text, index):
    """ Input index of a word in text, return the 10 words before and after """ 
    sentence = []
    sentence.append(text[index][0])

    for i in range(1, 10):
        if index + i < len(text) and index - i >= 0:
            if text[index + i] != ['-']:
                word = text[index + i][0]
                sentence.append(word)
            if text[index - i] != ['-']:
                word = text[index - i][0]
                sentence.insert(0, word)
            
    return ' '.join(sentence)



""" Main """

def main():    
    text = import_script('1_speeched_capsules copy.txt')
#    print(text)
    
    text_pos = get_pos(text)
#    print(text_pos)
    
    text_pos_meanings = get_wordnet_meaning(text_pos, text)
#    print(text_pos_meanings)
    
    disambiguation_output = open('10_output.txt', 'w', encoding = 'utf8')
    for item in text_pos_meanings:
        disambiguation_output.write("%s\n" % item)    
    disambiguation_output.close()
    
    return 'Done'

print(main())





