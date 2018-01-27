# INPUT: A .csv file whose rows contain a delimiter (for questions, this is '?').
# OUTPUT: A .csv file with columns "Question", "Answer", "meta",
# where Question and Answer are the text before and after the delimiter

# This makes separate rows for Q and A, and I'm not sure how to fix it.
# A quick vim fix is :%s/,\n,/,/g

# This won't work if there's a single row without a delimiter.
import sys
import pandas as pd
from time import strftime

DELIMITER = '?'

infile = ""
if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    print "Usage:   python question_splitter.py infile.csv"

outfile = "split_questions"+ DELIMITER + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"

indf = pd.read_csv(infile, dtype={"Joke": unicode})
outdf = pd.DataFrame(columns=['Question', 'Answer', 'meta'])

for index, row in indf.iterrows():
    joke_halves = row["Joke"].split(DELIMITER)
    # Append the question and answer.
    outdf = outdf.append([{"Question": joke_halves[0] + DELIMITER}, {"Answer": ' '.join(joke_halves[1:])}], ignore_index=True)
    if index % 100 == 0:
        print index

outdf.to_csv(outfile, encoding='utf-8', index=False)
