# spacy_basics.py
# 10.08.19

import spacy

# Load the language library
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
# Language library object used to parse and process the text.
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')

for token in doc:
    print(token.text, token.pos_, token.dep_)

print()
# Showing that spacy reconized is and n't, and the space and period all also
# grabbed and assigned tokens.
doc2 = nlp(u"Telsa isn't     looking into startups anymore.")
for token in doc2:
    print(token.text, token.pos_, token.dep_)

print(doc2)
# Showing Span
print(len(doc2)) # Len is the number of tokens.

# Does slicing slice on token or \w characters?
print(doc2[4:6]) # indices 4 and 5.
print()
# Sentences
doc3 = nlp(u'This is a sentence. The second sent stars here. And a third goes here.')
for sent in doc3.sents:
    print(sent)

# and indexing to find the start of sentence:
print(doc3[5].is_sent_start)
print(type(doc3.sents))

