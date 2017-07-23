
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame

class CONNECTIONChecker(BaseChecker):
    
    columnArr = ['Date', 'Label', 'fff']
        
    def __init__(self):
        BaseChecker.__init__(self)
        self.mTitle = 'CONNTECTION'
            
    def makeDataFrame(self):
        self.mDataframe = DataFrame(BaseChecker.makeDataFrame(self), columns=self.columnArr)
        print self.mDataframe
        
    def checkData(self):
        BaseChecker.checkData(self)