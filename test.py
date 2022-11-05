import nltk
from nltk import pos_tag

#nltk.download()

text = list(input().split())

tokens = pos_tag(text)

#tokenize breaks sent
#print(text)
#interrogative, auxillary, adjective, noun, adverb, verb, object
print(tokens)