#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp.tokenizer
import nlp.TextVectorizer

import sys

data = []
filenames = sys.argv[1:]
for filename in filenames:
    t = open(filename).read().decode('utf-8')
    data.append(t)

data = "\n".join(data)

print 'word,count'
v = nlp.TextVectorizer.TfVectorizer(tokenizer=nlp.tokenizer.tokenizeJp, texts=data)
tf = v.vectorize()
for t, f in sorted(tf.items(), key=lambda x:-x[1]):
    print "%s,%d" % (t.encode('utf-8'), f)
