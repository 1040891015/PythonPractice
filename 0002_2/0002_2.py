# -*- coding:utf-8 -*-

import os.path
import sys
import pymongo

if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    keyfile = os.path.dirname(dirname) + os.sep + '0001' + os.sep + 'outfile.txt'
    conn = pymongo.MongoClient('mongodb://localhost:27017/')
    db = conn.test
    testkey = db.testkey
    testkey.remove()
    with open(keyfile, 'r') as f:
        for line in f:
            if line:
                testkey.insert({'keyvalue':line[0:-1]})
    for i in testkey.find():
        print(i)