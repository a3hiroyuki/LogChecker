# -*- coding: utf-8 -*-
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pandas
import os
import re

#自作クラス
from NetworkChecker import NETWORKChecker
from  ConnectionChecker import CONNECTIONChecker
from DateChecker import DateChecker

path =  "tsv\\"

def getAllFileDataInDir(checker_map, dir_name):
    mod =__import__("Main")
    print mod
    pattern = r"AAA_" + dir_name + "*"
    files = os.listdir(path + dir_name)
    for file in files:
        matchObj = re.match(pattern , file)
        if matchObj != None:
            if checker_map.get(dir_name) == None:
                class_name = dir_name + 'Checker'
                class_def = getattr(mod, class_name)
                checker_map[dir_name] = class_def()
            f = open(path + dir_name + "\\" + file, 'r')
            readText = f.read()
            checker_map.get(dir_name).setText(readText)

if __name__ == '__main__':
    
    checker_map = {}
    dir_list = []
    
    #フォルダの読み込み
    dirs = os.listdir(path)  
    for item in dirs:
        if os.path.isdir(path + item):
            dir_list.append(item)
        
    for dir_name in dir_list:
        try:
            getAllFileDataInDir(checker_map, dir_name)
        except TypeError:
            print 'error'
        except StandardError:
            print 'standardError'
 
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
        if data != "":
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
        
    
    
    