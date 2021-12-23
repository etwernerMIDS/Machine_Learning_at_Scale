#!/usr/bin/env python
"""
This script reads word counts from STDIN and aggregates
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE (standalone):
    python aggregateCounts_v2.py < yourCountsFile.txt

Instructions:
    For Q7 - Your solution should not use a dictionary or store anything   
             other than a single total count - just print them as soon as  
             you've added them. HINT: you've modified the framework script 
             to ensure that the input is alphabetized; how can you 
             use that to your advantage?
"""

# imports
import sys


################# YOUR CODE HERE #################

# initialize trackers
cur_word = None
cur_count = 0

# read input key-value pairs from standard input
for line in sys.stdin:
    word, count  = line.split()
    # tally counts from current key
    if word == cur_word: 
        cur_count += int(count)
    elif cur_word is None:
        cur_word = word
        cur_count += int(count)
    # OR emit current total and start a new tally 
    else: 
        if cur_word:
            print(f'{cur_word}\t{cur_count}')
        cur_word, cur_count  = word, int(count)

# don't forget the last record! 
print(f'{cur_word}\t{cur_count}')




################ (END) YOUR CODE #################
