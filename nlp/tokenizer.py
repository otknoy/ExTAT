#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab
import re

def tokenizeEn(text):
    tokens = text.split(' ')
    # remove symbols
    tokens = map(lambda t: re.sub(r'[",.]', '', t), tokens)
    return tokens

def tokenizeJp(text):
    mecab = MeCab.Tagger('-Ochasen')
    node = mecab.parseToNode(text)
    tokens = []
    while node:
        surface = node.surface.decode('utf-8')
        basic_form = node.feature.split(',')[6].decode('utf-8')
        if basic_form == '*':
            basic_form = surface

        is_not_noun = not node.posid in range(38, 47+1)
        is_symbol = re.compile(r'^[!"#\$\%\&\'\(\)\*\+,\-\./:;\<\=\>\?\@\[\\\]\^\_\`\{\}\~\|]+$').search(basic_form)
        if any([is_not_noun, is_symbol]):
            node = node.next
            continue

        tokens.append(basic_form)

        node = node.next

    return tokens[1:-1]

# default
tokenize = tokenizeJp

if __name__ == '__main__':
    jp_text = u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。スクリーン・エディタとしての人気が高く、特にUNIXのプログラマを中心としたコンピュータ技術者に愛用者が多い。'
    en_text = u'Emacs and its derivatives are a family of text editors that are characterized by their extensibility. The manual for the most widely-used variant, GNU Emacs, describes it as "the extensible, customizable, self-documenting, real-time display editor".'
    
    tokens = tokenizeJp(jp_text.encode('utf-8'))
    print '|'.join(tokens)

    tokens = tokenizeEn(en_text.encode('utf-8'))
    print '|'.join(tokens)
