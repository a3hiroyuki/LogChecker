# -*- coding: utf-8 -*-
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pandas
import os
import re

#自作クラス
from NetworkChecker import NetworkChecker
from  ConnectionChecker import ConnectionChecker


if __name__ == '__main__':
    
    path = "C:\\workspace\\python1\\Test500\\src\\tsv\\"
    
    files = os.listdir(path)
    checker_map = {}
    pattern = r"AAA_[A-Z]*"
 
    #データの読出し
    for file in files:
        matchObj = re.match(pattern , file)
        if matchObj != None:
            strNum =  matchObj.end()
            title = file[:strNum]
            if checker_map.get(title) == None:
                if title == 'AAA_NETWORK':
                    checker_map[title] = NetworkChecker()
                elif title == 'AAA_CONNECTION':
                    checker_map[title] = ConnectionChecker()
                else:
                    continue
            f = open(path + file, 'r')
            readText = f.read()
            checker_map.get(title).setText(readText)
    
    #データフレームの生成
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.makeDataFrame()
            
    #全体の確認
    fig, axe = plt.subplots(1,2)
    count = 0
    for key in checker_map.keys():
        checker = checker_map.get(key)
        data = checker.getGroupbyData()
        axis = axe[count]
        axis.set_title(checker.getTitle())
        data.plot(kind='bar', ax=axis)
        count = count + 1
    
    #データの分布の確認
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.checkData()
        
    #データの分布の確認
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.checkDataPattern()
        
    plt.show()
        
    
    
    