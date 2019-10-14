# coding=utf-8
from collections import Counter
import csv
import time
import pymorphy2
from stop_words import get_stop_words

# "C:\workPlace\\text.txt"

#read from file
f = open(input(), 'r')
words = f.read()
#f2 = open("C:\workPlace\\text2.txt", 'w')
start_time = time.time()

#symbols for remove
puncts = ",.?!():;[]\n"
#removing symbols
for sym in puncts:
    words = words.replace(sym, '')
#text in lower case and split text to list of words
words = words.lower().split()
#print(morph)

#list of stop words for remove
stop_words = get_stop_words('ru')


#for normalize
morph = pymorphy2.MorphAnalyzer()
norm_list = []
#normalize words and remove stop-words
for word in words:
    p = morph.parse(word)[0]
    norm_list.append(p.normal_form)
for word in norm_list:
    if word in stop_words:
        norm_list.remove(word)

#print(a)

#counter of words
counter = Counter(norm_list)
#2 columns: word - count
pairs = [(pair[0], pair[1]) for pair in counter.most_common()]

#write in csv
with open("C:\workPlace\\text3.csv", "w", newline='') as f3:
    writer = csv.writer(f3)
    for row in pairs:
        writer.writerow(row)

#
print("--- %s seconds ---" % (time.time() - start_time))
