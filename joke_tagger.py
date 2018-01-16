import pandas
import re
import sys
df = pandas.read_csv('split_tweet_jokes.csv')
type_dict = eval(open("tags.py").read())

outfile = "jokes_copy.csv"

if len(sys.argv) > 1:
        outfile = sys.argv[1]

initial_processing = True
joke_typing = True
lightbulb = True

if initial_processing:
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
    for idx, question in enumerate(df["Question"]):
        # Iterate through each tag.
        for entry in type_dict:
            if entry in question.lower():
                if "type:" not in df.loc[df.index[idx], "meta"]:
                    df.loc[df.index[idx], "meta"] = df.loc[df.index[idx], "meta"] + type_dict[entry] + ","
        hasSubject = False
        for loci in ("Who", "What", "Where", "Why", "When", "Which", "How"):
            if loci in question:
                hasSubject = True
        if hasSubject is False:
            df.loc[df.index[idx], "meta"] = df.loc[df.index[idx], "meta"] + "tag:nosubject" + ","

if lightbulb:
    print "Identifying lightbulb jokes."
    for idx, meta in enumerate(df["meta"]):
        if "tag:lightbulb" in meta and "tag:quantity" in meta:
            df.loc[df.index[idx], "meta"] = "type:tradlightbulb,"


df.to_csv(outfile, encoding='utf-8', index=True)
