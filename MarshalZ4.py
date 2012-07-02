'''
Created on Jun 2, 2012

@author: Saber
'''
import marshal as _marshal
NONE = 'N'
TRUE = 'T'
FALSE = 'F'
INT32 = 'i'
INT64 = 'I'
LONG = 'l'
FLOAT = 'f'
BINARY_FLOAT = 'g'
STRINGREF = 'R'
UNICODE = 'u'
STRING = 's'
INTERNED = 't'
LIST = '['
TUPLE = '('
SET = '<'
FROZEN_SET = '>'
DICT = '{'
DICT_CLOSE = '0'
PAD = '_'
def verify_string(self,s_='',length=0):
    s = s_
    eof = s+length
    nstrings = 0
    i = 0
    v = 0
    m = 0
    while s < eof:
        if s[0] == INT32:
            s += 5
            continue

        if s[0] in (INT64, BINARY_FLOAT):
            s += 9
            continue

        if s[0] == LONG:
            if s + 5 > eof:
                return 0

            m = 1
            v = 0
            for i in range(1, 5):
                v += m * s[i]
                m *= 256

            s += 5 + v * 2
            continue

        if s[0] in (NONE, TRUE, FALSE):
            s += 1
            continue

        if s[0] == FLOAT:
            if s + 2 > eof:
                return 0

            s += 2 + s[1]
            continue

        if s[0] in (UNICODE, STRING, INTERNED):
            if s + 5 > eof:
                return 0

            if s[0] == INTERNED:
                nstrings += 1

            m = 1
            v = 0
            for i in range(1, 5):
                v += m * s[i]
                m *= 256

            s += 5 + v
            continue

        if s[0] == STRINGREF:
            if s + 5 > eof:
                return 0

            m = 1
            v = 0
            for i in range(1, 5):
                v += m * s[i]
                m *= 256

            # String reference to non-existing string.
            if v >= nstrings:
                return 0

            s += 5
            continue

        if s[0] in (LIST, TUPLE, SET, FROZEN_SET):
            s += 5
            continue

        if s[0] in (DICT, DICT_CLOSE):
            s += 1
            continue

        if s[0] == PAD:
            s += 1
            while s < eof and s[0] == PAD:
                s += 1
            return s == eof

        return 0

    if s > eof:
        return 0

    return 1
def loads(s):
    if verify_string(s, len(s)) == 0:
        raise ValueError('bad marshal data')

    return _marshal.loads(s)

def dumps(expr):
    s = _marshal.dumps(expr, 1)
    if verify_string(s, len(s)) == 0:
        raise ValueError('unsupported marshal data')

    return s
def load(f):
    '''load data from file'''
    return loads(f.read())
def dump(s,f):
    '''dump data to file'''
    f.write(dumps(s))