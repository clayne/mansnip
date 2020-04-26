#!/usr/bin/env python3
import os
import sys
import re
import tempfile
import subprocess
import json

os.environ['MANWIDTH'] = '250'
tempdir = None
def params_to_fname(params):
    return re.sub(' ', '_', params) + ".test"

def store_results(path, expected, actual):
    global tempdir
    if not tempdir:
        tempdir = tempfile.mkdtemp()
        print("Using {} for failures".format(tempdir))

    with open("{}/{}-expected".format(tempdir,path), 'w') as f:
        f.write(expected)

    with open("{}/{}-actual".format(tempdir,path), 'w') as f:
        f.write(actual)

if len(sys.argv) > 1:
    print("making test for arguments")
    args = sys.argv[1:]
    fname = params_to_fname(' '.join(args))

    if os.path.exists(fname):
        print("I'm not going to overwrite {}. Please remove it then rerun this.".format(fname))
        sys.exit(-1)

    with open('testlist.txt', 'a') as f:
        f.write(json.dumps(args) + "\n")

    with open(fname, 'w') as f:
        print("Creating {}".format(fname))

        p = subprocess.Popen(['../mansnip'] + args, stdout=subprocess.PIPE)
        res = p.communicate()[0].decode("utf-8")

        print(res) 
        f.write(res)
        sys.exit(0)

with open('testlist.txt', 'r') as f:
    testList = f.read().splitlines()

    for testraw in testList:
        testList = json.loads(testraw)
        test = ' '.join(testList)

        if test == 'stop':
            print("asked to stop")
            sys.exit(0)

        if test[0] == '#':
            print("skipping {}".format(test))
            continue

        fname = params_to_fname(test)

        with open(fname, 'r') as f:
            expected = f.read()

        p = subprocess.Popen(['../mansnip'] + testList, stdout=subprocess.PIPE)
        actual = p.communicate()[0].decode("utf-8")

        if actual == expected:
            print("PASSED " + test)
        else:
            print("!! FAILED " + test)
            store_results(fname, expected, actual)


