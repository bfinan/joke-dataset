Joke Processing Pipeline

1. remove_pattern.py
   - Remove jokes without '?'

2. question_splitter.py
   - Split jokes into questions and answers

3. Manually merge columns
   - TODO
   - Merge columns {2:} into 2
   - Label the third column as 'meta'


6. joke_policies.py
   - Apply policies to ensure the question-answer format is correct

4. joke_tagger.py
   - Apply tags

5. joke_mover.py
   - Move tags to the appropriate subfiles (e.g. 'tag:nosubject', 'type:tradlightbulb')

7. merge_CSVs.py
