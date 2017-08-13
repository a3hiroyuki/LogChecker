'''
Created on 2017/08/11

@author: abe
'''
import os
import re
from NetworkChecker import NetworkChecker
from DateChecker import DateChecker

class CheckerFactory:
    @classmethod
    def create_checker(Class, kind):
        class_name = {'NETWORK' : 'NetworkChecker', 
                      'DATE' : 'DateChecker'}[kind]
        return globals()[class_name]()

class CheckerManager:
    
    _checker_dict = {}
    
    def __init__(self):
        self
        
    def makeDataFrameFromDataInDir(self, path, dir_name, file_name):
        checker = CheckerFactory.create_checker(dir_name)
        print (checker)
        pattern = r'' + file_name
        for found_file_name in os.listdir(path + dir_name):
            if re.match(pattern , found_file_name) is not None:
                with open(path + dir_name + "\\" + found_file_name, 'r') as f:
                    read_text = f.read()
                    checker.makeDataFrame(read_text)
                    self._checker_dict[dir_name] = checker
                    return

    def getDataFrameDict(self):
        dataframe_dict = {key : value.getDataFrame() 
                          for key, value in self._checker_dict.items() }
        return dataframe_dict
    
    def getGroupByFrameDict(self):
        groupby_frame_dict = {key : value.getGroupbyData() 
                              for key, value in self._checker_dict.items() 
                              if value.getGroupbyData() is not None}
        return groupby_frame_dict
    
    def getDataFrame(self, name):
        return self._checker_dict[name]
    
    
            

        