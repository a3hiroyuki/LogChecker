
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

class NetworkChecker(BaseChecker):
    
    columnArr = ['Date', 'Label', 'fff']
    dtypes = {'Label': int, 'fff': int}
    check_flg = {1 : False, 2 : True, 2 : False}
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'NETWORK'
        
    def checkData(self):
        BaseChecker.checkData(self)
        fig, axe = plt.subplots(1,3)
        
        if self.check_flg[1] == True:
            filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 1)
            self.saveFile(filtered_data, '1')
            self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[0])
        
        if self.check_flg[2] == True:
            filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 2)
            self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[1])
        
        if self.check_flg[1] == True:
            filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 3)
            #self.plotGroupedDataFrame(df = data, groupby_column='fff', axe=axe[2])
            self.plotCutDataFrame(df=filtered_data, cut_column='fff', cut_num=20, axe=axe[2])
        
    def checkDataPattern(self):
        fig= plt.figure()
        ax = fig.add_subplot(1,1,1)
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 3)
        self.plotDownsamplingTimelineDataFrame(df = filtered_data, plot_column='fff', time_slice='4S', how='sum', axe=ax)
        
    
        
        