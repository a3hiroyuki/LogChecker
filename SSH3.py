# coding: UTF-8
'''
Created on 2017/08/1

@author: Abe
'''
import time
import subprocess
import os
from datetime import datetime

#年月日
str_date = datetime.today().strftime("%Y%m%d")

#commandを定義したマップ
cmd_dict = {'ssh' : 'plink.exe -l abe ',
            'scp' : 'pscp -l abe -load ',
            'cd'  : 'cd /home/abe/',
            'python' : 'python Main.py',
            'ls' : 'ls -lt tsv',
            'exit' : 'exit'
            }

server_dict = { 'aaa' : '192.168.1.10'
               }

tagrget_dir = './/' + str_date
#Shellコマンド
shell_cmd = cmd_dict['cd'] + '\n' + cmd_dict['python'] + '\n' + cmd_dict['ls'] + '\n' + cmd_dict['exit'] + '\n'

def get_history_file(session, ip_address):
    
    #plinkとセッション名を利用して接続する
    sp = subprocess.Popen(cmd_dict['ssh'] + session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

    #シェルを連続実行する
    sp.stdin.write(shell_cmd)
    sp.stdin.close()

    #シェル結果を受け取る
    line = sp.stdout.readline()
    
    #シェルの結果からファイル名を取得する
    file_name = ''
    isHitCommand = False
    while line:
        print line
        if isHitCommand == True and str_date in line:
            first = line.rfind(' ')
            file_name = line[first + 1:].replace('\n','')
            break
        if '$ ' + cmd_dict['ls'] in line:
            isHitCommand = True
            print 'Hit'
        line = sp.stdout.readline()
    print file_name

    sp.wait()
    
    if not os.path.isdir(tagrget_dir):
        os.makedirs(tagrget_dir)
    
    #scpによりファイルをダウンロードする
    scp_cmd = cmd_dict['scp'] + session + ' abe@' + ip_address + ':tsv/' + file_name + ' ' + tagrget_dir
    print scp_cmd
    sp2 = subprocess.Popen(scp_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    print sp2.stdout.read()

#メイン関数
if __name__ == '__main__':
    for key, value in server_dict.items():
        get_history_file(key, value)
