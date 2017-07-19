from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime
import os

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
        data.sort(ascending=False)
        data.plot(kind='bar', ax=axe)
        
    def plotCutDataFrame(self, df, cut_column, cut_num, axe):
        factor = pd.cut(df[cut_column], cut_num)
        data = df[cut_column].groupby(factor).size()
        data.plot(kind='bar', ax=axe)
        
    def plotTimelineDataFrame(self, plot_column, axe):
        frame = self.mDataframe.set_index(self.mDataframe['Date'])
        frame[plot_column].plot(ax=axe)
        
    def plotDownsamplingTimelineDataFrame(self, df, plot_column, time_slice, how, axe):
        frame = df.set_index(df['Date'])
        frame2 =  frame[plot_column].resample(time_slice, how)
        print frame2
        frame2.plot(kind='bar', ax=axe)
        
    def saveFile(self, df, item_name):
        dir_path =  "tsv\\" + self.mTitle + '1'
        if os.path.isdir(dir_path) == False:
            os.mkdir(dir_path)    
        df.to_csv(dir_path + '\\' + item_name + '.txt')

        
        