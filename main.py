# coding=utf-8
from collections import Counter
import csv
import pymorphy2
from stop_words import get_stop_words


#func write to file
def write_file():
    try:
        with open(input(), "w", newline='') as f3:
            writer = csv.writer(f3)
            for row in pairs:
                writer.writerow(row)
    except:
        print('Закройте файл в котороый ведется запись и введите путь вновь')
        write_file()

#func read from file
def read_file():
    try:
        f =open(input(), 'r')
        return f
    except:
        print('Путь указан неверно, введите путь вновь')
        f =read_file()
        return  f


# "C:/workPlace/text.txt"


#read from file
print('Укажите путь к входному файлу пр. C:/text.txt')
f = read_file()
words = f.read()


#symbols for remove
puncts = ",.?!():;[]{}\n–"
#removing symbols
for sym in puncts:
    words = words.replace(sym, '')
#text in lower case and split text to list of words
words = words.lower().split()

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


#counter of words
counter = Counter(norm_list)
#2 columns: word - count
pairs = [(pair[0], pair[1]) for pair in counter.most_common()]

#write in csv
#"C:/workPlace/text3.csv"
print('Укажите путь к выходному файлу пр. C:/text3.csv')
write_file()