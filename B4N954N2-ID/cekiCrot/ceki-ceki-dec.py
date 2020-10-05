# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <Sazxt>
import os, sys, time, random
m = '\x1b[31;1m'
h = '\x1b[32;1m'
b = '\x1b[36;1m'
pu = '\x1b[37;1m'
k = '\x1b[33;1m'
h2 = '\x1b[32;4m'
p = '\x1b[0;1m'
u = '\x1b[35;1m'
hi = '\x1b[30;1m'

def run(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


os.system('clear')
time.sleep(1)
run(pu + '\n\n[' + m + '!' + pu + '] ' + h + 'Subscribe dulu donk Channel Youtube Gw' + m + ' !!\n')
time.sleep(2)
os.system('xdg-open https://www.youtube.com/channel/UCqp78GUXAJsSteeJqGu9HBg')
os.system('php config-id-2.php')