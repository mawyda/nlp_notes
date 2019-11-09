# lemmatization.py
# 10.12.19

import spacy

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(u"I am a runner running in a race because I love to run since I ran today")
# Loop through, using the new lemma attributes.
for token in doc1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)

print()

def show_lemmas(text):
    for token in text:
        # Returns the text, the Part of Speech, the lemma number, and hte
        # lemma itself.
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')

doc2 = nlp(u"I saw eighteen mice today!")
show_lemmas(doc2)

print('\n--------')

doc3 = nlp(u'I am meeting him tomorrow at the meeting.')
show_lemmas(doc3)
# Here 'meeting' is recognized in it's two different forms/ pos_

print('\n--------')

doc4 = nlp(u"That's an enormous automobile")
show_lemmas(doc4)
# Lemmatization does not reduce words down to their most basic synonym


