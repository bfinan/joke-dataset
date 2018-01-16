# INPUT: .csv file with a single column "Joke" containing any text.
# OUTPUT: .csv file without rows with no '?'.

import pandas as pd


if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    print "Usage:   python remove_pattern.py file1.csv"

chunks = pd.read_csv(infile, dtype={"Joke": unicode}, chunksize=50000)

slim_data = []

for chunk in chunks:
    for index, row in chunk.iterrows():
        if index % 100 == 0:
            print index
        if ("?" in row["Joke"]) is False:
            chunk.drop(index, inplace=True)
    slim_data.append(chunk)

df = pd.concat(slim_data)

df.to_csv("sharpjokes.csv", encoding='utf-8', index=False)
