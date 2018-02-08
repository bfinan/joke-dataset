Joke Processing Pipeline

1. question_splitter.py
   - Remove lines without a '?'
   - Split jokes into questions and answers

2. Manually merge columns
   - TODO
   - Merge columns {2:} into 2
   - Label the third column as 'meta'

3. joke_policies.py
   - Apply policies to ensure the question-answer format is correct

4. joke_tagger.py
   - Apply tags

5. joke_mover.py
   - Move tags to the appropriate subfiles (e.g. 'tag:nosubject', 'type:tradlightbulb')

6. merge_CSVs.py
