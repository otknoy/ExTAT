#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import MeCab

class Token:
    def __init__(self, surface, basic_form, part_of_speech_id):
        self.surface = surface
        self.basic_form = basic_form
        self.part_of_speech_id = part_of_speech_id

    def __str__(self):
        s = '%s-%s-%d' % (self.surface, self.basic_form, self.part_of_speech_id)
        return s.encode('utf-8')

def tokenize(text):
    mecab = MeCab.Tagger('-Ochasen')
    node = mecab.parseToNode(text)
    tokens = []
    while node:
        surface = node.surface.decode('utf-8')
        basic_form = node.feature.split(',')[6].decode('utf-8')
        if basic_form == '*':
            basic_form = surface
            
        token = Token(surface, basic_form, node.posid)
        tokens.append(token)
        
        node = node.next
        
    return tokens[1:-1]

    
if __name__ == '__main__':
    text = u'Emacs（イーマックス）とは高機能でカスタマイズ性の高いテキストエディタである。スクリーン・エディタとしての人気が高く、特にUNIXのプログラマを中心としたコンピュータ技術者に愛用者が多い。'

    terms = tokenize(text.encode('utf-8'))

    for t in terms:
        print t
