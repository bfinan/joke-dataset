# joke_tagger.py
# INPUT: .csv, columns 'Question','Answer','meta'
# OUTPUT: tagged .csv

# RUNTIME INFORMATION: The longest loop has a strict  
# runtime of len(type_dict) * len(df.index). This
# is an area for potential optimization.

import pandas
import re
from jokeutils import *

infile = parse_args()
TAGFILE = 'scripts/tags.py'
        
inframe = pandas.read_csv(infile)
type_dict = eval(open(TAGFILE).read())

def joke_typing(df):
    df["meta"] = " "
    print("Identifying joke types...")
    for idx, question in enumerate(df["Question"]):
        if idx % 1000 == 0:
            print(idx)
        # Iterate through each tag.
        for entry in type_dict:
            if entry in question.lower():
                if "type:" not in df.loc[df.index[idx], "meta"]:
                    df.loc[df.index[idx], "meta"] += type_dict[entry] + " "
    return df

def lightbulb(df):
    print("Identifying lightbulb jokes.")
    for idx, meta in enumerate(df["meta"]):
        if "tag:lightbulb" in meta and "tag:quantity" in meta:
            df.loc[df.index[idx], "meta"] = "type:tradlightbulb "
    return df


inframe = parallel_dataframe(inframe, joke_typing)
inframe = parallel_dataframe(inframe, lightbulb)
outfile = outfile_name("tagged")
inframe.to_csv(outfile, encoding='utf-8', index=False)
