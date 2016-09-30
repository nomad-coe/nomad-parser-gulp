#!/usr/bin/env python
from __future__ import print_function
from glob import glob
import re
from optparse import OptionParser
from subprocess import Popen, PIPE
import os

p = OptionParser()
opts, args = p.parse_args()

if len(args) == 0:
    testfiles = glob('test/outputs/example*.got')
    testfiles.sort()

    #tests = {}

    #testfiles.sort()
    #print(testfiles)

    #pat = re.compile('test/outputs/example(\d+)[ab]?.got')

    #for fname in testfiles:
    #    print(fname, pat.match(fname))
    #testfiles.sort(key=lambda fname:
    #               int(pat.match(fname).group(1)))
    #for f in testfiles:
    #    print(f)
else:
    testfiles = argv

for testfile in testfiles:
    dirname, basename = os.path.split(testfile)
    print(basename)
    args = 'python main.py --annotate'.split()
    args.append(testfile)
    proc = Popen(args, stdout=PIPE)
    txt = proc.stdout.read()
    with open('%s.json' % testfile, 'w') as fd:
        fd.write(txt)
