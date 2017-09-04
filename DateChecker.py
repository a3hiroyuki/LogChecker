
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import margins
from datetime import datetime
from DataFrameUtil import DataFrameUtil

class DateChecker(BaseChecker):

    columnArr = ['DATE', 'kw', 'MONTH', 'INDEX']
    dtypes = {'INDEX' : int, 'DATE' : datetime}
    
    free_wifi_name_list = ['11', '22', '33']
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'DATE'
        self.filter_str = ''
        for wifi_str in self.free_wifi_name_list:
            self.filter_str += '^%s|' %  wifi_str
        self.filter_str = self.filter_str[:-1]
        print (self.filter_str)

    #Override
    def parseRecord(self, data, row):
        colArr = row.split(',')
        colResultArr = []
        colResultArr.append(datetime.strptime(colArr[0] + ' ' +  colArr[1], '%Y/%m/%d %H:%M'))
        colResultArr.append(colArr[2])
        colResultArr.append(colResultArr[0].strftime("%Y-%m"))
        colResultArr.append(1)
        data.append(colResultArr)
        
        
    def getCalcDataDictPerDay(self, how='sum'):
        dateframe_dict_per_day = DataFrameUtil.getDataframeDictPerDay(self.mDataframe)
        calc_data_dict_per_day = {key : value['INDEX'].resample('2H', how=how) 
                                  for key, value in dateframe_dict_per_day.items() }
        return calc_data_dict_per_day
        
    def checkDataPattern(self):
        self
              
    def getGroupbyData(self):
        df = self.getDataframe()
        date_groupby_df = df.groupby('DATE').size()
        print ('スキャン回数:' + str(len(date_groupby_df)))
        #wifi数のチェック
        wifi_filtered_df = df[df['kw'].str.contains(self.filter_str)]
        drop_df = wifi_filtered_df.drop_duplicates(['kw'])
        print ('AP種類数:' + str(len(drop_df.index)))
        date_groupby_df = drop_df.groupby('DATE').size()
        print ('AP取得時のスキャン回数:' + str(len(date_groupby_df)))
        return df
    
        
        