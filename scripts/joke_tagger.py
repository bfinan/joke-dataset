# joke_tagger.py
# INPUT: .csv, columns 'Question','Answer','meta'
# OUTPUT: tagged .csv

# RUNTIME INFORMATION: The longest loop has a strict  
# runtime of len(type_dict) * len(df.index). This
# is an area for potential optimization.

import pandas
import re
import sys
from time import strftime

infile = ''
TAGFILE = 'scripts/tags.py'
VERBOSITY = 8

if len(sys.argv) > 1:
        infile = sys.argv[1]
        
df = pandas.read_csv(infile)
type_dict = eval(open(TAGFILE).read())

# Flags for the policy methods.
initial_processing = True
joke_typing = True
lightbulb = True

if initial_processing:
    local_verbosity = (10 - VERBOSITY) * 1000
    print "Initial processing..."
    # Remove duplicates. Comment this if it's taking too long.
    df.drop_duplicates()
    for idx, question in enumerate(df["Question"]):
        # Capitalize the first letter.
        capitalized = question[0].upper()
        capitalizedjoke = capitalized + question[1:]
        df.loc[df.index[idx], "Question"] = capitalizedjoke
        # Remove existing tags.
        df.loc[df.index[idx], "meta"] = " "

if joke_typing:
    print "Identifying joke types..."
    local_verbosity = (10 - VERBOSITY) * 2500
    for idx, question in enumerate(df["Question"]):
        # Iterate through each tag.
        for entry in type_dict:
            if entry in question.lower():
                if "type:" not in df.loc[df.index[idx], "meta"]:
                    df.loc[df.index[idx], "meta"] = df.loc[df.index[idx], "meta"] + type_dict[entry] + ","
        hasSubject = False
            if locus in question:
                hasSubject = True
        if hasSubject is False:
            df.loc[df.index[idx], "meta"] = df.loc[df.index[idx], "meta"] + "tag:nosubject" + ","
            
        if idx % local_verbosity == 0:
            print idx
            if idx == 1000:
                df.to_csv(tagged_sample.csv, encoding='utf-8', index=True)

if lightbulb:
    local_verbosity = (10 - VERBOSITY) * 5000
    print "Identifying lightbulb jokes."
    for idx, meta in enumerate(df["meta"]):
        if "tag:lightbulb" in meta and "tag:quantity" in meta:
            df.loc[df.index[idx], "meta"] = "type:tradlightbulb,"
            
        if idx % local_verbosity == 0:
            print idx

outfile = "tagged_"+ infile[:-3] + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"
df.to_csv(outfile, encoding='utf-8', index=True)
