#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

def unicode_normalize(text):
    return unicodedata.normalize('NFKC', text)

if __name__ == '__main__':
    s = u'Emacs（ｲｰﾏｯｸｽ）とは高機能でカスタマイズ性の高いテキストエディタである。'

    print s
    print unicode_normalize(s)
