#!/usr/bin/env python
import sys

stopWords = set(['each', "hasn't", "weren't", 'had', 'off', 'at', 'ourselves', 'be', 'not', 'does', 'mightn', 'once', 'his', 'yourselves', 'until', 'into', 'hasn', 'against', "won't", 'did', 'before', 'theirs', 'both', 'am', 'there', 'only', "should've", 'we', 'it', 'of', 'by', 'more', 'aren', "you'd", 'and', 'whom', 'further', 't', 'what', 'being', 'herself', "couldn't", "mustn't", 'all', 'shan', 'with', 'any', 'yourself', 're', 'me', 'from', 'needn', 'to', 'm', 'because', 'yours', "needn't", 'over', 'as', 'have', 'wouldn', 'when', 'myself', "shan't", 'don', 'won', "wouldn't", 'can', 'their', 'on', 'below', "it's", 'wasn', 'will', 'most', 'should', "hadn't", 'isn', 'who', 'them', 'which', 'having', "she's", 'doing', 'how', 'nor', 'those', 'or', 'been', 'where', 's', 'he', 'him', 'so', 'here', 'its', 'you', 'themselves', "shouldn't", 'mustn', "you're", 'ma', 'some', 'her', 'hers', "mightn't", 'y', 'my', 'while', 'itself', 'this', 'do', 'doesn', 'during', 'above', 'through', 'out', 'ours', 'up', 'i', 'than', 'that', 'are', "you'll", 'under', 'has', "wasn't", 'your', 'such', "don't", 'they', 'shouldn', 'was', 'll', 'o', 'between', 'same', 'the', 'why', 'other', 'ain', 'these', 'then', 'in', 'if', 'again', 'just', 'couldn', "haven't", 'a', 'but', 'd', 'very', 'no', "you've", 'about', 'hadn', 'our', 'she', 'too', 'few', 'now', 'for', 'haven', "isn't", 'is', 'weren', 'own', 'an', 'were', 'down', "aren't", "didn't", 'after', 'himself', "that'll", 've', "doesn't", 'didn'])

#--- get all lines from stdin ---

for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()
    words = line.split()

    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        # ignore words wih length 0,1 or stop words.
        if len(word)>1 and word not in stopWords:
            print '%s\t%s' % (word, "1")
