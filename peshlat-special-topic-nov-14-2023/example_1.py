# Example 1: Simple usage

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

print('TEXT', '\t', 'LEMMA', '\t', 'POS', '\t', 'TAG', '\t', 'DEPENDENCY', '\t',
            'SHAPE', '\t', 'IS_ALPHA', '\t', 'IS_STOP', '\n')

for token in doc:
    print(token.text, '\t', token.lemma_, '\t', token.pos_, '\t', token.tag_, '\t', token.dep_, '\t',
            token.shape_, '\t', token.is_alpha, '\t', token.is_stop, '\n')