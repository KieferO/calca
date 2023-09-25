#!/usr/bin/env python3

from __future__ import print_function

import sys

class Evaler(object):
    def __init__(self):
        self.functs = [str, eval, float, int]

    def __call__(self, inval):
        while True:
            try:
                return self.functs[-1](inval)
            except:
                self.functs.pop()

def seq_eval(infile):
    inner = Evaler()
    for line in infile:
        line = line.strip()
        if not line:
            continue
        yield tuple( inner(tok) for tok in line.split(',') )

def file_eval(infile):
    inner = Evaler()
    for line in infile:
        line = line.strip()
        if not line:
            continue
        yield inner(line)

def writeval(outtuple):
    if hasattr(outtuple, '__iter__'):
        print(','.join([ str(v) for v in outtuple ]))
    else:
        print(outtuple)

def main():
    print(zip(*seq_eval(sys.stdin)))
    return 0

if __name__ == '__main__':
    sys.exit(main())

