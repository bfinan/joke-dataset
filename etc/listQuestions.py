import pandas
import re
df = pandas.read_csv('jokes.csv')


for idx, question in enumerate(df["Question"]):
    print question

#df.to_csv("jokes114.csv", encoding='utf-8')
