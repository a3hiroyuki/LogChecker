# coding: UTF-8
'''
Created on 2017/08/1

@author: Abe
'''
import time
import subprocess
import os
from datetime import datetime
import sys
import time
import itertools
import threading

isDone = False
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
server_session_list = ['aaa', 'aaa', 'aaa']

#ファイルを格納するディレクトリ
tagrget_dir = './/' + str_date

#サーバーで実行するShellコマンド
shell_cmd = '%(cd)s\n%(python)s\n%(ls)s\n%(exit)s\n' % cmd_dict


#ダウンロード中のアニメーション
class Anime():
    def __init__(self):
        self.is_done = False

    def animate(self):
        for c in itertools.cycle(['.', '..', '...', '   ']):
            if  self.is_done == True:
                break
            sys.stdout.write("\rdownLoading" + c)
            sys.stdout.flush()
            time.sleep(1)  
        sys.stdout.write('\rDone!     ')
    
    def stop(self):
        self.is_done = True

def get_history_file(session):
    
    #host = cmd_dict['ssh'] % (session)
    #print host
    #plinkとセッション名を利用して接続する
    
    
    sp = subprocess.Popen(cmd_dict['ssh'] + session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

    #シェルを連続実行する
    sp.stdin.write(shell_cmd.encode('utf-8'))
    sp.stdin.close()
    
    lines = sp.stdout.read().decode('utf-8')
    
    line_arr = lines.split('\n')

    #シェルの結果からファイル名を取得する
    file_name = ''
    is_exe_command = False
    line = sp.stdout.readline()
    for line in line_arr:
        print (line)
        if is_exe_command == True and str_date in line:
            first = line.rfind(' ')
            file_name = line[first + 1:].replace('\n','')
            break
        if cmd_dict['ls'] in line:
            is_exe_command = True
            print ('exe command')
        line = sp.stdout.readline()
    print (file_name)
    
    sp.stdout.close()
    
    return file_name
    
    
def get_file(session, file_name):
    #getによりファイルをダウンロードする
    sp = subprocess.Popen(cmd_dict['ssh'] + session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    get_cmd = '%s/%s %s\n%s\n' % (cmd_dict['get'], file_name, 'C:\\Users\\hiroy\\Desktop\\ggg\\' + str_date + '\\aaa.txt' , cmd_dict['exit'])
    #get_cmd = '%s\n' % (cmd_dict['exit'])
    print (get_cmd)
    sp.stdin.write(get_cmd.encode('utf-8'))
    sp.stdin.close()
    
    lines = sp.stdout.read().decode('utf-8')
    
    for line in lines.split('\n'):
        print (line)
    
    sp.stdout.close()
    
    #フォルダが存在しなければ作成する
    if not os.path.isdir(tagrget_dir):
        os.makedirs(tagrget_dir)
    
#メイン関数
if __name__ == '__main__':
    for session in server_session_list:
        anime = Anime()
        threading.Thread(target=anime.animate).start()
        file_naem = get_history_file(session)
        get_file(session, file_naem)
        anime.stop()
