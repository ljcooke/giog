"""
Ogham script

"""

# start and end markers
FORMAT_STR = '\u169B%s\u169C'

CHARS = {
    ' ': '\u1680',

    'b': '\u1681',
    'l': '\u1682',
    'f': '\u1683',
    's': '\u1684',
    'n': '\u1685',

    'h': '\u1686',
    'd': '\u1687',
    't': '\u1688',
    'c': '\u1689',
    'q': '\u168A',

    'm': '\u168B',
    'g': '\u168C',
    'z': '\u168E',
    'r': '\u168F',

    'x': '\u1699',     # ch/x/ae
    'p': '\u169A',

    'a': '\u1690',
    'o': '\u1691',
    'u': '\u1692',
    'e': '\u1693',
    'i': '\u1694',

    'á': u'\u1690',
    'ó': u'\u1691',
    'ú': u'\u1692',
    'é': u'\u1693',
    'í': u'\u1694',
}

pairs = {
    'ch': '\u1699',    # ch/x/ae
    'ng': '\u168D',

    'ea': '\u1695',
    'oi': '\u1696',
    'ui': '\u1697',
    'io': '\u1698',
    'ae': '\u1699',    # ch/x/ae
}


def normalise(text):
    return ''.join(filter(lambda c: c in CHARS, text.lower()))


def ogham(text):
    s = normalise(text)
    for pair, char in pairs.items():
        s = s.replace(pair, char)
    s = map(lambda c: CHARS.get(c, c), s)
    return FORMAT_STR % ''.join(s)


def test(text):
    print(normalise(text))
    print(ogham(text))
