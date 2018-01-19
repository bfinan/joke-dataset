# INPUT: .csv file with Question/Answer jokes
# OUTPUT: .csv file with various policies applied.
import sys
import pandas as pd

# Flags for the policy methods.

question_ends_in_eroteme = True
# Force question to end with '?'

question_begins_with_loci = True
# Remove questions without an answer.

answer_starts_with_nonspace = True
# Remove stuff before the loci of the question

answer_is_not_blank = True
# Remove blank questions

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    print "Usage:   python joke_fixer.py file1.csv"

chunks = pd.read_csv(infile, dtype={"Question": unicode, "Answer": unicode}, chunksize=50000)

slim_data = []

for chunk in chunks:
    for index, row in chunk.iterrows():
        if index % 1000 == 0:
            print index

        if question_ends_in_eroteme:

            if (row["Question"][-1] == '?') is False:
                row["Question"] += "?"

        if question_begins_with_loci:
            for loci in ("Who", "What", "Where", "Why", "When", "Which", "How"):
                if loci in row["Question"]:
                    question_loci = loci
                    break
            row["Question"] = row["Question"][row["Question"].find(loci):]

        if answer_is_not_blank:
            if(str(row["Answer"]) == "nan") is True:
                chunk.drop(index, inplace=True)

        if answer_starts_with_nonspace:
            try:
                if (row["Answer"][0] == ' ') is True:
                    row["Answer"] = row["Answer"].lstrip()
            except TypeError as e:
                pass

    slim_data.append(chunk)

df = pd.concat(slim_data)

df.to_csv("fixedJokes.csv", encoding='utf-8', index=False)
