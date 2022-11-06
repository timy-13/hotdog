import nltk
from nltk import pos_tag
import spacy

def lineInput(para):
    lines = list(para.split('\n'))
    return lines

def questionGen(inText):

    nlp = spacy.load("en_core_web_sm")

    text = list(inText.lower().strip('.!').split())

    #tag each type of word
    tokens = pos_tag(text)

    #tokenize breaks sent
    #print(text)
    #interrogative, auxillary, adjective, noun, adverb, verb, object
    print(tokens)

    #adj: (JJ, JJR, JJS)
    #noun: (NN, NNS, NNP, NNPS)
    #verb: (VB, VBG, VBD, VBP, VBZ)

    #nltk identifier codes for nouns, adjectives, verbs
    if tokens[0][1] == 'DT':
        text.remove(tokens[0][0])

    videntifier = ['VB', 'VBG', 'VBD', 'VBP', 'VBZ']
    verbs = []
    nums = []
    bc = False

    #Separate each word in sentence by their type
    for i in range(len(tokens)):
        if tokens[i][1] in videntifier:
            verbs.append(tokens[i][0])
        elif tokens[i][0] == 'because':
            bc = True
            text = text[:i]

    doc = nlp(' '.join(text))
    entityRec = [(X.text, X.label_) for X in doc.ents]
    print([(X.text, X.label_) for X in doc.ents])

    if bc == True:
        text.pop(text.index(verbs[0])) 
        text.pop(text.index('because'))
        question = 'How ' + verbs[0] + ' ' +  ' '.join(text) + '?'
        print(question)
        exit()

    place = ['GPE', 'GEO']
    time = ['TIM', 'DATE']
    wh = ''
    for i in range(len(entityRec)):
            if entityRec[i][1] in place:
                text.pop(text.index(entityRec[i][0]))
                wh = 'Where '
            elif entityRec[i][1] == 'PERSON':
                text.pop(text.index(entityRec[i][0]))
                wh = 'Who '
            elif entityRec[i][1] in time:
                text.pop(text.index(entityRec[i][0]))
                wh = 'When '
            else:
                wh = 'What '
                text.pop(text.index(entityRec[i][0]))
                break


    text.pop(text.index(verbs[0]))
    question = wh + verbs[0] + ' ' +  ' '.join(text) + '?'
    return(question.capitalize())
