from pandas import Series, DataFrame
import pandas as pd

class BaseChecker(object):
    
    mText = ''
    df = None

    def __init__(self):
        self
            
    def setText(self, text):
        if self.mText != '':
            self.mText += '\n'
        self.mText += text
        
    def printA(self):
        print(self.mText)
        
    def makeDataFrame(self):
        data = []
        rowArr = self.mText.split('\n')
        for row in rowArr:
            colArr = row.split('\t')
            data.append(colArr)
        return data
            
    def getGroupbyData(self):
        return self.df.groupby('fff').size()
            
            
            