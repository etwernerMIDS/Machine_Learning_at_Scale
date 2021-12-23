#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########

    # tally counts from current key                 
    if word == current_word: 
        
        #SPAM = binary; with 1 indicating a spam message
        if int(is_spam) == 0:
            ham_count += int(count)
        else:
            spam_count += int(count)
                             
    # OR ...                                        
    else:                                           
        
        if current_word: 
            print(f'{current_word}\t{0}\t{ham_count}') 
            print(f'{current_word}\t{1}\t{spam_count}') 
        
        # and start a new tally                     
        current_word = word
        spam_count, ham_count = 0,0
        
        if int(is_spam) == 0:
            ham_count += int(count)
        else:
            spam_count += int(count)
        
                                                    
## don't forget the last record!   
print(f'{current_word}\t{0}\t{ham_count}') 
print(f'{current_word}\t{1}\t{spam_count}') 













############ (END) YOUR CODE #########