'''
Created on 2017/07/27

@author: 
'''
import os
import subprocess

cmd1 = 'ssh aaa "python /home/abe/Main.py"'
cmd2 = 'ssh aaa "cat /home/abe/abe.txt" > hoge.txt'
cmd3 = 'ssh aaa "ls"'
cmd4 = 'scp aaa:'

os.system(cmd1)
os.system(cmd2)
ret  =  subprocess.check_output( cmd3.split(" ") )
found_file_name = ""
print str(ret)
for file_name in str(ret).split('\n'):
    print file_name
    index = file_name.find('Main')
    if index != -1:
        found_file_name = file_name
if found_file_name != "":
    cmd4 = cmd4 + "/home/abe/" + found_file_name +" ./"
    print cmd4
    os.system(cmd4)
