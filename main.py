# coding=utf-8
from collections import Counter
import pickle

f = open("C:\workPlace\\text.txt", 'r')
f2 = open("C:\workPlace\\text2.txt", 'w')
words = f.read()
puncts = ",.?!():;\n—"

for sym in puncts:
    words = words.replace(sym, '')



words = words.lower()
words = words.split()

counter = Counter(words)
pairs = [(pair[0], pair[1])for pair in counter.most_common()]


for item in pairs:
    n = ' '.join(map(str, item))

    #n = '\n'.join(n)
    print(n)
    f2.write(n)
    f2.write('\n')
