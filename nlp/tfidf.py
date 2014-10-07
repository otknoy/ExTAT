#!/usr/bin/env python
# -*- coding: utf-8 -*-

def term_frequency(terms):
    tf = {}
    for t in terms:
        if not tf.has_key(t):
            tf[t] = 0
        tf[t] += 1
    return tf

def document_frequency(texts):
    from itertools import chain
    all_terms = list(chain.from_iterable(texts)) # flatten
    df = {}
    for t in all_terms:
        df[t] = [t in text for text in texts].count(True)
    return df

def inverse_document_frequency(texts):
    df = document_frequency(texts)
    idf = {}
    for t in df.keys():
        idf[t] = 1.0/df[t]
    return idf


if __name__ == '__main__':
    texts = [u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。',
             u'vi（ヴィーアイ）は、Emacsと共にUNIX環境で人気があるテキストエディタ。',
             u'nanoは、UNIXを中心としたシステムで使われる、cursesを使ったテキストエディタの一種である。']

    import tokenizer

    print 'tokenize'
    docs = []
    for t in texts:
        tokens = tokenizer.tokenize(t.encode('utf-8'))
        terms = map(lambda t: t.basic_form, tokens)
        docs.append(terms)
        print '|'.join(terms)

    print '\ntf'
    for d in docs:
        tf = term_frequency(d)
        print '{' + ', '.join(["'%s': %d" % (t, f) for t, f in tf.items()]) + '}'

    print '\ndf'
    df = document_frequency(docs)
    print '{' + ', '.join(["'%s': %d" % (t, v) for t, v in df.items()]) + '}'

    print '\nidf'
    idf = inverse_document_frequency(docs)
    print '{' + ', '.join(["'%s': %f" % (t, v) for t, v in idf.items()]) + '}'
