'''
Created on 2017/08/02

@author: hiroy
'''

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

start = datetime.strptime('20120111', '%Y%m%d')
end = datetime.strptime('20120111', '%Y%m%d')

def get_month_first_day(date):
    return datetime(day=1, month=date.month, year=date.year)

def get_month_end_day(date):
    return datetime(date.year, date.month , 1) + relativedelta(months=1) + timedelta(days=-1)

def set_day_span_to_str_list(str_list, start_date, end_date):
    for n in range((end_date - start_date).days):
        date = start_date + timedelta(n)
        str_list.append(date.strftime('%Y%m%d'))
    str_list.append(end_date.strftime('%Y%m%d'))
        
        
def set_month_span_to_list(date_list, start_date, end_date):
    date_list.append(start_date)
    while(start_date.year != end_date.year or start_date.month != end_date.month):
        start_date += relativedelta(months=1)
        if start_date.month == end_date.month:
            date_list.append(end_date)
        else:
            date_list.append(start_date)
        
def replace_date_list_to_str_date_list(str_date_list, date_list):
    for index in range(len(date_list)):
        date = date_list[index]
        if index == 0:
            set_day_span_to_str_list(str_date_list, date, get_month_end_day(date))
        elif index == len(date_list) - 1:
            set_day_span_to_str_list(str_date_list, get_month_first_day(date), date)
        else:
            str_date_list.append(date.strftime('%Y%m'))

date_list = []
set_month_span_to_list(date_list, start, end)

str_date_list = []
if len(date_list) > 1:
    replace_date_list_to_str_date_list(str_date_list, date_list)
else:
    set_day_span_to_str_list(str_date_list, start, end)
    
    
for str in str_date_list:
    print str