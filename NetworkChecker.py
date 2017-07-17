
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

class NetworkChecker(BaseChecker):
    
    columnArr = ['Date', 'Label', 'fff']
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'NETWORK'
            
    def makeDataFrame(self):
        self.mDataframe = DataFrame(BaseChecker.makeDataFrame(self), columns=self.columnArr)
        print self.mDataframe
        
    def checkData(self):
        BaseChecker.checkData(self)
        fig, axe = plt.subplots(1,3)
        
        filter1 = self.mDataframe['Label'] == '1'
        data = self.mDataframe[filter1]
        data1 = data.groupby('fff').size()
        data1.sort()
        data1.plot(kind='bar', ax=axe[0])
        
        filter2 = self.mDataframe['Label'] == '2'
        data2 = self.mDataframe[filter2].groupby('fff').size()
        data2.sort()
        data2.plot(kind='bar', ax=axe[1])
        
        filter3 = self.mDataframe['Label'] == '3'
        data3 = self.mDataframe[filter3].groupby('fff').size()
        data3.sort()
        data3.plot(kind='bar', ax=axe[2])
        
    def checkDataPattern(self):
        fig, axe = plt.subplots(1,2)
        BaseChecker.checkDataPattern(self)
        #trend = Series(self.mDataframe['fff'] , index=self.mDataframe['Date'])
        #print self.mDataframe['fff']
        frame2 = self.mDataframe.set_index(self.mDataframe['Date'])
        print frame2
        frame2['Label'] = frame2['Label'].astype(float)
        #print frame2['Label']
        frame2['Label'].plot(ax=axe[0])
        
        