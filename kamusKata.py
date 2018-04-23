#!/usr/bin/env python3
out = open('wordDict.csv', 'w')
with open("dataclean.csv") as fobj:
    text = fobj.read().strip().split()
    kamus = []
    for kata in text:
        if kata in kamus:
            print ("duplicate")
        else:
            kamus.append(kata)
    for j in range(len(kamus)):
        out.write(kamus[j] + '\n')
out.close()
print (kamus)