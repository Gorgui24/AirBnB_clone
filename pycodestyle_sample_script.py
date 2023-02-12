import numpy as np, pandas as pd
words = raw_input("Enter some text to translate to pig latin: " )
words_list = words.split(' ' )
for word in words_list:
    if len(word) >= 3 :
        pig_latin = word + "%say" % (word[0])
        pig_latin = pig_latin[ 1: ]
        print(pig_latin )
    else:
        pass
