#!/usr/bin/env python
import sys
import operator
# maps words to their counts
word2count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
    try:
        word2count[word] = count
    except:
        pass

# sort dictionary based on values
sorted_d = sorted(word2count.items(), key=operator.itemgetter(0), reverse=True)
#print top 10 set of words only
for key in sorted_d[:10]:
    print '%s\t%s' % (key[0], key[1])


