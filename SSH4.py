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
cmd_dict = dict(ssh = 'winScp.com ',
                cd = 'cd /home/abe/',
                python = 'call python Main.py',
                ls = 'call ls -lt tsv',
                exit = 'exit',
                get = 'get /home/abe/tsv',
                move = 'move' )

#履歴を取得するサーバーのリスト
server_session_list = {'aaa'}

#ファイルを格納するディレクトリ
tagrget_dir = './/' + str_date

#サーバーで実行するShellコマンド
shell_cmd = '%(cd)s\n%(python)s\n%(ls)s\n%(exit)s\n' % cmd_dict

def get_history_file(session):
    
    #plinkとセッション名を利用して接続する
    sp = subprocess.Popen(cmd_dict['ssh'] + session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

    #シェルを連続実行する
    sp.stdin.write(shell_cmd)
    sp.stdin.close()

    #シェルの結果からファイル名を取得する
    file_name = ''
    is_exe_command = False
    line = sp.stdout.readline()
    while line:
        print line
        if is_exe_command == True and str_date in line:
            first = line.rfind(' ')
            file_name = line[first + 1:].replace('\n','')
            break
        if cmd_dict['ls'] in line:
            is_exe_command = True
            print 'exe command'
        line = sp.stdout.readline()
    print file_name
    
    #getによりファイルをダウンロードする
    sp2 = subprocess.Popen(cmd_dict['ssh'] + session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    get_cmd = '%s/%s\n%s\n' % (cmd_dict['get'], file_name, cmd_dict['exit'])
    sp2.stdin.write(get_cmd)
    
    print sp2.stdout.read()
    
    #フォルダが存在しなければ作成する
    if not os.path.isdir(tagrget_dir):
        os.makedirs(tagrget_dir)
    
    #ファイルの移動
    mv_cmd = '%s %s %s' % (cmd_dict['move'], file_name, str_date)
    os.system(mv_cmd)
    
    
#メイン関数
if __name__ == '__main__':
    for session in server_session_list:
        get_history_file(session)
