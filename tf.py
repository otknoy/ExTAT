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

data = {}
filenames = sys.argv[1:]
for filename in filenames:
    t = open(filename).read().decode('utf-8')
    data[filename] = t

for filename, text in data.items():
    v = nlp.TextVectorizer.TfVectorizer(tokenizer=nlp.tokenizer.tokenizeJp, texts=text)
    tf = v.vectorize()

    output = './output/' + os.path.basename(filename) + '.tf'
    save(output, tf)
