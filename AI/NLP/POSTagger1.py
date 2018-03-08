import nltk

text=nltk.word_tokenize("The planet Jupiter and its moons are in effect a minisolar system, and Jupiter itself is often called a star that never caught fire.")

taggedwords = nltk.pos_tag(text)
print(' '.join('{}/{}'.format(*el) for el in taggedwords))