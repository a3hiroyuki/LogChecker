
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import margins

class DateChecker(BaseChecker):

    columnArr = ['DATE', 'Time', 'kw', 'MONTH']
    dtypes = {'kw': int}
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'DATE'
            
    def makeDataFrame(self):
        self.mDataframe = DataFrame(BaseChecker.makeDataFrame(self), columns=self.columnArr)
        for k, v in self.dtypes.items():
            self.mDataframe[k] = self.mDataframe[k].astype(v)
            
    #Override
    def parseRecord(self, data, row):
        colArr = row.split(',')
        colArr[0] = pd.to_datetime(colArr[0])
        colArr.append(colArr[0].strftime("%Y-%m"))
        data.append(colArr)
        
        
    def checkData(self):
        df = self.mDataframe.set_index(self.mDataframe['DATE'])
        print df
        data =  df['kw'].resample('1M', how='sum')
        #data2 = pd.merge(frame, frame4, left_index=True, right_index=True)
        #print self.mDataframe.pivot_table('kw', rows='DATE', margins=True, cols='Time')
        #data = df.groupby('DATE')['kw'].mean()
        fig= plt.figure()
        ax = fig.add_subplot(1,1,1)
        data.plot(kind='bar', ax=ax)
        
    def checkDataPattern(self):
        self
        
    
        
    def getGroupbyData(self):
        return ""
    
        
        