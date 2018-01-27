# INPUT: .csv file with Question/Answer jokes
# OUTPUT: .csv file with various policies applied.
import sys
import pandas as pd
import numpy as np
from multiprocessing import Pool

num_partitions = 10
num_cores = 4

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    print "Usage:   python joke_policies.py file1.csv"

def parallelize_dataframe(dframe, func):
    dframe_split = np.array_split(dframe, num_partitions)
    pool = Pool(num_cores)
    poolmap = pool.map(func, dframe_split)
    dframe = pd.concat(poolmap)
    pool.close()
    pool.join()
    return dframe

def processing(df):
    for i, row in enumerate(df.itertuples(),1):
        print row.Index
        markForDrop = False
        
        # Questions will start with capital letters
        capitalized = df.loc[row.Index, "Question"][0].upper()
        capitalizedjoke = capitalized + df.loc[row.Index, "Question"][1:]
        df.loc[row.Index, "Question"] = capitalizedjoke

        # Questions will start with a locus
        hasSubject = False
        for locus in ("Who", "What", "Where", "Why", "When", "Which", "How"):
            if locus in row.Question:
                hasSubject = True
                location = row.Question.find(locus)
                fixed = row.Question[location:]
                df.loc[row.Index, "Question"] = fixed
                break
        if hasSubject is False:
            markForDrop = True

        # Question will end with '?'
        if df.loc[row.Index, "Question"].endswith('?') is False:
            df.loc[row.Index, "Question"] += '?'

        if type(df.loc[row.Index, "Answer"]) == float:
            markForDrop = True

        # Answer will start with an alphanumeric character
        # (not punctuation or whitespace)
        if markForDrop is False:
            if str(df.loc[row.Index, "Answer"])[0].isalnum() is False:
                while str(df.loc[row.Index, "Answer"][0]).isalnum() is False:
                    if len(df.loc[row.Index, "Answer"]) >= 2:
                        df.loc[row.Index, "Answer"] = df.loc[row.Index, "Answer"][1:]
                    else:
                        markForDrop = True
                        break    

        if markForDrop is True:
            df.drop(row.Index, inplace=True)

    df.drop_duplicates()
    return df

mainframe = pd.read_csv(infile, dtype={"Question": object, "Answer": object})
outframe = parallelize_dataframe(mainframe, processing)

outframe.to_csv("processedTweets.csv", encoding='utf-8', index=False)
