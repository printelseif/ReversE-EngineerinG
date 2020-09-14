# uncompyle6 version 3.7.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: bt.py
# Compiled at: 2020-08-20 10:52:48
N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
C = '\x1b[94m'
R = '\x1b[91m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;36m'
import os, sys, fileinput, time, socket, random, time, sys, platform, os

def wr(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 15)


def bn(h):
    for d in h + '\n':
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(1.0 / 100)


def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print

def keluar():
    tampil('\rm[!]Thanks for used my script')
    os.sys.exit()


def dekrip():
    try:
        sc = raw_input(ask + W + 'Masukkan Alamat Input ' + G + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Masukkan Alamat Output' + G + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch tes.sh')
        os.system('bash ' + out + ' > tes.sh')
        os.remove(out)
        os.system('mv -f tes.sh ' + out)
        print sukses + 'Done..'
        pil0 = raw_input('mau lagi?[y/n]')
    except KeyboardInterrupt:
        print eror + ' Stopped!'
    except IOError:
        print eror + ' File Not Found!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Masukan Alamat Script ' + G + '|> ' + W)
        output = raw_input(ask + W + 'Masukan Alamat Output ' + G + '|> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'Berhasil..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Terdeteksi!'


def bahan():
    try:
        wr(G + 'Install bahan dulu...')
        wr(B + 'Loading...')
        os.system('pkg install nodejs -y &> /dev/null;')
        os.system('npm install -g bash-obfuscate &> /dev/null;')
        os.system('python2 bash.py')
    except KeyboardInterrupt:
        print eror + ' Berhenti!'


def menu():
    os.system('clear')
    bn(" \t \x1b[1;33m____            _       _____           _\n\t| __ )  __ _ ___| |__   |_   _|__   ___ | |___  \n\t|  _ \\ / _` / __| '_ \\    | |/ _ \\ / _ \\| / __| \n\t| |_) | (_| \\__ \\ | | |   | | (_) | (_) | \\__ \\ \n\t|____/ \\__,_|___/_| |_|   |_|\\___/ \\___/|_|___/ \n\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n\x1b[1;37m\t\tAuthor  : MRROBO28\n\x1b[1;37m\t\tgithub  : https://github.com/MRROBO28\n\x1b[1;37m\t\tYoutube : TEKTRIKBOT CN\n\x1b[1;36m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n")
    print '\x1b[91m[1]\x1b[97mEncript'
    print '\x1b[91m[2]\x1b[97mDecrypt'
    print '\x1b[91m[3]\x1b[97minstall bahan dulu'
    print '\x1b[91m[0]\x1b[97mKeluar'
    takok = raw_input(W + 'Pilih' + G + ' |> ')
    if takok == '1' or takok == '01':
        enkrip()
    elif takok == '2' or takok == '02':
        dekrip()
    elif takok == '3' or takok == '03':
        bahan()
    elif takok == '0' or tatok == '00':
        keluar()
    else:
        print eror + ' Wrong input'
        keluar()


menu()
# okay decompiling bash.pyc
