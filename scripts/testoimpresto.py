import pandas
import re, string
from jokeutils import *
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from functools import reduce
infile = parse_args()
df = pandas.read_csv(infile, encoding="utf-8")

s=set(stopwords.words('english'))
stop = list(map(lambda x:x.upper(), s))

for currentIndex, current in enumerate(df.itertuples()):
    print("Current: " + str(currentIndex))
    drops = 0
    qstring = df.loc[currentIndex, "Question"].upper() + " " + df.loc[currentIndex, "Answer"].upper()
    qstring = qstring.translate(str.maketrans('','', string.punctuation))
    klist = list(filter(lambda w: not w in stop, qstring.split()))
    kwid = '-'.join(str(v) for v in klist)
    print(kwid)
