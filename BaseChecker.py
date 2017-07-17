from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime

class BaseChecker(object):
    
    mText = ''
    mTitle = ''
    mDataframe = None
    
    def __init__(self):
        self
            
    def setText(self, text):
        if self.mText != '':
            self.mText += '\n'
        self.mText += text
        
    def makeDataFrame(self):
        data = []
        rowArr = self.mText.split('\n')
        for row in rowArr:
            colArr = row.split('\t')
            colArr[0] = datetime.fromtimestamp(float(colArr[0]))
            data.append(colArr)
        return data
            
    def getGroupbyData(self):
        return self.mDataframe.groupby('Label').size()
    
    def checkData(self):
        return self
        
    def checkDataPattern(self):
        return self
        
    def getTitle(self):
        return self.mTitle