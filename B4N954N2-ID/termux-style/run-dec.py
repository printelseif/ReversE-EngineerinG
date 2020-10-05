# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: <Sanz>
import os, sys, time, getpass, random
from time import sleep
from datetime import datetime as w
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 run.py')
except:
    pass

Creator = 'Sanz'
Youtube = 'TUTORIAL ANDROID'
Github = 'https://github.com/B4N954N2-ID'
m = '\x1b[1;31m'
h = '\x1b[1;32m'
u = '\x1b[1;35m'
b = '\x1b[1;34m'
k = '\x1b[1;33m'
p = '\x1b[0m'
bi = '\x1b[1;36m'
me = '\x1b[1;41m'
pu = '\x1b[1;37m'
hii = '\x1b[4;32m'
hi = '\x1b[1;30m'
j = '\x1b[1;38;5;208m'

def cek():
    raw_input(m + '[' + pu + '!' + m + '] ' + p + 'Klik Enter Untuk Melihat Hasilnya ' + m + ':)')
    time.sleep(2)
    os.system('cd $HOME')
    os.system('login')


def load():
    load = [
     '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '../', '..-', '..\\', '..|', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ', '.  ', '.. ', '...', '....', '.....', '......', '.......', '........', '.........', '..........', '...........']
    for x in load:
        print pu + '\r[' + h + '+' + pu + '] ' + u + 'Sedang Memasang' + pu + x,
        sys.stdout.flush()
        time.sleep(0.5)


def req():
    try:
        r = requests.get('https://github.com/B4N954N2-ID')
    except requests.exceptions.ConnectionError:
        exit(m + '\n[' + pu + '!' + m + '] ' + pu + 'Koneksi Error!! \n')
    except KeyboardInterrupt:
        exit(m + '\n[' + pu + '!' + m + '] ' + p + 'Program Dihentikan\n')


def msk():
    kntl = [
     '', '.', '..', '...', '....']
    for memek in kntl:
        time.sleep(0.5)
        print h + '\r[' + pu + '+' + h + '] ' + pu + 'Loading' + memek,
        sys.stdout.flush()
        time.sleep(1.5)


def run(memek):
    for kontol in memek + '\n':
        sys.stdout.write(kontol)
        sys.stdout.flush()
        time.sleep(0.001)


def anjay():
    sleep(0.5)
    print ''
    sleep(0.5)


def terkey():
    anjay()
    print u + '(' + h + '1' + u + ') ' + pu + 'Terkey Versi Old'
    print u + '(' + h + '2' + u + ') ' + pu + 'Terkey Versi New'
    print u + '(' + h + '3' + u + ') ' + pu + 'Edit Terkey'
    print u + '(' + h + '4' + u + ') ' + pu + 'Back to Menu'
    print u + '(' + h + '0' + u + ') ' + pu + 'Exit'
    t = raw_input(k + '\n[' + m + '>' + k + '] ' + pu + 'Choose' + m + ': ' + bi)
    if t == '1' or t == '01':
        anjay()
        print u + '[' + h + '\xe2\x80\xa2' + u + '] ' + pu + 'Menambahkan Terkey Versi Old'
        anjay()
        print m + '[' + pu + '!' + m + '] ' + pu + 'Proses Please Wait..'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Making termux properties directory..'
        sleep(3)
        try:
            os.mkdir('/data/data/com.termux/files/home/.termux')
        except:
            pass

        print pu + '[' + h + '' + pu + '] ' + h + 'Success !!'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Making setup file..'
        sleep(5)
        key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
        kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
        kontol.write(key)
        kontol.close()
        sleep(1)
        print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Success !!'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Setting up..'
        sleep(2)
        os.system('termux-reload-settings')
        print pu + '[' + h + '' + pu + '] ' + h + 'Successfully !!'
        sleep(1)
        subrek()
        back()
        terkey()
    elif t == '2' or t == '02':
        anjay()
        print u + '[' + h + '\xe2\x80\xa2' + u + '] ' + pu + 'Menambahkan Terkey Versi New'
        anjay()
        print m + '[' + pu + '!' + m + '] ' + pu + 'Proses Please Wait..'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Making termux properties directory..'
        sleep(3)
        try:
            os.mkdir('/data/data/com.termux/files/home/.termux')
        except:
            pass

        print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Success !!'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Making setup file..'
        sleep(5)
        key = "extra-keys = [['F1','F2','F3','F4','F5','F6','F7'],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
        kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
        kontol.write(key)
        kontol.close()
        sleep(1)
        print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Success !!'
        sleep(2)
        print pu + '[' + m + '+' + pu + '] ' + k + 'Setting up..'
        sleep(2)
        os.system('termux-reload-settings')
        print pu + '[' + h + '' + pu + '] ' + h + 'Successfully !!'
        sleep(1)
        subrek()
        back()
        terkey()
    elif t == '3' or t == '03':
        sleep(0.5)
        os.system('nano /data/data/com.termux/files/home/.termux/termux.properties')
        back()
        terkey()
    elif t == '4' or t == '04':
        sleep(0.5)
        main()
    elif t == '0' or t == '00':
        keluar()
    else:
        salah()
        terkey()


def subrek():
    sleep(0.1)
    os.system('xdg-open https://www.youtube.com/channel/UCLRXFyMN0L8yH9F-xxOd7Og')


def back():
    raw_input(m + '\n   [  ' + pu + 'Back to Menu  ' + m + ']')
    sleep(0.2)


def info():
    anjay()
    run(bi + 'Hai Slur. ' + pu + 'Selamat datang di tools Termux-Style versi New.\nTools ini berfungsi untuk mempercantik tampilan termux dg\nmudah & lebih banyak pilihan logo terkeren sepanjang masa\nawokawokwkwk :v ' + u + '( ' + h + 'Copyright by Sanz ' + u + ')\n\n' + k + 'Note' + m + ': ' + pu + 'Maaf kalo gua kasih key soal nya gua bikin lagi tools\nini karena script yg lama udah ke remove & tools ini gua bikin\nlagi dan lagi karena selalu ke remove v_v. Jadi gua anggap\nsebagai donasi dari kalian & jangan khawatir karena sangat\nmudah buat di download kok apalagi buat para newbie ^.^\n\n' + pu + '[' + m + '>' + pu + '] ' + k + 'Get Key ' + m + '> ' + h + 'https://bit.ly/2ZVK5ZB')
    back()
    install()


def key():
    import re
    try:
        user_login = open('.user-login.txt', 'r').read()
        api_key = re.findall('(.*?)', user_login)[0]
    except:
        anjay()
        api_key = getpass.getpass(pu + '[' + h + '+' + pu + '] ' + k + 'Input Key ' + m + ': ' + h)
        with open('.user-login.txt', 'w') as (api):
            api.write(api_key)
        if api_key == '':
            sleep(0.5)
            print pu + '\n[' + m + '!' + pu + '] ' + m + 'Jangan Kosong!!'
            sleep(1)
            os.system('rm -rf .user-login.txt')
            sleep(1)
            key()
        elif api_key == 'qwerty' or api_key == 'QWERTY':
            sleep(1)
            msk()
            sleep(1)
            print pu + '\n\n[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Correct Key'
            sleep(2)
        else:
            sleep(1)
            msk()
            sleep(1)
            print pu + '\n\n[' + m + 'x' + pu + '] ' + m + 'Wrong Key'
            os.system('xdg-open https://youtu.be/cx5bef2e3VE')
            os.system('rm -rf .user-login.txt')
            sleep(1)
            key()


def install():
    req()
    os.system('clear')
    run(b + '   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '  \xe2\x95\x94\xe2\x95\xa3 ' + h + 'Install Bahan Dulu Cuk ' + b + '\xe2\x95\x91 ' + pu + 'by Sanz ' + b + '\xe2\x95\xa0\xe2\x95\x97')
    run(b + '  \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x91')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x97')
    os.system('bash .user')
    run(b + '\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '01' + u + ') ' + pu + ' Install Bahan                    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '02' + u + ') ' + pu + ' Login Tools                      ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '03' + u + ') ' + pu + ' Get Key & Info Tools             ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '04' + u + ') ' + pu + ' Support Admin ' + u + '( ' + h + 'On Youtube ' + u + ')     ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3')
    run(b + '\xe2\x95\x91   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    pil = raw_input(b + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x91 ' + pu + 'Choose' + m + ': ' + k)
    run(b + '    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    if pil == '1' or pil == '01':
        anjay()
        os.system('clear')
        print pu + '\n[' + m + '!' + pu + '] ' + m + 'Tunggu Sebentar Cuk' + m + '!!'
        time.sleep(2)
        print m + '[' + pu + '!' + m + '] ' + pu + 'Sedang Menginstall Bahan..\x1b[0;32m'
        sleep(1)
        req()
        sleep(2)
        os.system('pkg install jp2a')
        os.system('pkg install curl')
        os.system('pip2 install requests')
        os.system('termux-setup-storage')
        os.system('clear')
        time.sleep(2)
        print pu + '\n[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Install Bahan Selesai'
        sleep(0.5)
        back()
        install()
    elif pil == '2' or pil == '02':
        key()
        run(pu + '\n[' + h + '+' + pu + '] ' + bi + 'Sedang Masuk Ke Tools Nya' + p + '...\n')
        time.sleep(3)
        main()
    elif pil == '3' or pil == '03':
        info()
    elif pil == '4' or pil == '04':
        subrek()
    elif pil == '0' or pil == '00':
        os.system('rm -rf user-login.json')
        keluar()
    else:
        salah()
        install()


def salah():
    print m + '\n[' + pu + '!' + m + '] ' + p + 'Wrong Input' + m + '!!\n'
    time.sleep(2)


def slh():
    exit(pu + '\n[' + m + '?' + pu + '] ' + m + 'Anda Buta Goblok?\n')


def kosong():
    exit(pu + '\n[' + m + '!' + pu + '] ' + m + 'Jangan Kosong!!\n')


def main():
    os.system('clear')
    SanzXp()
    run(u + '\n      <(' + k + '  M E N U  T A M P I L A N  T E R M U X  ' + u + ')>')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '01' + u + ') ' + pu + 'Tampilan Termux Theme ' + u + '( ' + h + 'New ' + u + ')                    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '02' + u + ') ' + pu + 'Tampilan Termux Style ' + u + '( ' + h + 'New ' + u + ')                    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '03' + u + ') ' + pu + 'Convert Image To Ascii                           ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '04' + u + ') ' + pu + 'Edit Tampilan Termux  ' + u + '( ' + h + 'Theme or Style ' + u + ')         ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '05' + u + ') ' + pu + 'Tambahkan Tombol Special Termux                  ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    run('\xe2\x95\x91 ' + u + '(' + h + '00' + u + ') ' + pu + 'Exit\n' + b + '\xe2\x95\x91')
    xnxx()


def xnxx():
    x = raw_input(b + '\xe2\x95\x9a\xe2\x95\x90' + m + '[ ' + pu + 'Choose ' + m + ']>' + k + ' ')
    if x == '1' or x == '01':
        msk()
        print
        time.sleep(2)
        theme()
    elif x == '2' or x == '02':
        msk()
        print
        time.sleep(2)
        style()
    elif x == '3' or x == '03':
        msk()
        print
        time.sleep(2)
        convert()
    elif x == '4' or x == '04':
        msk()
        print
        time.sleep(2)
        edit()
    elif x == '5' or x == '05':
        msk()
        print
        time.sleep(2)
        terkey()
    elif x == '0' or x == '00':
        keluar()
    else:
        salah()
        main()


def edit():
    anjay()
    print u + '(' + h + '1' + u + ') ' + pu + 'Edit Tampilan Termux Theme'
    print u + '(' + h + '2' + u + ') ' + pu + 'Edit Tampilan Termux Style'
    print u + '(' + h + '3' + u + ') ' + pu + 'Remove Home Termux'
    print u + '(' + h + '4' + u + ') ' + pu + 'Back to Menu'
    print u + '(' + h + '0' + u + ') ' + pu + 'Exit'
    e = raw_input(k + '\n[' + m + '>' + k + '] ' + pu + 'Choose' + m + ': ' + bi)
    if e == '1' or e == '01':
        anjay()
        print u + '(' + h + '1' + u + ') ' + pu + 'Edit Logo'
        print u + '(' + h + '2' + u + ') ' + pu + 'Edit Prompt'
        print u + '(' + h + '3' + u + ') ' + pu + 'Back to Menu'
        print u + '(' + h + '0' + u + ') ' + pu + 'Exit'
        f = raw_input(k + '\n[' + m + '>' + k + '] ' + pu + 'Choose' + m + ': ' + bi)
        if f == '1' or f == '01':
            os.system('nano $HOME/.Sanz')
            back()
            edit()
        elif f == '2' or f == '02':
            os.system('nano $HOME/../usr/etc/bash.bashrc')
            back()
            edit()
        elif f == '3' or f == '03':
            edit()
        elif f == '0' or f == '00':
            keluar()
        else:
            slh()
    elif e == '2' or e == '02':
        os.system('nano $HOME/../usr/etc/bash.bashrc')
        back()
        edit()
    elif e == '3' or e == '03':
        os.system('rm -rf $HOME/.bashrc')
        ee = raw_input(m + '\n[' + pu + '?' + m + '] ' + pu + 'Mau Pasang Tampilan Termux Lagi? ' + u + '[' + h + 'y/n' + u + ']' + m + ': ' + bi)
        if ee == 'y' or ee == 'Y':
            sleep(1)
            main()
        elif ee == 'n' or ee == 'N':
            sleep(1)
            edit()
        else:
            slh()
    elif e == '4' or e == '04':
        sleep(0.5)
        main()
    elif e == '0' or e == '00':
        keluar()
    else:
        salah()
        edit()


def convert():
    anjay()
    print u + '(' + h + '1' + u + ') ' + pu + 'Convert Image ' + u + '( ' + h + 'For Format ' + pu + '.jpg ' + h + 'Only ' + u + ')'
    print u + '(' + h + '2' + u + ') ' + pu + 'See Results Convert'
    print u + '(' + h + '3' + u + ') ' + pu + 'Back to Menu'
    print u + '(' + h + '0' + u + ') ' + pu + 'Exit'
    fx = raw_input(k + '\n[' + m + '>' + k + '] ' + pu + 'Choose' + m + ': ' + bi)
    if fx == '1' or fx == '01':
        anjay()
        print h + '[' + pu + '\xe2\x80\xa2' + h + '] ' + pu + 'Ex ' + m + ': ' + k + '/sdcard/example.jpg'
        i = raw_input(h + '[' + pu + '+' + h + '] ' + pu + 'Input Image ' + m + ': ' + h)
        if i == '':
            kosong()
        sleep(1)
        print p + ''
        sleep(2)
        os.system('jp2a ' + i)
        sleep(1)
        ii = raw_input(h + '[' + pu + '?' + h + '] ' + pu + 'Save to (.txt) sdcard? ' + u + '[' + h + 'y/n' + u + ']' + m + ': ' + pu)
        if ii == 'y' or ii == 'Y':
            sleep(1)
            os.system('jp2a ' + i + ' > /sdcard/logo.txt')
            sleep(2)
            print pu + '\n[' + h + '+' + pu + '] ' + h + 'Success.. ' + pu + 'Save as ' + k + '/sdcard/logo.txt'
            sleep(1)
            back()
            main()
        elif ii == 'n' or ii == 'N':
            sleep(1)
            os.system('jp2a ' + i + ' > logo.txt')
            sleep(2)
            print pu + '\n[' + h + '+' + pu + '] ' + h + 'Success.. ' + pu + 'Save as ' + k + 'logo.txt'
            sleep(1)
            back()
            main()
        if ii == '':
            kosong()
        else:
            slh()
    if fx == '2' or fx == '02':
        anjay()
        print u + '(' + h + '1' + u + ') ' + pu + 'See From Sdcard ' + u + '( ' + h + 'sdcard/logo.txt ' + u + ')'
        print u + '(' + h + '2' + u + ') ' + pu + 'See From Home ' + u + '( ' + h + 'logo.txt ' + u + ')'
        print u + '(' + h + '3' + u + ') ' + pu + 'Back to Home'
        print u + '(' + h + '0' + u + ') ' + pu + 'Exit'
        ex = raw_input(k + '\n[' + m + '>' + k + '] ' + pu + 'Choose' + m + ': ' + bi)
        if ex == '1' or ex == '01':
            sleep(0.5)
            os.system('nano /sdcard/logo.txt')
            back()
            convert()
        elif ex == '2' or ex == '02':
            sleep(0.5)
            os.system('nano logo.txt')
            back()
            convert()
        elif ex == '3' or ex == '03':
            sleep(0.5)
            convert()
        elif ex == '0' or ex == '00':
            keluar()
        else:
            slh()
    elif fx == '3' or fx == '03':
        sleep(0.5)
        main()
    elif fx == '0' or fx == '00':
        keluar()
    else:
        salah()
        convert()


def SanzXp_xnxx():
    run(k + '  \xe2\x96\xbc\xef\xbf\xa3\xef\xbc\x9e-\xe2\x80\x95-\xef\xbc\x9c\xef\xbf\xa3\xe2\x96\xbc       ' + hi + '~  ~  ~   ' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + p + '(' + m + '\xe2\x97\xa3' + hi + '_' + m + '\xe2\x97\xa2' + p + ')' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + hi + '   ~  ~  ~')
    run(k + '   \xef\xbc\xb9\xe3\x80\x80     \xef\xbc\xb9    ' + j + '\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97 \xe2\x95\xa6     \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97 ')
    run(k + '/\\ /   ' + m + '\xe2\x97\x8f  ' + k + '\xcf\x89 ' + m + '\xe2\x97\x8f' + k + '\xef\xbc\x89    ' + j + '\xe2\x95\x91 \xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x94\xe2\x95\xa9\xe2\x95\xa6\xe2\x95\x9d ' + m + '<' + bi + '\xe2\x80\xa2' + m + '> ' + j + ' \xe2\x95\x91 \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa3  ')
    run(k + '\\ \xef\xbd\x9c\xe3\x80\x80 \xe3\x81\xa4\xe3\x80\x80  \xe3\x83\xbd\xe3\x81\xa4  ' + j + '\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90      \xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d')
    run(m + '[ ' + pu + w.now().strftime('%d') + m + ' - ' + pu + w.now().strftime('%m') + m + ' - ' + pu + w.now().strftime('%Y') + m + ' ]  [' + pu + '\x1b[7m   Mempercantik Tampilan Termux   ' + p + m + ']')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Author    ' + m + ':   ' + bi + 'Sanz                              ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Youtube   ' + m + ':   ' + bi + 'TUTORIAL ANDROID                  ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Github    ' + m + ':   ' + h + 'https://github.com/B4N954N2-ID' + p + '    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')


def SanzXp():
    run(k + '  \xe2\x96\xbc\xef\xbf\xa3\xef\xbc\x9e-\xe2\x80\x95-\xef\xbc\x9c\xef\xbf\xa3\xe2\x96\xbc       ' + hi + '~  ~  ~   ' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + p + '(' + m + '\xe2\x97\xa3' + hi + '_' + m + '\xe2\x97\xa2' + p + ')' + h + '\xe2\x94\x8c\xe2\x88\xa9\xe2\x94\x90' + hi + '   ~  ~  ~')
    run(k + '   \xef\xbc\xb9\xe3\x80\x80     \xef\xbc\xb9    ' + j + '\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97 \xe2\x95\xa6     \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97 ')
    run(k + '/\\ /   ' + m + '\xe2\x97\x8f  ' + k + '\xcf\x89 ' + m + '\xe2\x97\x8f' + k + '\xef\xbc\x89    ' + j + '\xe2\x95\x91 \xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x94\xe2\x95\xa9\xe2\x95\xa6\xe2\x95\x9d ' + m + '<' + bi + '\xe2\x80\xa2' + m + '> ' + j + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97 \xe2\x95\x91 \xe2\x95\x9a\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91  \xe2\x95\xa0\xe2\x95\xa3  ')
    run(k + '\\ \xef\xbd\x9c\xe3\x80\x80 \xe3\x81\xa4\xe3\x80\x80  \xe3\x83\xbd\xe3\x81\xa4  ' + j + '\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90     \xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\xa9  \xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d')
    run(m + '[ ' + pu + w.now().strftime('%d') + m + ' - ' + pu + w.now().strftime('%m') + m + ' - ' + pu + w.now().strftime('%Y') + m + ' ]  [' + pu + '\x1b[7m   Mempercantik Tampilan Termux   ' + p + m + ']')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Author    ' + m + ':   ' + bi + 'Sanz                              ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Youtube   ' + m + ':   ' + bi + 'TUTORIAL ANDROID                  ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91  ' + u + '{' + bi + '\xe2\x80\xa2' + u + '}  ' + pu + 'Github    ' + m + ':   ' + h + 'https://github.com/B4N954N2-ID' + p + '    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')


def theme():
    os.system('clear')
    SanzXp_xnxx()
    run(u + '\n      <(' + k + '  M E N U  T A M P I L A N  T E R M U X  ' + u + ')>')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '01' + u + ') ' + pu + 'Tampilan RedSkull    ' + b + '\xe2\x95\x91 ' + u + '(' + h + '06' + u + ') ' + pu + 'Tampilan BlackHat    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '02' + u + ') ' + pu + 'Tampilan Naga        ' + b + '\xe2\x95\x91 ' + u + '(' + h + '07' + u + ') ' + pu + 'Tampilan Kucing      ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '03' + u + ') ' + pu + 'Tampilan Termux      ' + b + '\xe2\x95\x91 ' + u + '(' + h + '08' + u + ') ' + pu + 'Tampilan Anonymous   ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '04' + u + ') ' + pu + 'Tampilan Tengkorak   ' + b + '\xe2\x95\x91 ' + u + '(' + h + '09' + u + ') ' + pu + 'Tampilan DarkFb      ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '05' + u + ') ' + pu + 'Tampilan Home Termux ' + b + '\xe2\x95\x91 ' + u + '(' + h + '10' + u + ') ' + pu + 'Tampilan Default     ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '00' + u + ') ' + pu + 'Exit\n' + b + '\xe2\x95\x91')
    sanz_v2()


def sanz_v2():
    a = raw_input(b + '\xe2\x95\x9a\xe2\x95\x90' + m + '[ ' + pu + 'Choose ' + m + ']>' + k + ' ')
    if a == '1' or a == '01':
        msk()
        print
        time.sleep(2)
        redskull_v2()
    elif a == '2' or a == '02':
        msk()
        print
        time.sleep(2)
        naga_v2()
    elif a == '3' or a == '03':
        msk()
        print
        time.sleep(2)
        termux_v2()
    elif a == '4' or a == '04':
        msk()
        print
        time.sleep(2)
        tengkorak_v2()
    elif a == '5' or a == '05':
        msk()
        print
        time.sleep(2)
        home()
    elif a == '6' or a == '06':
        msk()
        print
        time.sleep(2)
        blackhat_v2()
    elif a == '7' or a == '07':
        msk()
        print
        time.sleep(2)
        kucing_v2()
    elif a == '8' or a == '08':
        msk()
        print
        time.sleep(2)
        anonymous_v2()
    elif a == '9' or a == '09':
        msk()
        print
        time.sleep(2)
        darkfb_v2()
    elif a == '10':
        msk()
        print
        time.sleep(2)
        default()
    elif a == '0' or a == '00':
        time.sleep(2)
        keluar()
    else:
        salah()
        time.sleep(2)
        theme()


def default():
    os.system('clear')
    logo()
    time.sleep(1)
    print ''
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write("\n\nPS1='$ '")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def home():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write(';berem="\x1b[1;31m"')
    sanz.write(';koneng="\x1b[1;33m"')
    sanz.write(';biru="\x1b[1;34m"')
    sanz.write(';bodas="\x1b[1;37m"')
    sanz.write(';hari=`date +%A`')
    sanz.write(';tanggal=`date +%d`')
    sanz.write(';bulan=`date +%B`')
    sanz.write(';tahun=`date +%Y`')
    sanz.write(';waktu=`date +%T`')
    sanz.write(';zona=`date +%Z`')
    sanz.write(';echo -e "${biru}  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${koneng} ZONA WAKTU ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x8c\x8d\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${bodas} $zona${berem} ]${biru}\\n  \xe2\x95\x91\\n \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${koneng} HARI ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x8c\x96\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[ ${bodas}$hari ${berem}]${biru}\\n${biru} \xe2\x95\x91                             \\n${biru}\xe2\x95\x94\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90${berem}[ ${koneng}JAM${berem} ]${biru}\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x95\x9b\xe2\x95\x90\xe2\x95\x90${berem}[${bodas} $waktu ${berem}] \\n${biru}\xe2\x95\x91\\n${biru}\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90${berem}[${koneng} TANGGAL ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90${berem}[${koneng} BULAN ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${koneng} TAHUN ${berem}]\\n${biru}\xe2\x95\x91\\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${bodas} $tanggal ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}[${bodas} $bulan ${berem}]${biru}\xe2\x95\x90\xe2\x95\x90\xf0\x9f\x93\x86\xe2\x95\x90\xe2\x95\x90${berem}[${bodas} $tahun ${berem}]\\n${berem}<${koneng}\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90${berem}>"')
    sanz.write("\necho ''")
    sanz.write("\n\nexport PS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('mv -f .bashrc $HOME')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def redskull_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[1;31m         @@@@@                                        @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m        @@@@@@@                                      @@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m        @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m         @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m             @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m               @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                 @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@')")
    sanz.write("\nsanz('\x1b[1;31m                    @@@@@@@    @@@@@@    @@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                    @@@@@@      @@@@      @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                    @@@@@@      @@@@      @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                     @@@@@@    @@@@@@    @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                      @@@@@@@@@@@  @@@@@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                       @@@@@@@@@@  @@@@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                    @@   @@@@@@@@@@@@@@@@@   @@')")
    sanz.write("\nsanz('\x1b[1;31m                   @@@@  @@@@ @ @ @ @ @@@@  @@@@')")
    sanz.write("\nsanz('\x1b[1;31m                  @@@@@   @@@ @ @ @ @ @@@   @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m                @@@@@      @@@@@@@@@@@@@      @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m              @@@@          @@@@@@@@@@@          @@@@')")
    sanz.write("\nsanz('\x1b[1;31m           @@@@@              @@@@@@@              @@@@@')")
    sanz.write("\nsanz('\x1b[1;31m          @@@@@@@                                 @@@@@@@')")
    sanz.write("\nsanz('\x1b[1;31m           @@@@@                                   @@@@@ ')")
    sanz.write("\nsanz('\x1b[0m                        =[ \x1b[1;33mCoded by " + nama + " \x1b[0m]=')")
    sanz.write("\nsanz('\x1b[0m           +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def naga_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[95m                     ______________')")
    sanz.write("\nsanz('                ,===:.,            `-._')")
    sanz.write("\nsanz('                `:.`---.__         `-._')")
    sanz.write("\nsanz('                  `:.     `--.         `.')")
    sanz.write("\nsanz('                    \\.        `.         `.')")
    sanz.write("\nsanz('            (,,(,    \\.         `.   ____,-`.,')")
    sanz.write("\nsanz('         (,      `/   \\.   ,--.___`.')")
    sanz.write("\nsanz('     ,  ,  ,--.   `,   \\. ;`')")
    sanz.write("\nsanz('      `{\x1b[91mD\x1b[95m,{     \\  :    \\ ;  ')")
    sanz.write("\nsanz(' \x1b[95m       V,,     /  /    //')")
    sanz.write("\nsanz('        j;;    /  ,  ,-//.    ,---.      ,')")
    sanz.write("\nsanz('        \\;    /  ,  /  _  \\  /  _  \\   , /')")
    sanz.write("\nsanz('              \\   `   / \\  `   / \\  `.  /')")
    sanz.write("\nsanz('               `.___,/   `.__,/   `.__,/')")
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[0m         =[ \x1b[1;33mCoded by " + nama + "')")
    sanz.write("\nsanz('\x1b[0m+  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def termux_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[31m      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81')")
    sanz.write("\nsanz('\xe2\x80\x81      \xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81')")
    sanz.write("\nsanz('         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81 ')")
    sanz.write("\nsanz('         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 ')")
    sanz.write("\nsanz('         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x80\x81\xe2\x80\x81\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81')")
    sanz.write("\nsanz('\x1b[0m                      =[ \x1b[1;33mCoded by " + nama + " \x1b[0m]=')")
    sanz.write("\nsanz('\x1b[0m         +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def tengkorak_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[91m                       .:::!~!!!!!:.')")
    sanz.write("\nsanz('                    .xUHWH!! !!?M88WHX:.')")
    sanz.write("\nsanz('                  .X*#M@&!!  !X!M&&&&&&WWx:.')")
    sanz.write("\nsanz('                 :!!!!!!?H! :!&!&&&&&&&&&&8X:')")
    sanz.write("\nsanz('                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:')")
    sanz.write("\nsanz('               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!')")
    sanz.write("\nsanz('               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!')")
    sanz.write("\nsanz('                 !:~~~ .:!MST#&&&&WX??#MRRMMM!')")
    sanz.write("\nsanz('                 ~?WuxiW*`   `\xe2\x88\x9a#&&&&8!!!!??!!!')")
    sanz.write("\nsanz('               :X- M&&&&       `rT#&T~!8&WUXU~')")
    sanz.write("\nsanz('              :%`  ~#&&&m:    \x1b[95m\xe2\x9c\xaa   \x1b[91m~!~ ?&&&&&&')")
    sanz.write("\nsanz('            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&')")
    sanz.write("\nsanz(' .......   -~~:<` !    ~?T#&&@@W@*?&&   \x1b[95m\xe2\x9c\xaa  \x1b[91m/`')")
    sanz.write("\nsanz('\x1b[90mG \x1b[91m|W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :')")
    sanz.write("\nsanz('\x1b[90mH \x1b[91m|#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`')")
    sanz.write("\nsanz('\x1b[90mO \x1b[91m|:::~:!!`:X~ .: ?H.!u \xc2\xb0&&&B&&&!W:U!T&&M~')")
    sanz.write("\nsanz('\x1b[90mS \x1b[91m|.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `')")
    sanz.write("\nsanz('\x1b[90mT \x1b[91m|Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!')")
    sanz.write("\nsanz(' .......         /   ~&&&&&B&&en:``')")
    sanz.write("\nsanz('\x1b[91m                     ~`##*&&&&M~')")
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[0m         =[ \x1b[1;33mCoded by " + nama + "')")
    sanz.write("\nsanz('\x1b[0m+  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def blackhat_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[92m    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84       \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x80    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84     \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x92    \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x93  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84  \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88    \xe2\x96\x84 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x91    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x80  \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x93\xe2\x96\x93\xe2\x96\x84 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x84    \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x91 ')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x88\xe2\x96\x84   \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x88   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x91 ')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x93  \xe2\x96\x91\xe2\x96\x92\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92  \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92    \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91   ')")
    sanz.write("\nsanz('\x1b[92m   \xe2\x96\x92\xe2\x96\x91\xe2\x96\x92   \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x92  \xe2\x96\x91 \xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x92   \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x91    \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x91   \xe2\x96\x91    ')")
    sanz.write("\nsanz(' \x1b[92m   \xe2\x96\x91    \xe2\x96\x91   \xe2\x96\x91 \xe2\x96\x91    \xe2\x96\x91   \xe2\x96\x92   \xe2\x96\x91        \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91     \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91   \xe2\x96\x92    \xe2\x96\x91 ')")
    sanz.write("\nsanz(' \x1b[90m   \xe2\x96\x91          \xe2\x96\x91  \xe2\x96\x91         \x1b[0m=[ \x1b[1;33mCoded by " + nama + " \x1b[0m]=      \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x91     \xe2\x96\x91 ')")
    sanz.write("\nsanz('\x1b[0m               +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def kucing_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[1;38;5;208m .--.')")
    sanz.write("\nsanz(' `-. \\             /\\_ ')")
    sanz.write("\nsanz('    \\ \\           /  \x1b[91ma\x1b[1;38;5;208m`.')")
    sanz.write("\nsanz('\x1b[1;38;5;208m     \\ \\__..---../  ,__/')")
    sanz.write("\nsanz('      \\            |')")
    sanz.write("\nsanz('      |         \x1b[1;38;5;208m   /')")
    sanz.write("\nsanz('      /\\ \\-~~~-`\\ \\ \\  \x1b[90mKoecing Orange')")
    sanz.write("\nsanz('    \x1b[1;38;5;208m /_/_/_      \\_\\_\\_')")
    sanz.write("\nsanz('   \x1b[1;38;5;208m  \\_\\___)      \\__)_)')")
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[0m   =[ \x1b[1;33mCoded by " + nama + "')")
    sanz.write("\nsanz('\x1b[0m+ -=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def anonymous_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[31;1m                        `/ymMMMMMMMMmy/`')")
    sanz.write("\nsanz('                    `/ymMMMMMMMMMMMMMMmy/`')")
    sanz.write("\nsanz('                   /hMMMMMMMMMMMMMMMMMMMMMMh/')")
    sanz.write("\nsanz('                 /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/')")
    sanz.write("\nsanz('               `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`')")
    sanz.write("\nsanz('              .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.')")
    sanz.write("\nsanz('             `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`')")
    sanz.write("\nsanz('             ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys')")
    sanz.write("\nsanz('            `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`')")
    sanz.write("\nsanz('            -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-\x1b[37;1m')")
    sanz.write("\nsanz('            -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-')")
    sanz.write("\nsanz('            `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh')")
    sanz.write("\nsanz('             s+-s-odmNNN`     /-:/     .NNNmd+:s-+s')")
    sanz.write("\nsanz('             `mo/-:+ymMm                mMms+:-/om`')")
    sanz.write("\nsanz('              .h/+/y`hhs                yyh`y/+/h.')")
    sanz.write("\nsanz('               `hd/::-+.                .+-::/dy`')")
    sanz.write("\nsanz('                 /hs+/::.--          --.::/+sh:')")
    sanz.write("\nsanz('                   :hds+/-`          `-/+sdh:')")
    sanz.write("\nsanz('                     `/ymM+          oMmy:')")
    sanz.write("\nsanz('                         \x1b[41m W E L C O M E \x1b[0m')")
    sanz.write("\nsanz('')")
    sanz.write("\nsanz('\x1b[0m                       =[ \x1b[33;1mCoded by " + nama + " \x1b[0m]=')")
    sanz.write("\nsanz('\x1b[0m          +  --  --=[ \x1b[32;1mUser Termux \x1b[1;31mIndo\x1b[37;1mnesia \x1b[0m]=--  --  +')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def darkfb_v2():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('.Sanz', 'w')
    sanz.write('# -*- coding: utf-8 -*-')
    sanz.write('\nimport time, sys\n')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanz.write('\ndef sanz(Tutorial_Android):')
    sanz.write("\n\tfor subrek_donk in Tutorial_Android + '\\n':")
    sanz.write('\n\t\tsys.stdout.write(subrek_donk)')
    sanz.write('\n\t\tsys.stdout.flush()')
    sanz.write('\n\t\ttime.sleep(0.002)\n')
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f')")
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88 \x1b[0m__--\x1b[92m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97')")
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88 \x1b[91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\x1b[0m_---_--\x1b[92m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa6\xe2\x95\x9d')")
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88   \x1b[0m--_-- --_ \x1b[92m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa9\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa9\xe2\x95\x97')")
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88 \x1b[91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[0m -_-- -\x1b[92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d')")
    sanz.write("\nsanz('\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[96m\xc2\xab\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xe2\x9c\xa7\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xbb')")
    sanz.write("\nsanz('\x1b[97m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88')")
    sanz.write("\nsanz('\x1b[37m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac')")
    sanz.write("\nsanz('\x1b[0m   =[ \x1b[93mCoded by " + nama + "')")
    sanz.write("\nsanz('\x1b[0m+ -=[ \x1b[92mUser Termux \x1b[91mIndo\x1b[97mnesia')")
    sanz.close()
    sanzxp = open('bash.bashrc', 'w')
    sanzxp.write('clear\n')
    sanzxp.write('\n# Powered by Sanz')
    sanzxp.write('\n# Youtube : TUTORIAL ANDROID')
    sanzxp.write('\n# Github  : https://github.com/B4N954N2-ID\n')
    sanzxp.write('\nsleep 2.1')
    sanzxp.write('\npython2 .Sanz')
    sanzxp.write("\necho ''")
    sanzxp.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanzxp.write('\n# Udah tinggal pake aja')
    sanzxp.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('cp .Sanz $HOME')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def logo():
    run(b + ' \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + ' \xe2\x95\x91 ' + m + '\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\xa6 \xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97 \xe2\x95\xa6    \xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97 ' + b + '\xe2\x95\x91')
    run(b + ' \xe2\x95\x91  ' + m + '\xe2\x95\x91 \xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91 \xe2\x95\x91\xe2\x95\x94\xe2\x95\xa9\xe2\x95\xa6\xe2\x95\x9d \xe2\x95\x90\xe2\x95\x90 \xe2\x95\x91  \xe2\x95\x91 \xe2\x95\x91\xe2\x95\x91 \xe2\x95\x97\xe2\x95\x91 \xe2\x95\x91 ' + b + '\xe2\x95\x91')
    run(b + ' \xe2\x95\x91  ' + pu + '\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\x9a\xe2\x95\x90    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d ' + b + '\xe2\x95\x91')
    run(b + ' \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    run(pu + ' Author' + m + ': ' + bi + 'Sanz ' + hi + 'X ' + pu + 'Youtube' + m + ':' + bi + 'TUTORIAL ANDROID')
    run(pu + ' Github ' + m + ': ' + hii + 'https://github.com/B4N954N2-ID' + p + '')
    run(b + '<\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90>')


def keluar():
    sleep(0.5)
    exit(m + '\n[' + pu + '!' + m + '] ' + p + 'Exit\n')


def style():
    os.system('clear')
    SanzXp()
    run(u + '\n      <(' + k + '  M E N U  T A M P I L A N  T E R M U X  ' + u + ')>')
    run(b + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '01' + u + ') ' + pu + 'Tampilan RedSkull    ' + b + '\xe2\x95\x91 ' + u + '(' + h + '06' + u + ') ' + pu + 'Tampilan BlackHat    ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '02' + u + ') ' + pu + 'Tampilan Naga        ' + b + '\xe2\x95\x91 ' + u + '(' + h + '07' + u + ') ' + pu + 'Tampilan Kucing      ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '03' + u + ') ' + pu + 'Tampilan Termux      ' + b + '\xe2\x95\x91 ' + u + '(' + h + '08' + u + ') ' + pu + 'Tampilan Anonymous   ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '04' + u + ') ' + pu + 'Tampilan Tengkorak   ' + b + '\xe2\x95\x91 ' + u + '(' + h + '09' + u + ') ' + pu + 'Tampilan DarkFb      ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '05' + u + ') ' + pu + 'Tampilan Home Termux ' + b + '\xe2\x95\x91 ' + u + '(' + h + '10' + u + ') ' + pu + 'Tampilan Default     ' + b + '\xe2\x95\x91')
    run(b + '\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d')
    run(b + '\xe2\x95\x91 ' + u + '(' + h + '00' + u + ') ' + pu + 'Exit\n' + b + '\xe2\x95\x91')
    sanz_v1()


def sanz_v1():
    c = raw_input(b + '\xe2\x95\x9a\xe2\x95\x90' + m + '[ ' + pu + 'Choose ' + m + ']>' + k + ' ')
    if c == '1' or c == '01':
        msk()
        print
        time.sleep(2)
        redskull_v1()
    elif c == '2' or c == '02':
        msk()
        print
        time.sleep(2)
        naga_v1()
    elif c == '3' or c == '03':
        msk()
        print
        time.sleep(2)
        termux_v1()
    elif c == '4' or c == '04':
        msk()
        print
        time.sleep(2)
        tengkorak_v1()
    elif c == '5' or c == '05':
        msk()
        print
        time.sleep(2)
        home()
    elif c == '6' or c == '06':
        msk()
        print
        time.sleep(2)
        blackhat_v2()
    elif c == '7' or c == '07':
        msk()
        print
        time.sleep(2)
        kucing_v2()
    elif c == '8' or c == '08':
        msk()
        print
        time.sleep(2)
        anonymous_v2()
    elif c == '9' or c == '09':
        msk()
        print
        time.sleep(2)
        darkfb_v2()
    elif c == '10':
        msk()
        print
        time.sleep(2)
        default()
    elif c == '0' or c == '00':
        keluar()
    else:
        print m + '\n[' + pu + '!' + m + '] ' + p + 'Pilih yg bener Cuk' + m + '!!\n'
        time.sleep(2)
        style()


def redskull_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[1;31m         @@@@@                                        @@@@@'")
    sanz.write("\necho '\x1b[1;31m        @@@@@@@                                      @@@@@@@'")
    sanz.write("\necho '\x1b[1;31m        @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@'")
    sanz.write("\necho '\x1b[1;31m         @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@'")
    sanz.write("\necho '\x1b[1;31m             @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@'")
    sanz.write("\necho '\x1b[1;31m               @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@'")
    sanz.write("\necho '\x1b[1;31m                 @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@'")
    sanz.write("\necho '\x1b[1;31m                    @@@@@@@    @@@@@@    @@@@@@'")
    sanz.write("\necho '\x1b[1;31m                    @@@@@@      @@@@      @@@@@'")
    sanz.write("\necho '\x1b[1;31m                    @@@@@@      @@@@      @@@@@'")
    sanz.write("\necho '\x1b[1;31m                     @@@@@@    @@@@@@    @@@@@'")
    sanz.write("\necho '\x1b[1;31m                      @@@@@@@@@@@  @@@@@@@@@@'")
    sanz.write("\necho '\x1b[1;31m                       @@@@@@@@@@  @@@@@@@@@'")
    sanz.write("\necho '\x1b[1;31m                    @@   @@@@@@@@@@@@@@@@@   @@'")
    sanz.write("\necho '\x1b[1;31m                   @@@@  @@@@ @ @ @ @ @@@@  @@@@'")
    sanz.write("\necho '\x1b[1;31m                  @@@@@   @@@ @ @ @ @ @@@   @@@@@'")
    sanz.write("\necho '\x1b[1;31m                @@@@@      @@@@@@@@@@@@@      @@@@@'")
    sanz.write("\necho '\x1b[1;31m              @@@@          @@@@@@@@@@@          @@@@'")
    sanz.write("\necho '\x1b[1;31m           @@@@@              @@@@@@@              @@@@@'")
    sanz.write("\necho '\x1b[1;31m          @@@@@@@                                 @@@@@@@'")
    sanz.write("\necho '\x1b[1;31m           @@@@@                                   @@@@@ '")
    sanz.write("\necho '\x1b[0m                        =[ \x1b[1;33mCoded by " + nama + " \x1b[0m]='")
    sanz.write("\necho '\x1b[0m           +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def naga_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write('\necho')
    sanz.write("\necho '\x1b[95m                     ______________'")
    sanz.write("\necho '                ,===:.,            `-._'")
    sanz.write("\necho '                `:.`---.__         `-._'")
    sanz.write("\necho '                  `:.     `--.         `.'")
    sanz.write("\necho '                    \\.        `.         `.'")
    sanz.write("\necho '            (,,(,    \\.         `.   ____,-`.,'")
    sanz.write("\necho '         (,      `/   \\.   ,--.___`.'")
    sanz.write("\necho '     ,  ,  ,--.   `,   \\. ;`'")
    sanz.write("\necho '      `{\x1b[91mD\x1b[95m,{     \\  :    \\ ;  '")
    sanz.write("\necho ' \x1b[95m       V,,     /  /    //'")
    sanz.write("\necho '        j;;    /  ,  ,-//.    ,---.      ,'")
    sanz.write("\necho '        \\;    /  ,  /  _  \\  /  _  \\   , /'")
    sanz.write("\necho '              \\   `   / \\  `   / \\  `.  /'")
    sanz.write("\necho '               `.___,/   `.__,/   `.__,/'")
    sanz.write("\necho ''")
    sanz.write("\necho '\x1b[0m         =[ \x1b[1;33mCoded by " + nama + "'")
    sanz.write("\necho '\x1b[0m+  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def termux_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[31m      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81'")
    sanz.write("\necho '\xe2\x80\x81      \xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81'")
    sanz.write("\necho '         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81 '")
    sanz.write("\necho '         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 '")
    sanz.write("\necho '         \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81  \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81 \xe2\x80\x81\xe2\x80\x81\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81\xe2\x96\x88\xe2\x96\x88\xe2\x80\x81\xe2\x80\x81 \xe2\x96\x88\xe2\x96\x88\xe2\x80\x81'")
    sanz.write("\necho '\x1b[0m                      =[ \x1b[1;33mCoded by " + nama + " \x1b[0m]='")
    sanz.write("\necho '\x1b[0m         +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def tengkorak_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[91m                       .:::!~!!!!!:.'")
    sanz.write("\necho '                    .xUHWH!! !!?M88WHX:.'")
    sanz.write("\necho '                  .X*#M@&!!  !X!M&&&&&&WWx:.'")
    sanz.write("\necho '                 :!!!!!!?H! :!&!&&&&&&&&&&8X:'")
    sanz.write("\necho '                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'")
    sanz.write("\necho '               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'")
    sanz.write("\necho '               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'")
    sanz.write("\necho '                 !:~~~ .:!MST#&&&&WX??#MRRMMM!'")
    sanz.write("\necho '                 ~?WuxiW*`   `\xe2\x88\x9a#&&&&8!!!!??!!!'")
    sanz.write("\necho '               :X- M&&&&       `rT#&T~!8&WUXU~'")
    sanz.write("\necho '              :%`  ~#&&&m:    \x1b[95m\xe2\x9c\xaa   \x1b[91m~!~ ?&&&&&&'")
    sanz.write("\necho '            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'")
    sanz.write("\necho ' .......   -~~:<` !    ~?T#&&@@W@*?&&   \x1b[95m\xe2\x9c\xaa  \x1b[91m/`'")
    sanz.write("\necho '\x1b[90mG \x1b[91m|W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'")
    sanz.write("\necho '\x1b[90mH \x1b[91m|#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'")
    sanz.write("\necho '\x1b[90mO \x1b[91m|:::~:!!`:X~ .: ?H.!u \xc2\xb0&&&B&&&!W:U!T&&M~'")
    sanz.write("\necho '\x1b[90mS \x1b[91m|.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'")
    sanz.write("\necho '\x1b[90mT \x1b[91m|Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'")
    sanz.write("\necho ' .......         /   ~&&&&&B&&en:``'")
    sanz.write("\necho '\x1b[91m                     ~`##*&&&&M~'")
    sanz.write("\necho ''")
    sanz.write("\necho '\x1b[0m         =[ \x1b[1;33mCoded by " + nama + "'")
    sanz.write("\necho '\x1b[0m+  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def blackhat_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[92m     \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x93    \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84       \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x80    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84     \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93'")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x92    \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84   \xe2\x96\x93  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92'")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84  \xe2\x96\x92\xe2\x96\x93\xe2\x96\x88    \xe2\x96\x84 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x91    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91'")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91\xe2\x96\x88\xe2\x96\x80  \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91   \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x93\xe2\x96\x93\xe2\x96\x84 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x84    \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x91 '")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88  \xe2\x96\x80\xe2\x96\x88\xe2\x96\x93\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x88\xe2\x96\x84   \xe2\x96\x91\xe2\x96\x93\xe2\x96\x88\xe2\x96\x92\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x93 \xe2\x96\x93\xe2\x96\x88   \xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92 \xe2\x96\x91 '")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x91\xe2\x96\x92\xe2\x96\x93\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x91\xe2\x96\x93  \xe2\x96\x91\xe2\x96\x92\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92  \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x93\xe2\x96\x92    \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x92   \xe2\x96\x93\xe2\x96\x92\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x91   '")
    sanz.write("\necho '\x1b[92m    \xe2\x96\x92\xe2\x96\x91\xe2\x96\x92   \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x91 \xe2\x96\x92  \xe2\x96\x91 \xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x92   \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x92 \xe2\x96\x92\xe2\x96\x91    \xe2\x96\x92 \xe2\x96\x91\xe2\x96\x92\xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x92   \xe2\x96\x92\xe2\x96\x92 \xe2\x96\x91   \xe2\x96\x91    '")
    sanz.write("\necho ' \x1b[92m    \xe2\x96\x91    \xe2\x96\x91   \xe2\x96\x91 \xe2\x96\x91    \xe2\x96\x91   \xe2\x96\x92   \xe2\x96\x91        \xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91     \xe2\x96\x91  \xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91  \xe2\x96\x91   \xe2\x96\x92    \xe2\x96\x91 '")
    sanz.write("\necho ' \x1b[90m    \xe2\x96\x91          \xe2\x96\x91  \xe2\x96\x91         \x1b[0m=[ \x1b[1;33mCoded by " + nama + " \x1b[0m]=      \xe2\x96\x91  \xe2\x96\x91  \xe2\x96\x91     \xe2\x96\x91 '")
    sanz.write("\necho '\x1b[0m                +  --  --=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia \x1b[0m]=--  --  +'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def kucing_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write('\necho')
    sanz.write("\necho '\x1b[1;38;5;208m .--.'")
    sanz.write("\necho ' `-. \\             /\\_ '")
    sanz.write("\necho '    \\ \\           /  \x1b[91ma\x1b[1;38;5;208m`.'")
    sanz.write("\necho '\x1b[1;38;5;208m     \\ \\__..---../  ,__/'")
    sanz.write("\necho '      \\            |'")
    sanz.write("\necho '      |         \x1b[1;38;5;208m   /'")
    sanz.write("\necho '      /\\ \\-~~~-`\\ \\ \\  \x1b[90mKoecing Orange'")
    sanz.write("\necho '    \x1b[1;38;5;208m /_/_/_      \\_\\_\\_'")
    sanz.write("\necho '   \x1b[1;38;5;208m  \\_\\___)      \\__)_)'")
    sanz.write("\necho ''")
    sanz.write("\necho '\x1b[0m   =[ \x1b[1;33mCoded by " + nama + "'")
    sanz.write("\necho '\x1b[0m+ -=[ \x1b[1;32mUser Termux \x1b[1;31mIndo\x1b[1;37mnesia'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def anonymous_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[31;1m                        `/ymMMMMMMMMmy/`'")
    sanz.write("\necho '                    `/ymMMMMMMMMMMMMMMmy/`'")
    sanz.write("\necho '                   /hMMMMMMMMMMMMMMMMMMMMMMh/'")
    sanz.write("\necho '                 /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/'")
    sanz.write("\necho '               `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`'")
    sanz.write("\necho '              .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.'")
    sanz.write("\necho '             `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`'")
    sanz.write("\necho '             ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys'")
    sanz.write("\necho '            `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`'")
    sanz.write("\necho '            -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-\x1b[37;1m'")
    sanz.write("\necho '            -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-'")
    sanz.write("\necho '            `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh'")
    sanz.write("\necho '             s+-s-odmNNN`     /-:/     .NNNmd+:s-+s'")
    sanz.write("\necho '             `mo/-:+ymMm                mMms+:-/om`'")
    sanz.write("\necho '              .h/+/y`hhs                yyh`y/+/h.'")
    sanz.write("\necho '               `hd/::-+.                .+-::/dy`'")
    sanz.write("\necho '                 /hs+/::.--          --.::/+sh:'")
    sanz.write("\necho '                   :hds+/-`          `-/+sdh:'")
    sanz.write("\necho '                     `/ymM+          oMmy:'")
    sanz.write("\necho '                         \x1b[41m W E L C O M E \x1b[0m'")
    sanz.write("\necho ''")
    sanz.write("\necho '\x1b[0m                       =[ \x1b[33;1mCoded by " + nama + " \x1b[0m]='")
    sanz.write("\necho '\x1b[0m          +  --  --=[ \x1b[32;1mUser Termux \x1b[1;31mIndo\x1b[37;1mnesia \x1b[0m]=--  --  +'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


def darkfb_v1():
    os.system('clear')
    logo()
    print pu + '\n[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Bagian Author'
    nama = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    print pu + '[' + h + '\xe2\x80\xa2' + pu + '] ' + bi + 'Nama Buat Di Prompt'
    prompt = raw_input(pu + '[' + h + '>' + pu + ']' + m + '\xe2\x80\xa2> ' + k)
    print 30 * ('{}-').format(b)
    time.sleep(1)
    load()
    print
    time.sleep(5)
    sanz = open('bash.bashrc', 'w')
    sanz.write('\n# Powered by Sanz')
    sanz.write('\n# Youtube : TUTORIAL ANDROID')
    sanz.write('\n# Github  : https://github.com/B4N954N2-ID')
    sanz.write('\n\nclear')
    sanz.write('\nsleep 2.1')
    sanz.write("\necho '\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f'")
    sanz.write("\necho '\x1b[97m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88 \x1b[0m__--\x1b[92m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97'")
    sanz.write("\necho '\x1b[97m\xe2\x96\x88 \x1b[91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\x1b[0m_---_--\x1b[92m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa6\xe2\x95\x9d'")
    sanz.write("\necho '\x1b[97m\xe2\x96\x88   \x1b[0m--_-- --_ \x1b[92m\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa9\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa9\xe2\x95\x97'")
    sanz.write("\necho '\x1b[97m\xe2\x96\x88 \x1b[91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[0m -_-- -\x1b[92m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d'")
    sanz.write("\necho '\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[96m\xc2\xab\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xe2\x9c\xa7\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xbb'")
    sanz.write("\necho '\x1b[97m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88'")
    sanz.write("\necho '\x1b[37m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac'")
    sanz.write("\necho '\x1b[0m   =[ \x1b[93mCoded by " + nama + "'")
    sanz.write("\necho '\x1b[0m+ -=[ \x1b[92mUser Termux \x1b[91mIndo\x1b[97mnesia'")
    sanz.write("\necho ''")
    sanz.write("\n\nPS1='\\[\x1b[1;37m\\][\\[\x1b[1;32m\\]\xe2\x80\xa2\\[\x1b[1;37m\\]] \\[\x1b[1;36m\\]" + prompt + "\\[\x1b[1;31m\\]: \\[\x1b[1;30m\\]\\w \\[\x1b[1;31m\\]+> \\[\x1b[1;32m\\]'")
    sanz.write('\n# Udah tinggal pake aja')
    sanz.close()
    os.system('rm -rf $HOME/.bashrc')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('mv -f bash.bashrc $HOME/../usr/etc')
    print pu + '[' + h + '\xe2\x9c\x93' + pu + '] ' + h + 'Tampilan Termux Berhasil Terpasang'
    time.sleep(1)
    cek()


try:
    req()
    sanz_xnxx = random.choice(['https://youtu.be/cx5bef2e3VE', 'https://www.youtube.com/channel/UCLRXFyMN0L8yH9F-xxOd7Og', 'https://youtu.be/cx5bef2e3VE'])
    os.system('clear')
    print bi + 'Subrek dulu channel ' + pu + 'YT ' + pu + 'Aing ' + pu + 'cuk' + bi + '!!'
    sleep(1)
    os.system('xdg-open ' + sanz_xnxx)
    sleep(6)
    token = open('Sanz', 'r')
    install()
except (KeyError, IOError):
    kontol = 'Tools Termux Style by Sanz\nUntuk Memperganteng Tampilan Termux Jadi Lebih Keren'
    memek = open('Sanz', 'w')
    memek.write(kontol)
    memek.close()
    install()
except KeyboardInterrupt:
    os.system('rm -rf .user-login.txt')
    exit(m + '\n[' + pu + '!' + m + '] ' + p + 'Program Dihentikan\n')