# coding: UTF-8
'''
Created on 2017/07/27

@author: abe
'''

import os
import paramiko
import scp

home_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + '\\'
config_file = os.path.join(home_path,'.ssh/config')
ssh_config = paramiko.SSHConfig()
ssh_config.parse(open(config_file, 'r'))

lkup1 = ssh_config.lookup('aaa')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()

cfg = {'hostname': lkup1['hostname'], 
       'username': lkup1["user"],
       'key_filename':lkup1['identityfile'] }

if 'proxycommand' in lkup1: 
    cfg['sock'] = paramiko.ProxyCommand(ssh_config['proxycommand']) 

ssh.connect(**cfg)

stdin, stdout, stderr = ssh.exec_command('bash -')

#シェル
cmd = '''
python /home/abe/Main.py
ls /home/abe
exit
'''
stdin.write(cmd)
str_line = stdout.read()
for str in str_line.split('\n'):
    print(str)

scp = scp.SCPClient(ssh.get_transport())
print(scp.get('/home/abe/abe.txt'))

#sftp.close()
ssh.close()
scp.close()
