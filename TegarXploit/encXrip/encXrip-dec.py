# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
import base64, os, marshal, sys, time
os.system('xdg-open https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ/videos?pbjreload=101')

def jalan(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


os.system('clear')
logo = '\n\x1b[31;1m\n  @@@@@@@@ @@@  @@@  @@@@@@@ @@@  @@@ @@@@@@@  @@@ @@@@@@@\n  @@!      @@!@!@@@ !@@      @@!  !@@ @@!  @@@ @@! @@!  @@@\n  @!!!:!   @!@@!!@! !@!       !@@!@!  @!@!!@!  !!@ @!@@!@!\n  !!:      !!:  !!! :!!       !: :!!  !!: :!!  !!: !!:\n  : :: ::: ::    :   :: :: : :::  :::  :   : : :    :\n               \x1b[37;1m=\x1b[32;1m[ \x1b[33;1mAuthor: \x1b[37;1mTegar\x1b[31;1mXploit \x1b[37;1m]\x1b[32;1m=\n \t       \x1b[32;1m=\x1b[37;1m[ \x1b[37;1mSecurity\x1b[31;1mXploit \x1b[32;1mcrew \x1b[32;1m]\x1b[37;1m=\n'
print logo
jalan('\x1b[32;1m1.\x1b[37;1m Encrypt Marshal\n')
jalan('\x1b[32;1m2.\x1b[37;1m Encrypt Base16\n')
jalan('\x1b[32;1m3.\x1b[37;1m Encrypt Base32\n')
jalan('\x1b[32;1m4.\x1b[37;1m Encrypt Base64\n')
jalan('\x1b[32;1m5.\x1b[31;1m Exit\n')

def main():
    choice = raw_input('\x1b[32;1m(\x1b[37;1menc\x1b[31;1mX\x1b[37;1mrip\x1b[32;1m)\x1b[37;1m> \x1b[33;1m')
    if choice == '1' or choice == '01':
        try:
            file = raw_input('\x1b[37;1m[\x1b[32;1m+\x1b[37;1m] \x1b[32;1mFile: \x1b[37;1m')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = 'import marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[37;1m[\x1b[31;1m-\x1b[37;1m] \x1b[37;1mHasil: \x1b[32;1m', c
            main()
        except:
            print '\x1b[32;1m[\x1b[31;1m!\x1b[32;1m] \x1b[31;1mYang Bener Dong'
            sys.exit()
            main()

    if choice == '2' or choice == '02':
        try:
            file = raw_input('\x1b[37;1m[\x1b[32;1m+\x1b[37;1m] \x1b[32;1mFile: \x1b[37;1m')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "import base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[37;1m[\x1b[31;1m-\x1b[37;1m] \x1b[37;1mHasil: \x1b[32;1m', c
            main()
        except:
            print '\x1b[32;1m[\x1b[31;1m!\x1b[32;1m] \x1b[31;1mYang Bener Dong'
            sys.exit()
            main()

    if choice == '3' or choice == '03':
        try:
            file = raw_input('\x1b[37;1m[\x1b[32;1m+\x1b[37;1m] \x1b[32;1mFile: \x1b[37;1m')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "import base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[37;1m[\x1b[31;1m-\x1b[37;1m] \x1b[37;1mHasil: \x1b[32;1m', c
            main()
        except:
            print '\x1b[32;1m[\x1b[31;1m!\x1b[32;1m] \x1b[31;1mYang Bener Dong'
            sys.exit()
            main()

    if choice == '4' or choice == '04':
        try:
            file = raw_input('\x1b[37;1m[\x1b[32;1m+\x1b[37;1m] \x1b[32;1mFile: \x1b[37;1m')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "import base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print '\x1b[37;1m[\x1b[31;1m-\x1b[37;1m] \x1b[37;1mHasil: \x1b[32;1m', c
            main()
        except:
            print '\x1b[32;1m[\x1b[31;1m!\x1b[32;1m] \x1b[31;1mYang Bener Dong'
            sys.exit()
            main()

    if choice == '5' or choice == '05':
        print 'Terima kasih Udah pake'
        time.sleep(2)
        os.system('exit')


if __name__ == '__main__':
    main()