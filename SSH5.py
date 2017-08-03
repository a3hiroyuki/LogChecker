# coding: UTF-8
'''
Created on 2017/08/1

@author: Abe
'''

import subprocess
import os
import datetime
import _winreg
import sys
import re

#年月日
str_date = datetime.datetime.today().strftime("%Y%m%d")

#commandを定義したマップ
cmd_dict = dict(ssh = 'winScp.com %s',
                cd = 'cd /home/abe/%caw_id%',
                python = 'call python Main.py',
                ls = 'call ls -lt tsv',
                exit = 'exit',
                get = 'get /home/abe/tsv',
                move = 'move' )

#ファイルを格納するディレクトリ
tagrget_dir = './/' + str_date

#サーバーで実行するShellコマンド
shell_cmd = '%(cd)s\n%(python)s\n%(ls)s\n%(exit)s\n' % cmd_dict

#SCPのセッション情報を取得するレジストリ
reg_winscp = _winreg.OpenKey(
        _winreg.HKEY_CURRENT_USER,
        'SOFTWARE\\Martin Prikryl\\WinSCP 2\\Sessions'
        )

#セクション番号とセクション名を格納した辞書
enum_keys_dict = {}

def get_tsv_file(session, caw_id, start_date, end_date):
    
    #plinkとセッション名を利用して接続する
    sp = subprocess.Popen(cmd_dict['ssh'] % (session), stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    
    #caw_idを置換
    shell_cmd_conv = shell_cmd.replace('%caw_id%', caw_id)
    print shell_cmd_conv

'''    
    #シェルを連続実行する
    sp.stdin.write(shell_cmd)
    sp.stdin.close()
    
    print sp.stdout.read()
    
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
'''
#8桁の数値文字列からdateを作成する
def get_datetime(input_str):
    year = int(input_str[0:4])
    mon = int(input_str[4:6])
    day = int(input_str[6:8])
    return datetime.date(year, mon, day)

#セクションIDの入力チェック
def check_section_id(input_str):
    if input_str.isdigit:
        input_num = int(input_str)
        if input_num >= 0 and input_num < len(enum_keys_dict):
            return True
        print "範囲外です"
    return False

def check_caw_id(input_str):
    if re.match(r"[0-9]{8}", input_str) and len(input_str) == 8:
        return True
    else:
        print '8桁の数値を入力してください'
        return False

#入力した日時か範囲内かどうかチェック
def check_date(input_str):
    if re.match(r"[0-9]{8}", input_str) and len(input_str) == 8:
        try:
            date = get_datetime(input_str)
            if date < datetime.date(2020, 1, 1) and date > datetime.date(2015, 1, 1):
                return True
            else:
                print '指定範囲外の年月日が入力されました'
        except:
            print '異常な年月日が入力されました'
    else:
        print '8桁の数値で入力してください'
    return False

#条件にあう文字列を取得するまでループする
def raw_input_wrapper(input_check):
    while True:
        input_str = raw_input('>')
        if input_check(input_str) == True:
            return  input_str
        print 'もう一度入力してください'
 
#レジストリのキーを辞書に格納 
def set_enum_keys_into_dict(key):
    try:
        i = 0
        while True:
            k = _winreg.EnumKey(key, i)
            enum_keys_dict[i] = k
            i += 1
    except EnvironmentError:
        pass
    
    
#メイン関数
if __name__ == '__main__':
    try:
        set_enum_keys_into_dict(reg_winscp)
    finally:
        _winreg.CloseKey(reg_winscp)
    
    if len(enum_keys_dict) == 0:
        print 'セッションが存在しません、終了します'
        sys.exit()
    
    print '以下のセッション番号を選択してください。'
    for key, value in enum_keys_dict.items():
        print str(key) + ':' + value
    session_id = raw_input_wrapper(check_section_id)
    
    print 'cawId(8桁)を入力してください'
    caw_id = raw_input_wrapper(check_caw_id)
    
    start_date = ''
    end_date = ''
    print 'データを取得する年月日（YYYYMMDD）を入力してください'
    while True:
        print 'データ取得開始日を入力してください'
        start_date = raw_input_wrapper(check_date)  
        print 'データ取得終了日を入力してください'  
        end_date = raw_input_wrapper(check_date)
        if get_datetime(end_date) >= get_datetime(start_date):
            break
        else:
            print '開始日より終了日を先にしてください'
    
    get_tsv_file(enum_keys_dict[int(session_id)], caw_id, start_date = start_date, end_date = end_date)
