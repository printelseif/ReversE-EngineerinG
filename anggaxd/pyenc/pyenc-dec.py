# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
import os, sys, time, base64, marshal, zlib
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 100)


logo = "\n\x1b[1;91m______      _____                            _   \n\x1b[1;92m| ___ \\    |  ___|                          | |  \n\x1b[1;93m| |_/ /   _| |__ _ __   ___ _ __ _   _ _ __ | |_ \n\x1b[1;95m|  __/ | | |  __| '_ \\ / __| '__| | | | '_ \\| __|\n\x1b[1;96m| |  | |_| | |__| | | | (__| |  | |_| | |_) | |_ \n\x1b[1;93m\\_|   \\__, \\____/_| |_|\\___|_|   \\__, | .__/ \\__|\n\x1b[1;92m       __/ |                      __/ | |        \n\x1b[1;91m      |___/                      |___/|_|                  \n\x1b[1;97m-----------------------------------------------------\n\x1b[1;97m     [\x1b[1;93m*\x1b[1;97m] Author  : Angga Kurniawan\n\x1b[1;97m     [\x1b[1;93m*\x1b[1;97m] GitHub  : https://github.com/anggaxd\n\x1b[1;97m     [\x1b[1;93m*\x1b[1;97m] YouTube : ANGGA KURNIAWAN\n\x1b[1;97m-----------------------------------------------------\n"
anggaxd = '\n \x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Encrypt Marshal\n \x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Encrypt Base64\n \x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mBase32\n \x1b[1;97m[\x1b[1;92m04\x1b[1;97m] Encrypt Zlib\x1b[1;37m,\x1b[1;33mBase64\n \x1b[1;97m[\x1b[1;92m05\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase64\n \x1b[1;97m[\x1b[1;92m06\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase32\n \x1b[1;97m[\x1b[1;92m07\x1b[1;97m] Encrypt Marshal\x1b[1;37m,\x1b[1;33mZlib\x1b[1;37m,\x1b[1;33mBase16\n \x1b[1;97m[\x1b[1;92m00\x1b[1;97m] Exit\n'
os.system('clear')
print logo
slowprint(anggaxd)
mainmenu = raw_input(G + '\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] Select An Option' + C + ' : ' + Y)
if mainmenu == '1' or mainmenu == '01':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    a = compile(fileopen, 'dg', 'exec')
    m = marshal.dumps(a)
    s = repr(m)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal\nexec(marshal.loads(' + s + '))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '2' or mainmenu == '02':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    a = base64.b64encode(fileopen)
    b = "#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport base64\nexec(base64.b64decode('" + a + "'))"
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '3' or mainmenu == '03':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = base64.b32encode(sb)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,base64\nexec(marshal.loads(base64.b32decode("' + str(sc) + '")))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '4' or mainmenu == '04':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    sa = zlib.compress(fileopen)
    sb = base64.b64encode(sa)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport zlib,base64\nexec(zlib.decompress(base64.b64decode("' + sb + '")))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '5' or mainmenu == '05':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b64encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '6' or mainmenu == '06':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b32encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '7' or mainmenu == '07':
    print ''
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print ''
    file = raw_input(G + ' Name of the File to Encrypt' + C + ' > ' + Y)
    print ''
    c = raw_input(G + ' Output File Name' + C + ' > ' + Y)
    print ''
    slowprint(G + ' Encrypting...')
    print ''
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b16encode(sc)
    b = '#Encrypt By Angga Kurniawan (https://github.com/anggaxd)\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(sd) + '"))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print ''
    print G + ' Output File Name : ' + Y, c
    print ''
    print W
elif mainmenu == '0' or mainmenu == '00':
    print ''
    print ''
    slowprint(Y + '  Thanks for using this tool')
    time.sleep(1)
    print ''
    print W
    sys.exit
else:
    print W + ''
    print C + '[' + R + '!' + C + ']' + Y + ' Invalid input ' + C + '[' + R + '!' + C + ']'
    print W