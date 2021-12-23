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

# confirm that we have access to the model file
#print(os.listdir('.'))
assert 'NB_size.txt' in os.listdir('.'), "ERROR: can't find NB_size.txt"

for record in open('NB_size.txt', 'r').readlines():
    word, size = record.split('\t')

size = int(size)    
    
cur_word = None
class0Count = 0
class1Count = 0
class0Total = 0
class1Total = 0
class0WordTot = 0
class1WordTot = 0
corpusTotal = 0

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
                
                #compute conditional probs
                class0prob = (class0Count + 1)/(float(class0WordTot + size))
                class1prob = (class1Count + 1)/(float(class1WordTot + size))

                print(f'{cur_word}\t{class0Count},{class1Count},{class0prob},{class1prob}')
            

            cur_word = word
            class0Count = class0_partialCount
            class1Count = class1_partialCount


class0prob = (class0Count + 1)/(float(class0WordTot + size))
class1prob = (class1Count + 1)/(float(class1WordTot + size))
print(f'{cur_word}\t{class0Count},{class1Count},{class0prob},{class1prob}')
            
            
#print ClassPriors
if partitionKey == 'A':
    corpusTotal = class0Total + class1Total
    class0prob = class0Total/float(corpusTotal)
    class1prob = class1Total/float(corpusTotal)
    print(f'{"ClassPriors"}\t{class0Total},{class1Total},{class0prob},{class1prob}')

##################### (END) CODE HERE ####################