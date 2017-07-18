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
    
    def getFilteredDataFrame(self, filter_criteria):
        return self.mDataframe[filter_criteria]
    
    def plotGroupedDataFrame(self, df, groupby_column, axe):
        data = df.groupby(groupby_column).size()
        data.plot(kind='bar', ax=axe)
        
    def plotCutDataFrame(self, df, cut_column, cut_num, axe):
        df[cut_column] = df[cut_column].astype(int)
        factor = pd.cut(df[cut_column], cut_num)
        data = df[cut_column].groupby(factor).size()
        data.plot(kind='bar', ax=axe)
        
    def plotTimelineDataFrame(self, plot_column, axe):
        frame = self.mDataframe.set_index(self.mDataframe['Date'])
        frame[plot_column] = frame[plot_column].astype(float)
        frame[plot_column].plot(ax=axe)
        
    def plotDownsamplingTimelineDataFrame(self):
        frame = self.mDataframe.set_index(self.mDataframe['Date'])
        data = frame['fff'].astype(int)
        print data
        print data.resample('S').mean()
        