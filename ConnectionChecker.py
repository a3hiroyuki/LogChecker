
from BaseChecker import BaseChecker
from pandas.core.frame import DataFrame

class ConnectionChecker(BaseChecker):
    
    columnArr = ['ddd', 'eee', 'fff']
        
    def __init__(self):
        BaseChecker.__init__(self)
            
    def makeDataFrame(self):
        self.df = DataFrame(BaseChecker.makeDataFrame(self), columns=self.columnArr)
        print self.df