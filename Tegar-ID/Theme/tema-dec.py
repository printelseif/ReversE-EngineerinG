# Source Generated with Decompyle++
# File: tema.py (Python 2.7)

import os
import time
import sys
wd = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
YY = '\x1b[33;1m'
GG = '\x1b[32;1m'
WW = '\x1b[0;1m'
RR = '\x1b[31;1m'
CC = '\x1b[36;1m'
B = '\x1b[34m'
Y = '\x1b[33;1m'
G = '\x1b[32m'
W = '\x1b[0;1m'
R = '\x1b[31m'
C = '\x1b[36;1m'

def tik():
    titik = [
        '.   ',
        '..  ',
        '... ',
        '....']
    for o in titik:
        print Y + '\r[' + R + '\xe2\x97\x8f' + Y + '] ' + G + 'Loading ' + B + ' ' + o,
        sys.stdout.flush()
        time.sleep(1)
    


def tik2():
    titik = [
        '.   ',
        '..  ',
        '... ',
        '....',
        '... ',
        '..  ',
        '.   ',
        '    ']
    for o in titik:
        print Y + '\r[' + R + '\xe2\x97\x8f' + Y + '] ' + W + 'Mengecek License ' + o,
        sys.stdout.flush()
        time.sleep(1)
    


def tik3():
    titik = [
        '.   ',
        '..  ',
        '... ',
        '....',
        '... ',
        '..  ',
        '.   ',
        '    ',
        '.   ',
        '..  ',
        '... ',
        '....',
        '... ',
        '..  ',
        '.   ',
        '    ']
    for o in titik:
        print Y + '\r[' + R + '\xe2\x97\x8f' + Y + '] ' + W + 'Proses Membuat Tema ' + o,
        sys.stdout.flush()
        time.sleep(1)
    

logoo = '\n\xe2\x94\x8c \xe2\x94\x98 \xe2\x94\x90 \xe2\x94\x94'
logo = '\x1b[0;1m\n         \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x92\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x92\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n         \xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n         \xe2\x96\x91\xe2\x96\x92\xe2\x96\x84\xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x92\xe2\x96\x90\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\n'
logo2 = '\x1b[0;1m\n        \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n        \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x92\xe2\x96\x90\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\n        \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x80\xe2\x96\x91\xe2\x96\x90\xe2\x96\x88\xe2\x96\x84\n'

def main():
    os.system('clear')
    print logo
    print W + '            Author : Tegar ID'
    print '            Youtube : Dunia Kode\n'
    print '    \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90'
    print '    \xe2\x94\x82     Apakah Sudah Punya License nya       \xe2\x94\x82'
    print '    \xe2\x94\x82 Jika Belum Punya Silahkan Download Dulu  \xe2\x94\x82'
    print '    \xe2\x94\x82 Atau Bisa Minta Ke Author Nya pilih Menu \xe2\x94\x82'
    print '    \xe2\x94\x82            Hubungi Author                \xe2\x94\x82'
    print '    \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98\n'
    print '      [1] Login (Jika Sudah Punya License Nya)'
    print '      [2] Download License (Jika Belum Punya License Nya)'
    print '      [3] Hubungi Author (WhatsApp)'
    print '      [0] Keluar\n'
    print '      [A] About [Y] Youtube [F] Fanspage [I] Instagram\n'
    pilih = raw_input('      [Pilih Menu] : ')
    if pilih == '1':
        license()
    elif pilih == '2':
        print '[!] Membuka Browser'
        time.sleep(1)
        os.system("xdg-open 'https://www.mediafire.com/download/f03666nqizx9zqd'")
        main()
    elif pilih == '3':
        print 'Membuka WhatsApp'
        time.sleep(1)
        os.system("xdg-open 'http://wa.me/6282125068665'")
        main()
    elif pilih == '0':
        os.system('clear')
        exit('Thanks To Use My Project')
    elif pilih == 'A' or pilih == 'a':
        about()
    elif pilih == 'Y' or pilih == 'y':
        print 'Membuka Yotube'
        time.sleep(1)
        os.system("xdg-open 'https://www.youtube.com/channel/UCtw4FMEyTYYll2RyQl6y28w'")
        main()
    elif pilih == 'F' or pilih == 'f':
        print 'Membuka Facebook'
        time.sleep(1)
        os.system("xdg-open 'https://www.facebook.com/duniakode08.official/'")
        main()
    elif pilih == 'I' or pilih == 'i':
        print 'Membuka Instagram'
        time.sleep(1)
        os.system("xdg-open 'https://www.instagram.com/invites/contact/?i=ar648rzby0xl&utm_content=i22qyhl'")
        main()
    else:
        print '[!] Nomor ' + pilih + ' Tidak Tersedia'
        time.sleep(1)
        main()


def about():
    os.system('clear')
    print '       [ About ]'
    print ' Author    : Tegar ID'
    print ' Youtube   : Dunia Kode'
    print ' Fanspage  : Dunia Kode'
    print ' Instagram : @Dunia_Kode'
    print ' Created   : 18/Sep/2020 - 19/Sep/2020'
    print ' NOTE      : Follow My Sosial Media'
    print "             Don't Modified My Project"
    print 'CopyRight Dunia Kode \xc2\xa92020-2030\n'
    balik = raw_input('[Enter Untuk Kembali ke Menu]')
    if balik == '':
        main()
    else:
        main()


def license():
    os.system('clear')
    print logo2
    print '\n'
    license = raw_input('[Masukan Kode Lincense Nya] : ')
    if license == '8s9jd8j38d':
        tik2()
        print '\n[\xe2\x9c\x94] Kode License Cocok Anda Berhasil Login'
        time.sleep(2)
        menutema()
    else:
        tik2()
        print '\n[\xe2\x9c\x96] License Tidak Cocok Silahkan Download License Nya Dulu'
        time.sleep(2)
        main()


def menutema():
    os.system('clear')
    print logo
    print '      Note : Untuk Power Shell Sudah Di Setting Oleh Kami\n'
    print '              [ Tema Yang Tersedia ]\n'
    print '      [1] Tengkorak (versi 1)'
    print '      [2] Ghost'
    print '      [3] Modern (tersedia fitur waktu)'
    print '      [4] Bendera Indonesia'
    print '      [5] Tengkorak (versi 2)'
    print '      [6] Monster (versi 1)'
    print '      [7] Monster (versi 2)'
    print '      [0] Keluar\n'
    tema = raw_input('      [Pilih Tema] : ')
    if tema == '1':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;1m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "\x1b[0;1m\n   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97 \n \xe2\x95\x94\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97 \n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91       CREATED BY DUNIA KODE\n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x91\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x95\x91 \n\xe2\x95\x9a\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\xa6\xe2\x95\x9d \n\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97 \n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91           ${R}AUTHOR ${G}:${W}  %s\n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d           ${W}TEAM   ${G}:${R}  %s\n${W}\xe2\x95\x94\xe2\x95\x90\xe2\x95\xac\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d.\xe2\x96\x92.. \n\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x95\x90\xe2\x95\x90\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe3\x80\x80...\xe2\x96\x92.  \n\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x95\x90\xe2\x95\x90\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe3\x80\x80.\xe2\x96\x92..\n\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\xe2\x96\x92.  \n\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\n\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\n"\nPS1=\'[ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '0':
        os.system('clear')
        exit('Thanks To Use My Project')
    elif tema == '2':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;1m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "${W}\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x88\xe2\x96\x90\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x90\xe2\x94\xbc\xe2\x96\x90\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92     ${Y}CREATED BY DUNIA KODE\n${W}\xe2\x96\x90\xe2\x94\xbc\xe2\x96\x90\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x90\xe2\x96\x84\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x96\x90\xe2\x96\x90\xe2\x96\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c    ${R}AUTHOR ${G}:${W}  %s\n${W}\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92    ${W}TEAM   ${G}:${R}  %s\n${W}\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x90\xe2\x96\x8c\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x90\xe2\x96\x80\xe2\x96\x90\xe2\x96\x92\xe2\x96\x8c\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x92\xe2\x96\x90\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x90\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x8c\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\n\n"\nPS1=\'[ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '4':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;1m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "${W}\n${R}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88     ${Y}CREATED BY DUNIA KODE\n${R}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n${W}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 ${G}[  ${R}LASKAR CYB${W}ER INDONESIA  ${G}]\n${W}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88     ${R}AUTHOR ${G}:${W}  %s\n                      ${W}TEAM   ${G}:${R}  %s\n\n"\nPS1=\'\\[\x1b[0;1m\\][ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '5':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;11m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "${W}\n${R}   ____________\n${R}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n${R}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91          ${Y}CREATED BY DUNIA KODE\n${R}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n${W}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n${W}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n${W}\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x95\x91\n${B}  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97           ${R}AUTHOR ${G}:${W}  %s\n${B}  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n${W}\xc2\xa0  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97\n\xc2\xa0  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x96\x88\xe2\x95\x91           ${W}TEAM   ${G}:${R}  %s\n${W}\xc2\xa0  \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\xac\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x96\x88\xe2\x95\x91\n \xc2\xa0 \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x95\x9a\xe2\x95\x9d\xe2\x96\x88\xe2\x95\x91\n \xc2\xa0 \xe2\x95\x9a\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x90\xe2\x95\x9d\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\x9d\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x95\x91\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88${R}\xe2\x96\x92${WW}.\xef\xbd\xa1oO\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa0\xe2\x95\xa6\xe2\x95\xa6\xe2\x95\xa6\xe2\x95\x97\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0 \xe2\x95\x9a\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0\xc2\xa0  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\n"\nPS1=\'[ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '6':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;11m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "${W}\n${R}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88    ${Y}CREATED BY DUNIA KODE\n${R}\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\n${R}\xe2\x96\x88${W}\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc      ${R}AUTHOR ${G}:${W}  %s\n${R}\xe2\x96\x88\n${W}\xe2\x96\x88${R}\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2      ${W}TEAM   ${G}:${R}  %s\n${W}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n${W}_\xe2\x96\x88____\xe2\x96\x88_\n\n"\n\nPS1=\'[ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '7':
        nama = raw_input('Nama Kamu Untuk Di Tempel Di Banner : ')
        team = raw_input('Nama Team Kamu : ')
        power = raw_input('Tulisan Untuk Di Power Shell : ')
        f = open('.bashrc', 'a')
        f.write('\nwd="\x1b[90;1m" # dark\nGL="\x1b[96;11m" # Blue aqua\nBB="\x1b[34;1m" # Blue light\nYY="\x1b[33;1m" # Yellow light\nGG="\x1b[32;1m" # Green light\nWW="\x1b[0;1m"  # White light      # Kode Warna\nRR="\x1b[31;1m" # Red light\nCC="\x1b[36;1m" # Cyan light\nB="\x1b[34m"    # Blue\nY="\x1b[33;1m"  # Yellow\nG="\x1b[32m"    # Green\nW="\x1b[0;1m"   # White\nR="\x1b[31m"    # Red\nC="\x1b[36;1m"  # Cyan\nclear\necho "${W}\n${R} \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xc2\xa0\n${R} \xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88  \xc2\xa0 ${Y} CREATED BY DUNIA KODE\n${R}_\xe2\x96\x88 ${W}\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc ${R}\xe2\x96\x88\xc2\xa0\n${R}\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c   ${R}AUTHOR ${G}:${W}  %s \xc2\xa0\n${W} \xe2\x96\x88 ${R}\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2 ${W}\xe2\x96\x88\xc2\xa0\n${W} \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xc2\xa0   ${W}TEAM   ${G}:${R}  %s\n${W}  \xe2\x96\x88\xe2\x96\x88___\xe2\x96\x88\xe2\x96\x88\n\n"\nPS1=\'[ \\[\x1b[36;1m\\]%s \\[\x1b[0;1m\\]/ \\[\x1b[31m\\]${PWD/*\\//}\\[\x1b[0;1m\\] ] \\[\x1b[32m\\]> \\[\x1b[0;1m\\]\'\n        ' % (nama, team, power))
        f.close()
        os.system('rm -rf $HOME/.bashrc && mv .bashrc $HOME')
        tik3()
        print W + '\n[\xe2\x9c\x94] Tema Berhasil Terpasang Silahkan Buka Ulang Termux'
    elif tema == '3':
        print '[!] Belum Tersedia, Silahkan Pilih Yang Lain'
        time.sleep(2)
        menutema()
    else:
        print '[!] Nomor ' + tema + ' Tidak Tersedia'
        time.sleep(2)
        menutema()

main()