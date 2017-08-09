
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import margins
from datetime import datetime

class DateChecker(BaseChecker):

    columnArr = ['DATE', 'kw', 'MONTH', 'INDEX']
    dtypes = {'kw': int, 'DATE' : DataFrame}
        
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
        colResultArr = []
        colResultArr.append(datetime.strptime(colArr[0] + ' ' +  colArr[1], '%Y/%m/%d %H:%M'))
        colResultArr.append(colArr[2])
        colResultArr.append(colResultArr[0].strftime("%Y-%m"))
        colResultArr.append(1)
        data.append(colResultArr)
        
    def getDataframeListPerDay(self):
        df = self.mDataframe.set_index(self.mDataframe['DATE'])
        df2 = df.groupby(pd.TimeGrouper(freq='1D')).size()
        date_list = df2.index.tolist()
        dateframe_list_per_day = []
        for date in date_list:
            dateframe_list_per_day.append(df[(df.index - date).days == 0])
        return dateframe_list_per_day
        '''
        for dateframe in day_dateframe_list:
            print dateframe
        '''
        
        
    def checkData(self):
        dateframe_list_per_day = self.getDataframeListPerDay()
        
        fig, axe = plt.subplots(1,4)
        for i, dataframe_per_day in enumerate(dateframe_list_per_day):
            if i < 4:
                data =  dataframe_per_day['INDEX'].resample('1H', how='sum')
                #data2 = pd.merge(frame, frame4, left_index=True, right_index=True)
                #data = df.groupby('DATE')['kw'].mean()
                data.plot(kind='bar', ax=axe[i])
        
        
    def checkDataPattern(self):
        self
              
    def getGroupbyData(self):
        return None
    
        
        