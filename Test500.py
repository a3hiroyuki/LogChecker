# -*- coding: utf-8 -*-


import numpy
import matplotlib
import matplotlib.pyplot as plt
import pandas
import os
import re
from NetworkChecker import NetworkChecker
from  ConnectionChecker import ConnectionChecker


if __name__ == '__main__':
    
    path = "C:\\workspace\\python1\\Test500\\src\\tsv\\"
    
    files = os.listdir(path)
    
    checker_map = {}
    
    pattern = r"\AAAA_[A-Z]*"
 
    for file in files:
        matchObj = re.match(pattern , file)
        if matchObj != None:
            strNum =  matchObj.end()
            str = file[:strNum]
            if checker_map.get(str) == None:
                if str == 'AAA_NETWORK':
                    checker_map[str] = NetworkChecker()
                elif str == 'AAA_CONNECTION':
                    checker_map[str] = ConnectionChecker()
                else:
                    continue
            f = open(path + file, 'r')
            checker_map.get(str).setText(f.read())
            
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.makeDataFrame()
        
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.makeDataFrame()
        
    fig, axe = plt.subplots(1,2)
    count = 0
    for key in checker_map.keys():
        checker = checker_map.get(key)
        data = checker.getGroupbyData()
        data.plot(kind='bar', ax=axe[count])
        count = count + 1
    plt.show()
    
    
    