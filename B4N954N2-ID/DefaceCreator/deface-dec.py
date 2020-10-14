# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: Sanz
import sys, os, random, time

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)


ngeue = "\x1b[92m\n  ______              ___\n |   _  \\   .-----. .'  _| .---.-. .----. .-----.\n |.  |   \\  |  -__| |   _| |  _  | |  __| |  -__|\n |.  |    \\ |_____| |__|   |___._| |____| |_____| \x1b[97mCreator\x1b[93mv1.0\x1b[92m\n |:  1    / \x1b[97m[\x1b[93mA\x1b[97m]\x1b[93muthor  \x1b[91m: \x1b[96mSanz\x1b[92m\n |::.. . /  \x1b[97m[\x1b[93mY\x1b[97m]\x1b[93mouTube \x1b[91m: \x1b[96mSANZ SOEKAMTI\x1b[92m\n `------'   \x1b[97m[\x1b[93mG\x1b[97m]\x1b[93mitHub  \x1b[91m: \x1b[4;92mhttps://github.com/B4N954N2-ID\x1b[0m\x1b[92m\n"
os.system('termux-setup-storage')
os.system('cd /sdcard')
os.system('clear')
fo = open('jadi.html', 'w')
print ngeue
mengetik('\x1b[90m>>\x1b[92mIsi datanya dengan bener ya,kalo salah nyalahin pembuatnya nanti,entah apa yang merasukimu *_*\n\x1b[90m>>\x1b[92mfill in the data correctly,if wrong blame the creator later, who knows what possessed you *_*\n')
title = raw_input(' \x1b[97mTitle : \x1b[92m')
bg = raw_input(' \x1b[97mBackground Color : \x1b[92m')
gambar = raw_input(' \x1b[97mUrl Gambar : \x1b[92m')
nick = raw_input(' \x1b[97mNick : \x1b[92m')
pesan = raw_input(' \x1b[97mPesan : \x1b[92m')
team = raw_input(' \x1b[97mNama Team : \x1b[92m')
email = raw_input(' \x1b[97mEmail / Cp : \x1b[92m')
lagu = raw_input(' \x1b[97mLink lagu : \x1b[92m')
pesan1 = '<html><head><title>'
pesan2 = title
pesan3 = '</title></head>'
pesan4 = '<body><br><link href=\'http://fonts.googleapis.com/css?family=Iceland\' rel=\'stylesheet\' type=\'text/css\'>\n<style>body{cursor:url("../www.madleets.com/elhacker.cur"),auto;}html{display:table;height:100%;width:100%;}body{display:table-row;}body{display:table-cell;vertical-align:middle;text-align:center;}a:link{text-decoration:none;}</style>\n</p>\n<center>&nbsp;</center>\n<body bgcolor='
pesan5 = bg
pesan6 = '><center><img src='
pesan7 = gambar
pesan8 = " width='400px' height='400px'><br>"
pesan9 = '<font face="Iceland" style="color:red;text-shadow:0px 1px 5px #000;font-size:60px">'
pesan10 = nick
pesan11 = '</font></p>'
pesan12 = '<p><font face="Iceland" style="font-size: 30px" color="white">'
pesan13 = pesan
pesan14 = '</font></p>'
pesan15 = '<p><font face="Iceland" style="font-size: 25px" color="silver">'
pesan16 = team
pesan17 = '</font></p>'
pesan18 = '<p><font face="Iceland" style="font-size: 20px" color="silver">'
pesan19 = email
pesan20 = '<iframe width="0" height="0" src='
pesan21 = lagu
pesan22 = '&autoplay=1" frameborder="0"></iframe>'
pesan23 = '</font></p><br></center></body></html>'
fo.write(pesan1)
fo.write(pesan2)
fo.write(pesan3)
fo.write(pesan4)
fo.write(pesan5)
fo.write(pesan6)
fo.write(pesan7)
fo.write(pesan8)
fo.write(pesan9)
fo.write(pesan10)
fo.write(pesan11)
fo.write(pesan12)
fo.write(pesan13)
fo.write(pesan14)
fo.write(pesan15)
fo.write(pesan16)
fo.write(pesan17)
fo.write(pesan18)
fo.write(pesan19)
fo.write(pesan20)
fo.write(pesan21)
fo.write(pesan22)
fo.write(pesan23)
mengetik('\x1b[92mScript Deface HTML sudah berhasil dibuat...\nSubscribe Channel YouTube Sanz Soekamti')
print
fo.close()
