#!/usr/bin/env python
# -*- coding: utf-8 -*-

def term_frequency(term_list):
    tf = {}
    for t in term_list:
        if not tf.has_key(t):
            tf[t] = 0
        tf[t] += 1
    return tf

if __name__ == '__main__':
    text = u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。スクリーン・エディタとしての人気が高く、特にUNIXのプログラマを中心としたコンピュータ技術者に愛用者が多い。'

    import tokenizer
    tokens = tokenizer.tokenize(text.encode('utf-8'))
    terms = map(lambda t: t.basic_form, tokens)

    tf = term_frequency(terms)
    for t, f in tf.items():
        print t.encode('utf-8'), f
