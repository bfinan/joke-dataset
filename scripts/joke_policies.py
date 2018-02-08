# INPUT: .csv file with Question/Answer jokes
# OUTPUT: .csv file with various policies applied.
import pandas as pd
from jokeutils import *

with open('dicts/chars.txt', 'r') as chars:
    validchars = chars.read()

def processing(df):
    for i, row in enumerate(df.itertuples(),1):
        print(row.Index)
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

infile = parse_args()
mainframe = pd.read_csv(infile, dtype={"Question": object, "Answer": object})
outframe = parallel_dataframe(mainframe, processing)
outfile = outfile_name("processed_jokes")

outframe.to_csv(outfile, encoding='utf-8', index=False)
