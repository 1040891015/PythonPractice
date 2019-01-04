# -*- coding:utf-8 -*-
import csv
import sys
from matplotlib.pylab import *




if __name__ == "__main__":
    filename = 'D:/workspace/001Project_Feitian/Cases/hongkou/result/iot-iot-.csv'
    RES = []
    time = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            RES.append(int(row[' RES'].strip()))
            time.append(int(row['record_time'].strip()))
        # print(RES)
        # print(time)
    figure()
    subplot(2,3,1)
    plot(time,RES)
    show()