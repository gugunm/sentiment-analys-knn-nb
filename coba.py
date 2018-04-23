import os
import csv
from xml.etree import ElementTree
import glob

file_name = ['100850.xml', '105780.xml']
out = open('data_rapih.csv', 'w')
for x in range(len(file_name)):        
    hasil =[]
    full_file = os.path.abspath(os.path.join('data/train', file_name[x]))
    dom = ElementTree.parse(full_file)
    isi = dom.findall('text/p')

    for i in isi:
        hasil.append(i.text)

    for n in range(len(file_name)):
        for j in range(len(hasil)):
            out.write(hasil[j])
            # print (hasil[j])
    out.write('\n')
out.close()


