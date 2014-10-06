#!/usr/bin/env python
# -*- coding: utf-8 -*-

def term_frequency(term_list):
    tf = {}
    for t in term_list:
        if not tf.has_key(t):
            tf[t] = 0
        tf[t] += 1
    return tf

def document_frequency(texts):
    df = {}
    for terms in texts:
        for t in list(set(terms)):
            if not df.has_key(t):
                df[t] = 0
            df[t] += 1
    return df


if __name__ == '__main__':
    texts = [u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。スクリーン・エディタとしての人気が高く、特にUNIXのプログラマを中心としたコンピュータ技術者に愛用者が多い。',
             u'vi（ヴィーアイ）は、Emacsと共にUNIX環境で人気があるテキストエディタ。ビル・ジョイによって開発された。名の由来はVIsual editorないしVisual Interfaceとされる[1][2]。後発のUnix系OSに搭載されているviは、上位互換のVimやnviであることが多い（viコマンドでvimやnviが起動する）。']

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
    print '{' + ', '.join(["'%s': %d" % (d, f) for d, f in df.items()]) + '}'
