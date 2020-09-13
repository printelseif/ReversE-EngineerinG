# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
import os, requests
os.system('clear')
os.system('termux-open-url https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ')
os.system('clear')
os.system('toilet -f mono9 -F gay Admin')
print '\x1b[1;91m--------------\x1b[1;97m+++++++++++\x1b[1;91m-------------------'
print '\x1b[1;92m Author :\x1b[1;93m TegarXploit'
print '\x1b[1;92m Github :\x1b[1;93m github.com/TegarXploit'
print '\x1b[1;92m Youtube:\x1b[1;93m CYTOM'
print '\x1b[1;91m--------------\x1b[1;97m+++++++++++\x1b[1;91m-------------------'
print '\x1b[1;93m'
target = raw_input('Masukan web target=>> ')
f = open('wordlist.txt', 'r')
kontent = f.read()
x = kontent.split('\n')
for i in x:
    url = target + '/' + i
    code = requests.get(str(url)).status_code
    if code == 200:
        print '\x1b[1;97m<!>\x1b[1;92mberhasil ' + url
    else:
        print '\x1b[1;91m<$>\x1b[1;93mgagal  ' + url