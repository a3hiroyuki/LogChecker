
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import margins
from datetime import datetime
from DataFrameUtil import DataFrameUtil

class DateChecker(BaseChecker):

    columnArr = ['DATE', 'kw', 'MONTH', 'INDEX']
    dtypes = {'kw': int, 'INDEX' : int}
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'DATE'

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
        #print (calc_data_dict_per_day)
        return calc_data_dict_per_day
        
    def checkDataPattern(self):
        self
              
    def getGroupbyData(self):
        return None
    
        
        