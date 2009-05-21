#!/usr/bin/env python
# -*- coding: utf-8 -*-

# start and end markers
format = u'\u169B%s\u169C'

chars = {
    ' ': u'\u1680',

    'b': u'\u1681',
    'l': u'\u1682',
    'f': u'\u1683',
    's': u'\u1684',
    'n': u'\u1685',

    'h': u'\u1686',
    'd': u'\u1687',
    't': u'\u1688',
    'c': u'\u1689',
    'q': u'\u168A',

    'm': u'\u168B',
    'g': u'\u168C',
    'z': u'\u168E',
    'r': u'\u168F',

    'x': u'\u1699',     # ch/x/ae
    'p': u'\u169A',

    'a': u'\u1690',
    'o': u'\u1691',
    'u': u'\u1692',
    'e': u'\u1693',
    'i': u'\u1694',

    u'á': u'\u1690',
    u'ó': u'\u1691',
    u'ú': u'\u1692',
    u'é': u'\u1693',
    u'í': u'\u1694',
}

pairs = {
    'ch': u'\u1699',    # ch/x/ae
    'ng': u'\u168D',

    'ea': u'\u1695',
    'oi': u'\u1696',
    'ui': u'\u1697',
    'io': u'\u1698',
    'ae': u'\u1699',    # ch/x/ae
}

def normalise(text):
    return ''.join(filter(lambda c: c in chars, text.lower()))

def ogham(text):
    s = normalise(text)
    for pair, char in pairs.items():
        s = s.replace(pair, char)
    s = map(lambda c: chars.get(c, c), s)
    return format % ''.join(s)

def test(text):
    print normalise(text)
    print ogham(text)
