import sys
from subprocess import call
import pandas
import re, string
from jokeutils import *
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from functools import reduce
from colors import bcolors

infile = parse_args()
df = pandas.read_csv(infile, encoding="utf-8")
print(df.shape)
s=set(stopwords.words('english'))
stop = list(map(lambda x:x.upper(), s))
totaldrops = 0

MANUAL = False

size = len(df.index)
startIndex = int(input("Select starting index: "))

for currentIndex, current in enumerate(df.itertuples(), startIndex):
    if(currentIndex > size - totaldrops - 1):
        break
    if(currentIndex % 250 == 0):
        print("{0:.2f}%".format(float(currentIndex)/float(size) * 100))

    qstring = df.loc[currentIndex, "Question"].upper() + " " + df.loc[currentIndex, "Answer"].upper()
    qstring = qstring.translate(str.maketrans('','', string.punctuation))
    klist = list(filter(lambda w: not w in stop, qstring.split()))
    kwid = '-'.join(str(v) for v in klist)
    df.loc[currentIndex, "kwid"] = kwid
    
    drops = 0
    for finderIndex, found in zip(range(currentIndex-1), df.itertuples()):
        if finderIndex == currentIndex:
            break
            
        if(df.loc[finderIndex, "kwid"] == kwid):
            if MANUAL is True:
                call(["clear"])
                print()
                print( "[1] " + str(currentIndex) + ": " + df.loc[currentIndex, "Question"] + " " + df.loc[currentIndex, "Answer"] )
                print()
                print( "[2] " + str(finderIndex) + ": " + df.loc[finderIndex, "Question"] + " " + df.loc[finderIndex, "Answer"])
                print()
                commandKey = input("Select which one(s) to drop: (1/2) ").lower()
                if '1' in commandKey:
                    df.drop(currentIndex, inplace=True)
                    drops = drops+1
                    totaldrops += 1
                if '2' in commandKey:
                    df.drop(finderIndex, inplace=True)
                    drops = drops+1
                    totaldrops += 1
                if 'e' in commandKey:
                    outfile = outfile_name("partial_dupdel")
                    df.to_csv(outfile, encoding='utf-8', index=False)
                    print(bcolors.WARNING + bcolors.BOLD + "Be sure to write down where you left off!")
                    sys.exit()
            else:
                    df.drop(currentIndex, inplace=True)
                    drops = drops+1
                    totaldrops += 1
    if drops:
        df.reset_index(drop=True, inplace=True)

outfile = outfile_name("kwids_added")

df.to_csv(outfile, encoding='utf-8', index=False)



