#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp.tokenizer
import nlp.TextVectorizer

import sys
import os

def save(filename, term_weights):
    f = open(filename, 'w')
    f.write('word,count\n')
    for t, w in sorted(term_weights.items(), key=lambda x:-x[1]):
        f.write("%s,%f\n" % (t.encode('utf-8'), w))
    f.close()

filenames = sys.argv[1:]
texts = []
for filename in filenames:
    t = open(filename).read().decode('utf-8')
    texts.append(t)

v = nlp.TextVectorizer.TfidfVectorizer(tokenizer=nlp.tokenizer.tokenizeJp, texts=texts)
tfidf_list = v.vectorize()

for filename, tfidf in zip(filenames, tfidf_list):
    output = './output/' + os.path.basename(filename) + '.tfidf'
    save(output, tfidf)
