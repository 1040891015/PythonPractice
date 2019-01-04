# -*- coding:utf-8 -*-

import os.path
import sys
from hashlib import sha1
import time

def sha1_encode(str_0):
    psw = sha1()
    psw.update(str_0.encode('utf-8'))
    str_1 = psw.hexdigest()
    return str_1

if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    outfile = dirname + os.sep + 'outfile.txt'
    with open(outfile, 'a') as f:
        for i in range(200):
            str_src = 'hobot.cc' + str(int(time.time())) + str(i).zfill(3)
            str_end = sha1_encode(str_src)[0:15]
            print(str_end)
            f.write(str_end + '\n')