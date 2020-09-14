# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <Sanz>
import LIST
from LIST.id import *
from LIST.it import *
from LIST.jp import *
from LIST.us import *
from LIST.fr import *
from LIST.kr import *
from LIST.de import *
from LIST.tr import *
import requests, re, os
b = '\x1b[0;34m'
g = '\x1b[1;32m'
w = '\x1b[1;32m'
r = '\x1b[0;34m'
y = '\x1b[1;33m'
cyan = '\x1b[0;36m'
lgray = '\x1b[0;37m'
dgray = '\x1b[1;30m'
ir = '\x1b[0;101m'
reset = '\x1b[0m'

def main():
    os.system('clear')
    os.system('figlet "HACK CCTV" | lolcat')
    print ("{}  '--------------'----------{}------------------.  ").format(r, w)
    print ('{}  | {}Author  : {}MRROBO28 {}     | {}INDO{}N{}{}ESIA         | ').format(r, w, r, w, r, ir, reset, w)
    print ('{}  | {}Youtube : {}TEKTRIKBOT {}| {}@irshad_faqih {}|').format(r, w, w, w, lgray, w)
    print ("{}  '------------------------------------{}-------'  ").format(r, w)
    print ('  {}[ 1 ] {}Italy').format(r, w)
    print ('  {}[ 2 ] {}Indonesia').format(r, w)
    print ('  {}[ 3 ] {}Japan').format(r, w)
    print ('  {}[ 4 ] {}United States').format(r, w)
    print ('  {}[ 5 ] {}France').format(r, w)
    print ('  {}[ 6 ] {}Korea').format(r, w)
    print ('  {}[ 7 ] {}German').format(r, w)
    print ('  {}[ 8 ] {}Turkey').format(r, w)
    print ('  {}[ 00 ] {}Exit').format(r, w)
    print ''
    select = input('\x1b[1;31m[ \x1b[1;37mSelect@Number \x1b[1;31m]\x1b[1;37m> ')
    filtering(select)


def filtering(pilih):
    if pilih == 1:
        italy()
    elif pilih == 2:
        indonesia()
    elif pilih == 3:
        japan()
    elif pilih == 4:
        unitedstates()
    elif pilih == 5:
        france()
    elif pilih == 6:
        korea()
    elif pilih == 7:
        german()
    elif pilih == 8:
        turkey()
    elif pilih == 0 or 0:
        print r + 'Exiting ...' + w
        os.sys.exit()
    else:
        print r + 'Exiting ...' + w
        os.sys.exit()


if __name__ == '__main__':
    main()