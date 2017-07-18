
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
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == '1')
        self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[0])
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == '2')
        self.plotGroupedDataFrame(df = filtered_data, groupby_column='fff', axe=axe[1])
        
        filtered_data = self.getFilteredDataFrame(filter_criteria = self.mDataframe['Label'] == '3')
        #self.plotGroupedDataFrame(df = data, groupby_column='fff', axe=axe[2])
        self.plotCutDataFrame(df=filtered_data, cut_column='fff', cut_num=20, axe=axe[2])
        
    def checkDataPattern(self):
        fig, axe = plt.subplots(1,2)
        self.plotTimelineDataFrame(plot_column='fff', axe=axe[0])
        
        self.plotDownsamplingTimelineDataFrame()
    
        
        