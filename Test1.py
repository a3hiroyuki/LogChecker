'''
Created on 2016/07/14

@author: hiroy
'''
import datetime
'''
weekMap = {('Mon', 1):1, ('Thr',2):2, ('Wed',3):3}

if ('Mon', 1) in weekMap:
    print 'True'
    
weekMap.get(('Mon, 1'), 'nai')

print weekMap.values()
print weekMap.keys()

del(weekMap[('Mon', 1)])

for k, c in weekMap.items():
    print str(k) + str(c)
    
def greet():
    print 'hello'
    
greet()
'''

holiday_str_list = ['2017/8/20', '2017/8/21', '2017/8/25', '2017/7/21']
holiday_date_list = [datetime.datetime.strptime(x, "%Y/%m/%d").date() for x in holiday_str_list]

def check_output_date_list(today_date, check_date_list):
    yeasterday = today_date - datetime.timedelta(days=1)
    check_date_list.append(yeasterday)
    if yeasterday in holiday_date_list:
        check_output_date_list(yeasterday, check_date_list)

print (holiday_date_list)

today= datetime.datetime.today()
yeasterday = today.date() - datetime.timedelta(days=1)

print (today) 
#print (yeasterday)

output_date_list = []
check_output_date_list(today.date(), output_date_list)

print output_date_list


    




    
