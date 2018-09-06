# !/usr/bin/perl
#
#
#
#

import paramiko

with paramiko.SSHClient() as ssh:
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(hostname='na-dev-kazu', port=22, username='joshua', password='joshua1017')
   stdin, stdout, stderr = ssh.exec_command('mkdir test')
