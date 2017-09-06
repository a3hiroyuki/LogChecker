'''
Created on 2016/09/07

@author: Abe
'''
import datetime
import os
import pandas as pd

holiday_str_list = ['2017/9/1','2017/9/2', '2017/9/3']
holiday_date_list = [datetime.datetime.strptime(x, "%Y/%m/%d").date() for x in holiday_str_list]

def check_new_data(df, yesterday):
    temp_df = df[(df['aaa'] == '○') & (df['Date'] == yesterday)]['ID']
    id_list = list(temp_df)
    if len(id_list) > 0:
        df2 = df[(df['ID'].isin(id_list)) & (df['Date'] < yesterday)]
        print (df2)
        df3 = df2.groupby(['Judge', 'ID']).count()
        df4 = df3[df3['Date'] == 1]
        id_list = list(df4.index)
        if len(id_list) > 0:
            id_list = [x[1] for x in id_list]
            df.loc[(df['ID'].isin(id_list)) & (df['aaa'] == '○'), 'bbb'] = '○'
            df = df[~(df['ID'].isin(id_list)) & ~(df['Date'] < yesterday)]
            print(df)
    return df

def check_output_date_list(today_date, check_date_list, df):
    yesterday = today_date - datetime.timedelta(days=1)
    #errorの場合フラグを立てる
    df.loc[(df['Date'] == yesterday) & (df['Judge'] == '×'), 'aaa'] = '○'
    df = check_new_data(df, yesterday)
    check_date_list.append(yesterday)
    if yesterday in holiday_date_list:
        check_output_date_list(yesterday, check_date_list, df)

#print (holiday_date_list)
parent_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(parent_dir+ "\\aaa.csv")
df['Date'] = df['Date'].apply(lambda x:datetime.datetime.strptime(x,"%Y/%m/%d"))
df['aaa'] = str('')
df['bbb'] = str('')
print (df)

today = datetime.datetime.strptime('2017/9/4', "%Y/%m/%d")
#today= datetime.datetime.today()
yesterday = today.date() - datetime.timedelta(days=1)

print (today) 

output_date_list = []
check_output_date_list(today.date(), output_date_list, df)

print (output_date_list)


    




    
