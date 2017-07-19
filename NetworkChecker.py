
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

class NetworkChecker(BaseChecker):
    
    columnArr = ['Date', 'Label', 'fff']
    dtypes = {'Label': int, 'fff': int}
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'NETWORK'
            
    def makeDataFrame(self):
        self.mDataframe = DataFrame(BaseChecker.makeDataFrame(self), columns=self.columnArr)
        for k, v in self.dtypes.items():
            self.mDataframe[k] = self.mDataframe[k].astype(v)
        print self.mDataframe
        
    def checkData(self):
        BaseChecker.checkData(self)
        fig, axe = plt.subplots(1,3)
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 1)
        self.saveFile(filtered_data, '1')
        self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[0])
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 2)
        self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[1])
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 3)
        #self.plotGroupedDataFrame(df = data, groupby_column='fff', axe=axe[2])
        self.plotCutDataFrame(df=filtered_data, cut_column='fff', cut_num=20, axe=axe[2])
        
    def checkDataPattern(self):
        fig, axe = plt.subplots(1,2)
        self.plotTimelineDataFrame(plot_column='fff', axe=axe[0])
        
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == 3)
        self.plotDownsamplingTimelineDataFrame(df = filtered_data, plot_column='fff', time_slice='4S', how='sum', axe=axe[0])
        
        self.plotDownsamplingTimelineDataFrame(df = filtered_data, plot_column='fff', time_slice='4S', how='mean', axe=axe[1])
    
        
        