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
import queue
import random

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

def report(message):
    sys.stdout.write(message)
    sys.stdout.flush()

#ダウンロード中のアニメーション
class Anime():
    def __init__(self):
        self.is_done = False

    def animate(self):
        for c in itertools.cycle(['.', '..', '...', '   ']):
            if  self.is_done == True:
                break
            sys.stdout.flush()
            report("\rdownLoading" + c)
            time.sleep(1)  
        sys.stdout.write('\rDone!     ')
    
    def stop(self):
        self.is_done = True

class Downloader:
    
    def __init__(self, session):
        self.session = session
        
    def get_history_file(self):
        
        sp = subprocess.Popen(cmd_dict['ssh'] + self.session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    
        #シェルを連続実行する
        sp.stdin.write(shell_cmd.encode('utf-8'))
        sp.stdin.close()
        
        lines = sp.stdout.read().decode('utf-8')
        
        line_arr = lines.split('\n')
    
        #シェルの結果からファイル名を取得する
        file_name = ''
        is_exe_command = False
        for line in line_arr:
            if is_exe_command == True and str_date in line:
                first = line.rfind(' ')
                file_name = line[first + 1:].replace('\n','')
                break
            if cmd_dict['ls'] in line:
                is_exe_command = True
                report ('exe command\n' )
            line = sp.stdout.readline()
        report (file_name + '\n')
        
        sp.stdout.close()
        
        self.file_name = file_name
    
    
    def get_file(self):
        #getによりファイルをダウンロードする
        num = random.randint(1,10000)
        sp = subprocess.Popen(cmd_dict['ssh'] + self.session, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        get_cmd = '%s/%s %s\n%s\n' % (cmd_dict['get'], self.file_name, 'C:\\Users\\hiroy\\Desktop\\ggg\\' + str_date + '\\aaa' + str(num)+ '.txt' , cmd_dict['exit'])
        #get_cmd = '%s\n' % (cmd_dict['exit'])
        #print (get_cmd)
        sp.stdin.write(get_cmd.encode('utf-8'))
        sp.stdin.close()
        
        lines = sp.stdout.read().decode('utf-8')
        '''
        for line in lines.split('\n'):
            report (line)
        '''
        sp.stdout.close()
        
    def download(self):
        self.get_history_file()
        self.get_file()
        report('finish\n')
        
#マルチタスク処理
def worker(jobs, results):
    try:
        downloader = jobs.get()
        downloader.download()
    finally:
        jobs.task_done()

def create_threads(jobs, results, concurrency):
    for _ in range(concurrency):
        thread = threading.Thread(target = worker, args=(jobs, results))
        thread.daemon = True
        thread.start()
        
def add_jobs(jobs, server_session_list):
    for session in server_session_list:
        jobs.put(Downloader(session))
        
def process(jobs, results):
    try:
        jobs.join()
    except KeyboardInterrupt:
        canceled = True
    report('jfkdjfkldjfkljf')
    
#メイン関数
if __name__ == '__main__':
    anime = Anime()
    threading.Thread(target=anime.animate).start()
    #フォルダが存在しなければ作成する
    if not os.path.isdir(tagrget_dir):
        os.makedirs(tagrget_dir)
    jobs = queue.Queue()
    results = queue.Queue()
    create_threads(jobs, results, 3)
    add_jobs(jobs, server_session_list)
    process(jobs, results)
    anime.stop()
    

