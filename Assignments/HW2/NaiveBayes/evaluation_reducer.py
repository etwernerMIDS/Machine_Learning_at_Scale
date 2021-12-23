#!/usr/bin/env python
"""
Reducer to calculate precision and recall as part
of the inference phase of Naive Bayes.
INPUT:
    ID \t true_class \t P(ham|doc) \t P(spam|doc) \t predicted_class
OUTPUT:
    precision \t ##
    recall \t ##
    accuracy \t ##
    F-score \t ##
         
Instructions:
    Complete the missing code to compute these^ four
    evaluation measures for our classification task.
    
    Note: if you have no True Positives you will not 
    be able to compute the F1 score (and maybe not 
    precision/recall). Your code should handle this 
    case appropriately feel free to interpret the 
    "output format" above as a rough suggestion. It
    may be helpful to also print the counts for true
    positives, false positives, etc.
"""
import sys

# initialize counters
FP = 0.0 # false positives
FN = 0.0 # false negatives
TP = 0.0 # true positives
TN = 0.0 # true negatives

# read from STDIN
for line in sys.stdin:
    # parse input
    docID, class_, pHam, pSpam, pred = line.split()
    # emit classification results first
    print(line[:-2], class_ == pred)
    
    # then compute evaluation stats
#################### YOUR CODE HERE ###################

    # 1 - positive case & 0 - negative case
    if int(class_) == int(pred):
        #TP
        if int(pred) == 1:
            TP += 1
        #TN
        else:
            TN += 1
    else:
        #FP - actual = 1 & pred = 0
        if int(pred) == 1:
            FP += 1      
        #FN - actual = 0 & pred = 1
        else:
            FN += 1

            
print(f'{"True Positive"}\t{TP}')
print(f'{"True Negative"}\t{TN}')
print(f'{"False Positive"}\t{FP}')
print(f'{"False Negative"}\t{FN}')
          
#accuracy = (TP + TN) / (TP + TN + FP + FN)
accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f'{"Accuracy"}\t{accuracy}')    
    
#precision = TP / (TP + FP)
precision = TP/(TP + FP)
print(f'{"Precision"}\t{precision}')

#recall = TP / (TP + FN)
recall = TP/(TP + FN)
print(f'{"Recall"}\t{recall}')

#Fscore = TP / (TP + [0.5(FP + FN)] ) 
denom = 0.5 * (FP + FN)
FScore = TP / (TP + denom) 
print(f'{"F-Score"}\t{FScore}')

#################### (END) YOUR CODE ###################
    