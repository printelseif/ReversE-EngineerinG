
	#-*- coding: utf-8 -*-
import os
import sys
import time
import colorama
from colorama import *

def tm():
   time.sleep(1)

def pt():
   print("")

def clr():
   os.system("clear")

def author():
    print("\033[1;92m")
    print(Fore.RED +"Loading Author Information.....")
 
def logo():
    pt()
    time.sleep(0.3)
    print(Fore.RED +"Loading Author Info + scripts.....")
    time.sleep(2)
    pt()
    os.system("clear")
    print("\033[1;96m")
    print("  _____ __  __  \033[1;93m .::. \033[1;92m[ vulnerability scanner ]\033[1;93m .::.\033[1;96m        ")
    print(" |_   _|  \/  |___  ___ __ _ _ __  _ __   ___ _ __ ")
    print("   | | | |\/| / __|/ __/ _` | '_ \| '_ \ / _ \ '__| ")
    print("   | | | |  | \__ \ (_| (_| | | | | | | |  __/ |   ")
    print("   |_| |_|  |_|___/\___\__,_|_| |_|_| |_|\___|_| v1.0")
    print("")
    print("  \033[1;95m.::.\033[1;97m TM-scanner v1.0 Coded by @TechnicalMujeeb \033[1;95m.::.")
    print(" ")

def main():
    print("\033[1;91m[\033[1;93m1\033[1;91m]> \033[1;92mFTP-Backdoor      \033[1;91m[\033[1;93m2\033[1;91m]> \033[1;92mFirewall Detection ")
    pt()
    print("\033[1;91m[\033[1;93m3\033[1;91m]> \033[1;92mOS Detection      \033[1;91m[\033[1;93m4\033[1;91m]> \033[1;92mHeartBleed") 
    pt()
    print("\033[1;91m[\033[1;93m5\033[1;91m]> \033[1;92mfirewall-bypass   \033[1;91m[\033[1;93m6\033[1;91m]> \033[1;92mssl-poodle")
    pt()
    print("\033[1;91m[\033[1;93m7\033[1;91m]> \033[1;92mwordpress-users   \033[1;91m[\033[1;93m8\033[1;91m]> \033[1;92mXSS-stored ")
    pt()
    print("\033[1;91m[\033[1;93m9\033[1;91m]> \033[1;92mcookie Flags      \033[1;91m[\033[1;93m10\033[1;91m]> \033[1;92mCSRF")
    pt()
    print("\033[1;91m[\033[1;93m11\033[1;91m]> \033[1;92mphpself XSS      \033[1;91m[\033[1;93m12\033[1;91m]> \033[1;92mphpmyadmin traversal")
    pt()
    print("\033[1;91m[\033[1;93m13\033[1;91m]> \033[1;92mDlink Backdoor   \033[1;91m[\033[1;93m14\033[1;91m]> \033[1;92mshellshock")
    pt()
    print("\033[1;91m[\033[1;93m15\033[1;91m]> \033[1;92mSQL injection    \033[1;91m[\033[1;93m16\033[1;91m]> \033[1;92msmtp [cve2011-1764]")
    pt()
    print("\033[1;91m[\033[1;93m17\033[1;91m]> \033[1;92mMy-SQL           \033[1;91m[\033[1;93m18\033[1;91m]> \033[1;92mBotnet channels")
    pt()
    print("\033[1;91m[\033[1;93m19\033[1;91m]> \033[1;92mMacOS-X AFP      \033[1;91m[\033[1;93m20\033[1;91m]> \033[1;92mFtp libopie ")
    pt()
    print("\033[1;91m[\033[1;93m21\033[1;91m]> \033[1;92mDos site ?       \033[1;91m[\033[1;93me\033[1;91m]> \033[1;92mExit ")
    pt()




    op = raw_input("\033[1;91m┌─[\033[1;96mTM-scanner\033[1;91m]\n|\n└────────►\033[1;92m ")
    pt()

    def again():
        pp = raw_input("\033[1;91m┌──[\033[1;96mContinue|Exit=[c/e]\033[1;91m]\n└─────►\033[1;92m ")
        if pp=='e':
            time.sleep(1)
            print("\033[1;91mExiting......")
            print("")
        else:
             print("launching................")
             time.sleep(1)
             os.system("clear")
             logo()
             main()

    if op=='1':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap --script ftp-proftpd-backdoor -p 21 ' + t)
        again()
    elif op=='2':
        tm()
        t = raw_input("\033[1;91m Target Ip : \033[1;92m") 
        os.system('nmap -sA ' + t)
        again()
    elif op=='3':
        tm()
        t = raw_input("\033[1;91m Target Ip : \033[1;92m") 
        os.system('nmap -O ' + t)
        again()
    elif op=='4':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p 443 --script ssl-heartbleed ' + t)
        again()
    elif op=='5':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap --script firewall-bypass ' + t)
        again()
    elif op=='6':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV --version-light --script ssl-poodle -p 443 ' + t)
        again()
    elif op=='7':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p80 --script http-wordpress-users ' + t)
        again()
    elif op=='8':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p80 --script http-stored-xss.nse ' + t)
        again()
    elif op=='9':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p 443 --script http-cookie-flags ' + t)
        again()
    elif op=='10':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p80 --script http-csrf.nse ' + t)
        again()
    elif op=='11':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap --script=http-phpself-xss -p80 ' + t)
        again()
    elif op=='12':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p80 --script http-phpmyadmin-dir-traversal ' + t)
        again() 
    elif op=='13':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV --script http-dlink-backdoor ' + t)
        again()
    elif op=='14':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV -p- --script http-shellshock ' + t)
        again()
    elif op=='15':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV --script=http-sql-injection ' + t)
        again()
    elif op=='16':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap --script=smtp-vuln-cve2011-1764 -pT:25,465,587 ' + t)
        again()
    elif op=='17':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p3306 --script mysql-vuln-cve2012-2122 ' + t)
        again()
    elif op=='18':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -p 6667 --script=irc-botnet-channels ' + t)
        again()
    elif op=='19':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV --script=afp-path-vuln ' + t)
        again()
    elif op=='20':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap -sV --script=ftp-libopie ' + t)
        again()
    elif op=='21':
        tm()
        t = raw_input("\033[1;91m Target : \033[1;92m") 
        os.system('nmap --script dos -Pn ' + t)
        again()
    elif op=='e':
        time.sleep(1)
        print("Exiting........")
        print("")
        time.sleep(1)
    else:
        os.system("clear")
        logo()
        main()

logo()
main()
