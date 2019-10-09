# tokenization.py
# 10.09.19

import spacy

nlp = spacy.load('en_core_web_sm')

mystring = '"We\'re moving to L.A.!"'
print(mystring)

# Create a doc obj
doc = nlp(mystring)
for token in doc:
    print(token.text, end = '|')

# Testing for tokens of punctuation/ symbols:
doc2 = nlp(u"We're here to help! Send snail-mail, to test@someemail.com!!")
for token in doc2:
    print(token)
print()
for token in nlp(u'This is test $10.30, at 3:30pm'):
    print(token)

# Names entities
doc3 = nlp(u'Apple to build Hong Kong Factory for $6 million')
for token in doc3:
    print(token.text, end = '|')
print('\n------\n') # because the print statement above has | vs \n
for ent in doc3.ents:
    print(f'{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}')

print(type(doc3.ents))

# noun chunks
doc4 = nlp(u"Red cars do not carry higher insurance rates.")
for chunk in doc4.noun_chunks:
    print(chunk) # Do you need to print text? No. Are the types the same?

# What part of speech is 'insurance' in the above. Adj?
print(doc4[-3].pos_) # Says noun, but that doesn't seem right
for token in doc4:
    print(token.text, token.pos_, spacy.explain(token.pos_))

# Visualizing with displaCy
# Using doc3
# spacy.displacy.serve(doc3, style='dep')

# Note: Keyboard interrupt is Ctrl+F2
spacy.displacy.serve(doc3, style = 'ent')

