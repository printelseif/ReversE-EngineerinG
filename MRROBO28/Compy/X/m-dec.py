# uncompyle6 version 3.7.3
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: m.py
# Compiled at: 2020-09-02 15:38:10
# Size of source mod 2**32: 2268 bytes
import marshal, os, time, sys, base64, zlib
from time import sleep
m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
b = '\x1b[1;36m'
p = '\x1b[1;37m'
u = '\x1b[1;35m'

def tik():
    print('\x1b[1;32mPlease wait...')
    sleep(3)


def wr(i):
    for x in i + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(0.001)


banm2 = u" \t\x1b[1;33m  ____                      _ _\n\t / ___|___  _ __ ___  _ __ (_) | ___   _ __  _   _\n\t| |   / _ \\| '_ ` _ \\| '_ \\| | |/ _ \\ | '_ \\| | | |\n\t| |__| (_) | | | | | | |_) | | |  __/ | |_) | |_| |\n\t \\____\\___/|_| |_| |_| .__/|_|_|\\___| | .__/ \\__, |\n\t                     |_|              |_|    |___/ \n\x1b[1;36m\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\n\x1b[1;36m\u2551 \t\x1b[1;37mAuthor  \x1b[1;37m: \x1b[1;32mMRROBO28\x1b[1;36m                   \t\t\u2551\n\x1b[1;36m\u2551 \t\x1b[1;37mgithub  \x1b[1;37m: \x1b[1;32mhttps://github.con/MRROBO28\x1b[1;36m\t\t\u2551\n\x1b[1;36m\u2551 \t\x1b[1;37mYoutube \x1b[1;37m: \x1b[1;32mTEKTRIKBOT CN\x1b[1;36m              \t\t\u2551\n\x1b[1;36m\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d\n\t              \x1b[1;36m[\x1b[1;41m\x1b[1;37mCompile  python3\x1b[00m\x1b[1;36m]\n"

def mar():
    os.system('clear')
    wr(banm2)
    try:
        inp = input(h + 'Ex :/path/file.py\n' + p + '[' + b + '+' + p + ']' + p + 'Input file' + h + ' > ' + h)
        o = input(p + '[' + b + '+' + p + ']' + p + 'Output file' + h + ' > ' + h)
        tik()
        bk = open(inp, 'r').read()
        cp = compile(bk, ' ', 'exec')
        md = marshal.dumps(cp)
        zl = zlib.compress(md)
        cb = base64.b64encode(zl)
        zb = zlib.compress(cb)
        tar = open(o, 'w').write('#compile by MRROBO28\n#Subcribe chanel TEKTRIKBOT CN\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(zlib.decompress(' + repr(zb) + ')))))')
        print(b + 'Sucses Compile file')
    except:
        print(p + '[' + m + '!' + p + ']' + k + 'File tidak ada!!!')
        sleep(4)
        mar()
    else:
        pil = input(k + 'Mau compile lagi?' + h + '(y/t) : ' + p)
        if pil == 'y':
            mar()
        elif pil == 't':
            print(h + 'Thanks for used my script ^_^')
            sleep(0.5)
            print(m + 'Exiting...')
            sleep(2)
            sys.exit()


mar()
# okay decompiling x.pyc
