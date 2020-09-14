# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: o.py
# Compiled at: 2020-08-22 12:50:28
import os, sys, time
from time import sleep
os.system('clear')
os.system('xdg-open https://m.youtube.com/channel/UCSqjFOkS5_2bEP9WW24pnLA')
sleep(5)
print '\x1b[1;37m\xe2\x97\x80\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;37m\xe2\x96\xb6'
print '\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]\x1b[1;33mLogin SC'
print '\x1b[1;37m[\x1b[1;32m2\x1b[1;37m]\x1b[1;33minstall bahan dulu'
print '\x1b[1;37m[\x1b[1;32m0\x1b[1;37m]\x1b[1;31mexit'
pil = raw_input('\x1b[1;33mPilih > \x1b[1;32m')
if pil == '1':
    os.chdir('X')
    os.system('python2 a.py')
elif pil == '2':
    os.system('clear')
    print '\x1b[1;33mInstalling...'
    sleep(2)
    os.system('pkg install figlet ruby -y')
    os.system('gem install lolcat')
    os.system('clear')
    print '\x1b[1;32mBahan Terinstall'
    fil = raw_input('\x1b[1;33mTekan Enter untuk login sc : ')
    if fil == '':
        os.chdir('X')
        os.system('python2 a.py')
elif pil == '0':
    sys.exit()
# okay decompiling run.pyc
