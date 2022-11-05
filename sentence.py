import nltk
from nltk import pos_tag
import spacy

nlp = spacy.load("en_core_web_sm")

#nltk.download()

text = list(input().split())

tokens = pos_tag(text)

#tokenize breaks sent
#print(text)
#interrogative, auxillary, adjective, noun, adverb, verb, object
print(tokens)

#adj: (JJ, JJR, JJS)
#noun: (NN, NNS, NNP, NNPS)
#verb: (VB, VBG, VBD, VBP, VBZ)

nidentifier = ['NN', 'NNS', 'NNP', 'NNPS']
aidentifier= ['JJ', 'JJR', 'JJS']
videntifier = ['VB', 'VBG', 'VBD', 'VBP', 'VBZ']
nouns = []
adjs = []
verbs = []
bc = False


for i in range(len(tokens)):
    if tokens[i][1] in nidentifier:
        nouns.append(tokens[i][0])
    elif tokens[i][1] in aidentifier:
        adjs.append(tokens[i][0])
    elif tokens[i][1] in videntifier:
        verbs.append(tokens[i][0])
    elif tokens[i][0] == 'because':
        bc = True
        #text[i].remove()
        text = text[:i]



#if 'going' in verbs:
    #where is {noun} going?
    #lemmas for going

if bc == True:
    # How does/did {noun} {verb} {gimojji}
    text.pop(text.index(verbs[0])) 

    question = 'How ' + verbs[0] + ' ' +  ' '.join(text) + '?'
    print(question)

else:

    text.pop(text.index(verbs[0]))

    question = verbs[0] + ' ' + ' '.join(text) + '?'
    print(question)
    

entityRec = nlp(nouns)
print(entityRec)