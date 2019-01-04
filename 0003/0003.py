# -*- coding:utf-8 -*-

import os.path
import sys
import redis

if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    keyfile = os.path.dirname(dirname) + os.sep + '0001' + os.sep + 'outfile.txt'
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    with open(keyfile, 'r') as f:
        for line in f:
            if line:
                r.sadd('keyvalue',line[0:-1])
    for i in r.smembers('keyvalue'):
        print(i)
    pool.disconnect()
