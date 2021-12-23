#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    partitionKey \t word \t class0_partialCount,class1_partialCount
OUTPUT:
    word \t class0_count,class1_count,class0_condProb,class1_condProb
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
"""
##################### YOUR CODE HERE ####################

import re                                                   
import sys                                                  
import numpy as np      
from operator import itemgetter
import os

cur_word = None
class0Count = 0
class1Count = 0
class0Total = 0
class1Total = 0
class0WordTot = 0
class1WordTot = 0
corpusTotal = 0

WORD_COUNT = 0

# read from standard input
for line in sys.stdin:
    # parse input
    partitionKey, word, partialCounts = line.strip().split('\t')
    class0_partialCount, class1_partialCount = partialCounts.split(',')
    class0_partialCount = float(class0_partialCount)
    class1_partialCount = float(class1_partialCount)
    
    #print(f'{word}')
    
    #doc total to compute priors
    if word == "**doc_total":
        class0Total += class0_partialCount
        class1Total += class1_partialCount
    
    #word total for conditional probability
    elif word == "**word_total":
        class0WordTot += class0_partialCount
        class1WordTot += class1_partialCount
    
    else:    
        if word == cur_word: 
            class0Count += class0_partialCount
            class1Count += class1_partialCount

        # OR emit current total and start a new tally 
        else: 
            if cur_word:
                
                WORD_COUNT += 1          

            cur_word = word

WORD_COUNT += 1
print(f'{"UniqueWordCount"}\t{WORD_COUNT}')

##################### (END) CODE HERE ####################