#!/usr/bin/env python
import sys
tw = sys.argv[1].split(",")
top_words = {word:0 for word in tw}


#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    t_words = dict(top_words)
    li = []
    for word in words:
        if word in t_words:
            t_words[word]=1
    for word in tw:
	if t_words[word]==1:
            li.append(word)
    
    # make pair of words and emit words
    for i in xrange(len(li)):
        for j in xrange(i+1,len(li)):
            print '%s\t%s' % (str(li[i])+","+str(li[j]), "1")

