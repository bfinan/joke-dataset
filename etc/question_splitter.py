# INPUT: A .csv file whose rows contain a delimiter (for questions, this is '?').
# OUTPUT: A .csv file with columns "Question", "Answer", "meta",
# where Question and Answer are the text before and after the delimiter

# This makes separate rows for Q and A, and I'm not sure how to fix it.
# A quick vim fix is :%s/,\n,/,/g

# This won't work if there's a single row without a delimiter.

import pandas as pd
from time import strftime

outfile = "split_questions" + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"

DELIMITER = '?'


indf = pd.read_csv("sharpjokes.csv", dtype={"Joke": unicode})
outdf = pd.DataFrame(columns=['Question', 'Answer', 'meta'])

for index, row in indf.iterrows():
    joke_halves = row["Joke"].split(DELIMITER)
    
    # Append the question and answer.
    outdf = outdf.append([{"Question": joke_halves[0] + '?'}, {"Answer": ' '.join(joke_halves[1:])}], ignore_index=True)
    print index

outdf.to_csv(outfile, encoding='utf-8', index=False)
