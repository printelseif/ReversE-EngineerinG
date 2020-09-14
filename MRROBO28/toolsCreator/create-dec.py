# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name:  
import os, sys, time
from time import sleep
m = '\x1b[1;31m'
b = '\x1b[1;36m'
k = '\x1b[1;33m'
h = '\x1b[1;32m'
u = '\x1b[1;35m'
p = '\x1b[1;37m'
ut = '\x1b[1;34m'

def wr(s):
    for x in s + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(1.0 / 1000)


ban = '     \t\x1b[1;37m\t\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac  \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90 \n\t         \xe2\x95\x91 \xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x90     \n\t         \xe2\x95\xa9 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98     \n\t      \x1b[1;37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90 \n\t      \xe2\x95\x91  \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98 \n\t      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80 \n\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;37m[\x1b[1;33m+\x1b[1;37m]\x1b[1;33mAuthor  \x1b[1;37m: \x1b[1;32mMRROBO28\n\x1b[1;37m[\x1b[1;33m+\x1b[1;37m]\x1b[1;33mGithub  \x1b[1;37m: \x1b[1;32mhttps://github.com/MRROBO28\n\x1b[1;37m[\x1b[1;33m+\x1b[1;37m]\x1b[1;33mYoutube \x1b[1;37m: \x1b[1;32mTEKTRIKBOT CN\n\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;31mNotes : hanya membuat file dengan python2\n'

def menu():
    os.system('clear')
    os.system('xdg-open https://www.youtube.com/channel/UCSqjFOkS5_2bEP9WW24pnLA')
    sleep(5)
    wr(ban)
    naf = raw_input(p + '[' + h + '+' + p + ']' + h + 'Ex : namafile.py\n' + p + '[' + h + '+' + p + ']' + b + 'Masukkan Nama file ' + p + '> ' + k)
    w = open(naf, 'w')
    w.write('#coding:utf-8\nimport os,sys,time\nfrom time import sleep\n \nm = "\x1b[1;31m"\nb = "\x1b[1;36m"\nk = "\x1b[1;33m"\nh = "\x1b[1;32m"\nu = "\x1b[1;35m"\np = "\x1b[1;37m"\n \nos.system("clear")\nsleep(2)\n')
    print ''
    print p + '[' + h + '+' + p + ']' + k + 'Warna\n' + p + '[' + k + 'b' + p + ']' + h + 'biru\n' + p + '[' + k + 'm' + p + ']' + h + 'merah\n' + p + '[' + k + 'k' + p + ']' + h + 'kuning\n' + p + '[' + k + 'h' + p + ']' + h + 'hijau\n' + p + '[' + k + 'p' + p + ']' + h + 'putih\n' + p + '[' + k + 'u' + p + ']' + h + 'ungu\n'
    war = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Warna Banner ' + p + '> ' + k)
    print ''
    bn = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Judul Banner ' + p + '> ' + k)
    print ''
    w.write('print ' + war + '\n' + 'os.system("figlet ' + bn + '")\n')
    war1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Warna Garis (===) ' + p + '> ' + k)
    print ''
    wart = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Warna teks ' + p + '> ' + k)
    print ''
    aut = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Author (Nama lo) ' + p + '> ' + k)
    print ''
    is1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan channel yt ' + p + '> ' + k)
    print ''
    w.write('print ' + war1 + '\n' + 'print "\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"\n')
    w.write('print ' + wart + '+' + '"Author  : ' + aut + '"\n')
    w.write('print "Youtube : ' + is1 + '"\n')
    w.write('print ' + war1 + '+' + '"\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"\n')
    w.write('print "\t     \x1b[1;36m[\x1b[1;41m\x1b[1;37m Menu \x1b[00m\x1b[1;36m]"\n')
    print k + '[!]' + h + 'Menu Max : 5'
    pil = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Jumlah menu ' + p + '> ' + k)
    if pil == '1':
        os.system('clear')
        sleep(2)
        print h
        os.system('figlet Menu')
        mn1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 1 ' + p + '> ' + k)
        print ''
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]"' + '+' + wart + '+"' + mn1 + '"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m77\x1b[1;37m]\x1b[1;33mInstall bahan"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m00\x1b[1;37m]\x1b[1;31mExit"\n')
        wri = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan warna Input ' + p + '> ' + k)
        print p + '[' + h + '+' + p + ']' + k + 'Jika tidak ada enter saja'
        inbk = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pkg install bahan ' + p + '> ' + k)
        print ''
        inbp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pip(1/2) install bahan ' + p + '> ' + k)
        print ''
        w.write('pil = raw_input(' + wri + '+' + '"pilih > "' + '+' + wart + ')\n')
        gitp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Tekan enter untuk lanjut ke edit github ' + p + '> ' + k)
        if gitp == '':
            os.system('clear')
            sleep(2)
            print k
            os.system('figlet Github')
            print p + '[' + h + '+' + p + ']' + k + 'Menu 1'
            mng1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 1 ' + p + '> ' + k)
            ch1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            w.write('if pil == "1":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng1 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch1 + '")\n')
            w.write('  os.system("' + mi1 + '")\n')
            w.write('elif pil == "0":\n  print "\x1b[1;31mExiting..."\n  sleep(2)\n')
            w.write('  sys.exit()\n')
            w.write('elif pil == "77":\n')
            w.write('  os.system("' + inbk + '")\n')
            w.write('  os.system("' + inbp + '")\n')
            w.write('  os.system("python2 ' + naf + '")\n')
    elif pil == '2':
        os.system('clear')
        sleep(2)
        print h
        os.system('figlet Menu')
        mn1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 1 ' + p + '> ' + k)
        print ''
        mn2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 2 ' + p + '> ' + k)
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]"' + '+' + wart + '+"' + mn1 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m2\x1b[1;37m]"' + '+' + wart + '+"' + mn2 + '"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m77\x1b[1;37m]\x1b[1;33mInstall bahan"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m00\x1b[1;37m]\x1b[1;31mExit"\n')
        wri = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan warna Input ' + p + '> ' + k)
        print ''
        print p + '[' + h + '+' + p + ']' + k + 'Jika tidak ada enter saja'
        inbk = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pkg install bahan ' + p + '> ' + k)
        print ''
        inbp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pip(1/2) install bahan ' + p + '> ' + k)
        print ''
        w.write('pil = raw_input(' + wri + '+' + '"pilih > "' + '+' + wart + ')\n')
        gitp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Tekan enter untuk lanjut ke edit github ' + p + '> ' + k)
        if gitp == '':
            os.system('clear')
            sleep(2)
            print k
            os.system('figlet Github')
            print p + '[' + h + '+' + p + ']' + k + 'Menu 1'
            mng1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 1 ' + p + '> ' + k)
            ch1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 2'
            mng2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 2 ' + p + '> ' + k)
            ch2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            w.write('if pil == "1":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng1 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch1 + '")\n')
            w.write('  os.system("' + mi1 + '")\n \n')
            w.write('elif pil == "2":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng2 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch2 + '")\n')
            w.write('  os.system("' + mi2 + '")\n')
            w.write('elif pil == "77":\n')
            w.write('  os.system("' + inbk + '")\n')
            w.write('  os.system("' + inbp + '")\n')
            w.write('  os.system("python2 ' + naf + '")\n')
            w.write('elif pil == "0":\n  print "\x1b[1;31mExiting..."\n  sleep(2)\n')
            w.write('  sys.exit()\n')
    elif pil == '3':
        os.system('clear')
        sleep(2)
        print h
        os.system('figlet Menu')
        mn1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 1 ' + p + '> ' + k)
        print ''
        mn2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 2 ' + p + '> ' + k)
        print ''
        mn3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 3 ' + p + '> ' + k)
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]"' + '+' + wart + '+"' + mn1 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m2\x1b[1;37m]"' + '+' + wart + '+"' + mn2 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m3\x1b[1;37m]"' + '+' + wart + '+"' + mn3 + '"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m77\x1b[1;37m]\x1b[1;33mInstall bahan"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m00\x1b[1;37m]\x1b[1;31mExit"\n')
        wri = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan warna Input ' + p + '> ' + k)
        print ''
        print p + '[' + h + '+' + p + ']' + k + 'Jika tidak ada enter saja'
        inbk = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pkg install bahan ' + p + '> ' + k)
        print ''
        inbp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pip(1/2) install bahan ' + p + '> ' + k)
        print ''
        w.write('pil = raw_input(' + wri + '+' + '"pilih > "' + '+' + wart + ')\n')
        gitp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Tekan enter untuk lanjut ke edit github ' + p + '> ' + k)
        if gitp == '':
            os.system('clear')
            sleep(2)
            print k
            os.system('figlet Github')
            print p + '[' + h + '+' + p + ']' + k + 'Menu 1'
            mng1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 1 ' + p + '> ' + k)
            ch1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 2'
            mng2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 2 ' + p + '> ' + k)
            ch2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 3'
            mng3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 3 ' + p + '> ' + k)
            ch3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            w.write('if pil == "1":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng1 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch1 + '")\n')
            w.write('  os.system("' + mi1 + '")\n \n')
            w.write('elif pil == "2":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng2 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch2 + '")\n')
            w.write('  os.system("' + mi2 + '")\n')
            w.write('elif pil == "3":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng3 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch3 + '")\n')
            w.write('  os.system("' + mi3 + '")\n')
            w.write('elif pil == "77":\n')
            w.write('  os.system("' + inbk + '")\n')
            w.write('  os.system("' + inbp + '")\n')
            w.write('  os.system("python2 ' + naf + '")\n')
            w.write('elif pil == "0":\n  print "\x1b[1;31mExiting..."\n  sleep(2)\n')
            w.write('  sys.exit()\n')
    elif pil == '4':
        os.system('clear')
        sleep(2)
        print h
        os.system('figlet Menu')
        mn1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 1 ' + p + '> ' + k)
        print ''
        mn2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 2 ' + p + '> ' + k)
        print ''
        mn3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 3 ' + p + '> ' + k)
        print ''
        mn4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 4 ' + p + '> ' + k)
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]"' + '+' + wart + '+"' + mn1 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m2\x1b[1;37m]"' + '+' + wart + '+"' + mn2 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m3\x1b[1;37m]"' + '+' + wart + '+"' + mn3 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m4\x1b[1;37m]"' + '+' + wart + '+"' + mn4 + '"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m77\x1b[1;37m]\x1b[1;33mInstall bahan"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m00\x1b[1;37m]\x1b[1;31mExit"\n')
        wri = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan warna Input ' + p + '> ' + k)
        print ''
        print p + '[' + h + '+' + p + ']' + k + 'Jika tidak ada enter saja'
        inbk = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pkg install bahan ' + p + '> ' + k)
        print ''
        inbp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pip(1/2) install bahan ' + p + '> ' + k)
        print ''
        w.write('pil = raw_input(' + wri + '+' + '"pilih > "' + '+' + wart + ')\n')
        gitp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Tekan enter untuk lanjut ke edit github ' + p + '> ' + k)
        if gitp == '':
            os.system('clear')
            sleep(2)
            print k
            os.system('figlet Github')
            print p + '[' + h + '+' + p + ']' + k + 'Menu 1'
            mng1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 1 ' + p + '> ' + k)
            ch1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 2'
            mng2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 2 ' + p + '> ' + k)
            ch2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 3'
            mng3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 3 ' + p + '> ' + k)
            ch3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 4'
            mng4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 4 ' + p + '> ' + k)
            ch4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            w.write('if pil == "1":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng1 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch1 + '")\n')
            w.write('  os.system("' + mi1 + '")\n \n')
            w.write('elif pil == "2":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng2 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch2 + '")\n')
            w.write('  os.system("' + mi2 + '")\n')
            w.write('elif pil == "3":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng3 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch3 + '")\n')
            w.write('  os.system("' + mi3 + '")\n')
            w.write('elif pil == "4":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng4 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch4 + '")\n')
            w.write('  os.system("' + mi4 + '")\n')
            w.write('elif pil == "77":\n')
            w.write('  os.system("' + inbk + '")\n')
            w.write('  os.system("' + inbp + '")\n')
            w.write('  os.system("python2 ' + naf + '")\n')
            w.write('elif pil == "0":\n  print "\x1b[1;31mExiting..."\n  sleep(2)\n')
            w.write('  sys.exit()\n')
    elif pil == '5':
        os.system('clear')
        sleep(2)
        print h
        os.system('figlet Menu')
        mn1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 1 ' + p + '> ' + k)
        print ''
        mn2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 2 ' + p + '> ' + k)
        print ''
        mn3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 3 ' + p + '> ' + k)
        print ''
        mn4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 4 ' + p + '> ' + k)
        print ''
        mn5 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan nama  menu 5 ' + p + '> ' + k)
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m1\x1b[1;37m]"' + '+' + wart + '+"' + mn1 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m2\x1b[1;37m]"' + '+' + wart + '+"' + mn2 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m3\x1b[1;37m]"' + '+' + wart + '+"' + mn3 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m4\x1b[1;37m]"' + '+' + wart + '+"' + mn4 + '"\n')
        w.write('print ' + '"\x1b[1;37m[\x1b[1;32m5\x1b[1;37m]"' + '+' + wart + '+"' + mn5 + '"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m77\x1b[1;37m]\x1b[1;33mInstall bahan"\n')
        w.write('print "\x1b[1;37m[\x1b[1;32m00\x1b[1;37m]\x1b[1;31mExit"\n')
        wri = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan warna Input ' + p + '> ' + k)
        print ''
        print p + '[' + h + '+' + p + ']' + k + 'Jika tidak ada enter saja'
        inbk = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pkg install bahan ' + p + '> ' + k)
        print ''
        inbp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan pip(1/2) install bahan ' + p + '> ' + k)
        print ''
        w.write('pil = raw_input(' + wri + '+' + '"pilih > "' + '+' + wart + ')\n')
        gitp = raw_input(p + '[' + h + '+' + p + ']' + b + 'Tekan enter untuk lanjut ke edit github ' + p + '> ' + k)
        if gitp == '':
            os.system('clear')
            sleep(2)
            print k
            os.system('figlet Github')
            print p + '[' + h + '+' + p + ']' + k + 'Menu 1'
            mng1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 1 ' + p + '> ' + k)
            ch1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi1 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 2'
            mng2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 2 ' + p + '> ' + k)
            ch2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi2 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 3'
            mng3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 3 ' + p + '> ' + k)
            ch3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi3 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 4'
            mng4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 4 ' + p + '> ' + k)
            ch4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi4 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            print p + '[' + h + '+' + p + ']' + k + 'Menu 5'
            mng5 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan url github menu 5 ' + p + '> ' + k)
            ch5 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan Direktori githubnya ' + p + '> ' + k)
            print p + '[' + h + '+' + p + ']' + k + 'Ex : python(2/3)/sh namafile.(py/sh)'
            mi5 = raw_input(p + '[' + h + '+' + p + ']' + b + 'Masukkan file intinya ' + p + '> ' + k)
            print ''
            w.write('if pil == "1":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng1 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch1 + '")\n')
            w.write('  os.system("' + mi1 + '")\n \n')
            w.write('elif pil == "2":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng2 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch2 + '")\n')
            w.write('  os.system("' + mi2 + '")\n')
            w.write('elif pil == "3":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng3 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch3 + '")\n')
            w.write('  os.system("' + mi3 + '")\n')
            w.write('elif pil == "4":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng4 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch4 + '")\n')
            w.write('  os.system("' + mi4 + '")\n')
            w.write('elif pil == "5":\n  print "\x1b[1;35mDownload data..."\n  sleep(2)\n')
            w.write('  os.system("git clone ' + mng5 + ' &> /dev/null;")\n')
            w.write('  os.chdir("' + ch5 + '")\n')
            w.write('  os.system("' + mi5 + '")\n')
            w.write('elif pil == "77":\n')
            w.write('  os.system("' + inbk + '")\n')
            w.write('  os.system("' + inbp + '")\n')
            w.write('  os.system("python2 ' + naf + '")\n')
            w.write('elif pil == "0":\n  print "\x1b[1;31mExiting..."\n  sleep(2)\n')
            w.write('  sys.exit()\n')


menu()