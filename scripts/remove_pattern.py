# INPUT: .csv file with a single column "Joke" containing any text.
# OUTPUT: .csv file without rows with no '?'.

import sys
import pandas as pd
from time import strftime

OPERATION_COL = "Joke"
OPERATION_PATTERN = "?"

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    print "Usage:   python remove_pattern.py file1.csv"
    
outfile = infile + "_without_" + OPERATION_PATTERN + "_IN_" + OPERATION_COL + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"

chunks = pd.read_csv(infile, dtype={OPERATION_COL: unicode}, chunksize=50000)

slim_data = []

for chunk in chunks:
    for index, row in chunk.iterrows():
        if index % 100 == 0:
            print index
        if (OPERATION_PATTERN in row[OPERATION_COL]) is False:
            chunk.drop(index, inplace=True)
    slim_data.append(chunk)

df = pd.concat(slim_data)

df.to_csv(outfile, encoding='utf-8', index=False)
