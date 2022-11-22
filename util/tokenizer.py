import re
import os
import spacy

from islenska import Bin

b = Bin()

nlp = spacy.load("en_core_web_sm")

stop_words_path = os.getcwd()+'/txts/stop_words_english.txt'
stop_words = open(stop_words_path, 'r')

def custom_tokenizer(x):
    pattern = re.compile(r'(?x) \w\.[áí]\s\w\. | (?:\w+\.(?!$))+ | \w+(?:[-\']\w*)* | [\.,?!]')
    t_base = pattern.findall(x)
    t = []
    for token in t_base:
        if (token.count('.') > 1 or token.count('.') < 1 or token == '.'):
            t.append(token)
        else:
            t.append(token[:-1])
            t.append(token[-1])
    return t

def question_processing2(question):
    # Lemmar og tekur út stopporð ásamt ?, ! og kommu
    doc = nlp(question)
    jonathan = " ".join([token.lemma_ for token in doc])
    joseph = custom_tokenizer(jonathan)
    tokens_normalized = []
    for token in joseph:
        if token != ',' and token != '?' and token != '!' and token not in stop_words:
            w, m = b.lookup(token)
            if len(m) > 0:
                tokens_normalized.append(m[0].ord)
            else:
                tokens_normalized.append(token)
    res = []
    # None birtist for some reason, tekið út
    for val in tokens_normalized:
        if val != None :
            res.append(val)
    return tokens_normalized