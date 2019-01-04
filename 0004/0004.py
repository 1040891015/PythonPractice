# -*- coding:utf-8 -*-

import os.path
import sys
import re


if __name__ == '__main__':
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    filename = dirname + os.sep + 'news.txt'
    with open(filename) as f:
        sum = 0
        for line in f:
            word_count = re.findall('[A-Za-z0-9\']+', line).__len__()
            sum += word_count
    print(sum)