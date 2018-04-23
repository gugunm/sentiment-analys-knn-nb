import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import OrderedDict
from nltk.tokenize import PunktSentenceTokenizer
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer

arr_praproses =[]

with open ('data_sorted_test.csv', 'r') as input :
    reader = input.read().split("\n")               #Akses data per baris
    for indeks in range(len(reader)):
        lowcase_word = reader[indeks].lower()       #lowcase data perbaris
        tokenizer = RegexpTokenizer(r'\w+')         #remove punctuatuion
        tokens = tokenizer.tokenize(lowcase_word)   #Tokenisasi Kalimat
        filtered_words = [w for w in tokens if not w in stopwords.words('english')]     #remove Stopwords
        output = []                                 #nampung hasil stemming dulu
        for kata in filtered_words:
            output.append(PorterStemmer().stem(kata)) #proses stemming per-kata dalam 1 kalimat
        arr_praproses.append(output)                #tampung kalimat hasil stemm ke arr_praproses

out = open('data_bersih_test.csv', 'w')                        #Open file .csv buat nampung data

for j in range(len(arr_praproses)):
    out.write(" ".join(arr_praproses[j]) + '\n')

out.close()
# print (len(arr_praproses))