#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import utils

class Vectorizer:
    def __init__(self, tokenizer, texts):
        self.tokenizer = tokenizer
        self.texts = texts

class TfVectorizer(Vectorizer):
    def vectorize(self):
        docs = [self.tokenizer(t.encode('utf-8')) for t in self.texts]
        return [utils.term_frequency(d, normalize=False) for d in docs]

class TfidfVectorizer(Vectorizer):
    def vectorize(self):
        docs = [self.tokenizer(t.encode('utf-8')) for t in self.texts]
        return utils.tf_idf(docs, normalize=True)


if __name__ == '__main__':
    texts = [u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。',
             u'vi（ヴィーアイ）は、Emacsと共にUNIX環境で人気があるテキストエディタ。',
             u'nanoは、UNIXを中心としたシステムで使われる、cursesを使ったテキストエディタの一種である。']

    import tokenizer

    print 'TF'
    v = TfVectorizer(tokenizer=tokenizer.tokenizeJp, texts=texts)
    tf_list = v.vectorize()
    for i in range(len(tf_list)):
        tf = tf_list[i]
        ranking = sorted(tf.items(), key=lambda x:-x[1])[:10]
        print "[%d]" % (i+1), ', '.join(map(lambda e: "%s: %.2f" % e, ranking))

    print 

    print 'TFIDF'
    v = TfidfVectorizer(tokenizer=tokenizer.tokenizeJp, texts=texts)
    tfidf_list = v.vectorize()
    for i in range(len(tfidf_list)):
        tfidf = tfidf_list[i]
        ranking = sorted(tfidf.items(), key=lambda x:-x[1])[:10]
        print "[%d]" % (i+1), ', '.join(map(lambda e: "%s: %.2f" % e, ranking))
