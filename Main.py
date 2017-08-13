# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import pandas
import os
from CheckerManager import CheckerManager
from datetime import datetime
import math

path =  'C:\\workspace\\python1\\Test950\\src\\tsv\\'

_cheker_manager = CheckerManager()
    
def create_dataframe(network = 'NETWORK', date = 'DATE', id = 'AAA'):
    
    file_name_dict = {'NETWORK' : id + '_' + network if id != '' else network,
                      'DATE' :  id + '_' + date if id != '' else date}
    
    #フォルダの読み込み
    dir_list = []
    for item in os.listdir(path):
        if os.path.isdir(path + item):
            dir_list.append(item)
            
    for dir_name in dir_list:
        try:
            file_name = file_name_dict[dir_name]
            if file_name is not None:
                _cheker_manager.makeDataFrameFromDataInDir(path, dir_name, file_name)
        except KeyError:
            print ('error')
            
    print (_cheker_manager.getDataFrameDict())
    
    
def plot_type_distribution():
    #全体の確認
    groupby_frame_dict = _cheker_manager.getGroupByFrameDict()
    fig = plt.figure()
    for key, value in groupby_frame_dict.items():
        ax = fig.add_subplot(1, len(groupby_frame_dict), 1)
        ax.set_title(key)
        value.plot(kind='bar', ax = ax)
        
    plt.show()
    
def plot_calc_data_per_day(name='DATE'):
    first_date = datetime.strptime('2017/1/1', '%Y/%m/%d')
    end_date = datetime.strptime('2017/1/10', '%Y/%m/%d')
    calc_data_dict = {key : value 
                      for key, value in _cheker_manager.getDataFrame(name).getCalcDataDictPerDay().items()
                      if key >= first_date and key <= end_date}
    print (calc_data_dict)
    count = 1
    size = len(calc_data_dict)
    col_num = size if size/5 == 0 else 5
    row_num = math.ceil(size/5)
    fig = plt.figure()
    for key, value in calc_data_dict.items():
        ax = fig.add_subplot(row_num, col_num, count)
        ax.set_title(key)
        #ax.plot(value)
        #value.plot(kind='bar', ax = ax)
        value.plot(kind='bar', ax = ax)
        count += 1 
    plt.show()

if __name__ == '__main__':
    
    
    create_dataframe()
    plot_type_distribution()
    plot_calc_data_per_day()
    
    
    '''
    #データの分布の確認
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.checkData()
    
    #データの分布の確認
    for key in checker_map.keys():
        checker = checker_map.get(key)
        checker.checkDataPattern()
    '''

        
    
    
    