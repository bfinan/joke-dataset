# INPUT: .csv with "Question", "Answer", and "meta" fields.
# OUTPUT: .csv with only the rows with the specified "meta" tags.


import pandas as pd
import sys
from time import strftime

INFILE = 'pull2.csv'
DELETE_AFTER_MOVING = False
df = pd.read_csv(INFILE)

cols = (["Question", "Answer", "meta"])
newdf = pd.DataFrame(columns=cols)


tag = "tag:nosubject"
if len(sys.argv) > 1:
    tag = sys.argv[1]

outfile = tag + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"


insertion_row = 1
for idx, tags in enumerate(df["meta"]):
    if tag in tags:
        newdf.loc[insertion_row] = df.loc[idx]
        if DELETE_AFTER_MOVING:
            df = df.drop(idx)
        insertion_row += 1

    if (idx % 5000 == 0):
        print idx

df.to_csv(INFILE, encoding='utf-8', index=False)
newdf.to_csv(outfile, encoding='utf-8', index=False)
