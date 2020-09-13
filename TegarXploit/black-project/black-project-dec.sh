clear
blu='\033[34;1m'
gre='\033[32;1m'
pur='\033[35;1m'
cya='\033[36;1m'
red='\033[31;1m'
kun='\033[33;1m'
wht='\033[37;1m'
sleep 1
echo "
$gre
███████╗██╗  ██╗ ██████╗
██╔════╝╚██╗██╔╝██╔════╝
███████╗ ╚███╔╝ ██║       BLACK PROJECT VERSI 0.1
╚════██║ ██╔██╗ ██║
███████║██╔╝ ██╗╚██████╗   $wht SecurityXploit crew
╚══════╝╚═╝  ╚═╝ ╚═════╝
"
echo $wht"AUTHOR :" $wht"Tegar"$red"Xploit" "" $wht"Team :" $wht"Security"$red"Xploit" $gre"crew"
echo
echo $wht"["$gre"1"$wht"]" $kun"Ip Addres info"
echo $wht"["$gre"2"$wht"]" $kun"Website Scan (nmap)"
echo $wht"["$gre"3"$wht"]" $kun"Cek System"
echo $wht"["$gre"4"$wht"]" $kun"Tools Hacking (instaler)"
echo $wht"["$gre"5"$wht"]" $kun"Server php (open file php)"
echo $wht"["$gre"6"$wht"]" $kun"Encrypt / Decrypt "
echo $wht"["$gre"7"$wht"]" $kun"Informasi gambar"
echo $wht"["$gre"8"$wht"]" $cya"Install bahan"
echo $wht"["$gre"9"$wht"]" $red"Hubungi Author"
echo $gre
read -p "pilih nomor: " pil;
if [ $pil = 1 ]
then
echo -n "masukan ip: "
read ip
curl -s https://ipinfo.io/$ip | sed "s/\"//g; s/^ $//g; s/\:/ :/g; s/readme.*//g" | tr -d '{}'
fi
if [ $pil = 2 ]
then
clear
echo -n "masukan website: "
read nmp
clear
nmap $nmp
fi
if [ $pil = 3 ]
then
clear
apt install htop
htop
fi
if [ $pil = 4 ]
then
clear
echo $wht "
██   ██  █████   ██████ ██   ██
██   ██ ██   ██ ██      ██  ██
███████ ███████ ██      █████
██   ██ ██   ██ ██      ██  ██
██   ██ ██   ██  ██████ ██   ██
"
echo "" "" "" "" "" "" "" $wht"["$gre"•"$wht"]" $kun"Tools Installer Versi 0.1" $wht"["$gre"•"$wht"]"
echo $gre"1. nmap"
sleep 1
echo $gre"2. metasploit"
sleep 1
echo $gre"3. websploit"
sleep 1
echo $gre"4. hydra"
sleep 1
echo $gre"5. Redhawk"
sleep 1
echo $gre"6. RouterSploit"
sleep 1
echo $gre"7. Google Dork search"
sleep 1
echo $gre"8. Sqlmap"
sleep 1
echo $gre"9. Admin Finder"
sleep 1
echo $kun"0. Kembali"
sleep 1
read -p "pilih nomor: " man;
if [ $man = 1 ]
then
apt update && apt upgrade
apt install nmap
clear
nmap
fi
if [ $man = 2 ]
then
apt update && apt upgrade
apt install unstable-repo
apt install metasploit
clear
msfconsole
fi
if [ $man = 3 ]
then
apt update && apt upgrade
apt install python2
pip2 install scapy
git clone https://github.com/The404Hacking/websploit.git
cd websploit
chmod 777
clear
python2 websploit.py
fi
if [ $man = 4 ]
then
apt update && apt upgrade
apt install hydra
clear
hydra
fi
if [ $man = 5 ]
then
apt update && apt upgrade -y
apt install python
apt install git -y
apt install php -y
git clone https://github.com/Tuhinshubhra/RED_HAWK
cd RED_HAWK
php rhawk.php
fi
if [ $man = 6 ]
then
apt update && apt upgrade -y
apt install git
apt install python2
pip2 install requests
git clone https://github.com/reverse-shell/routersploit.git
cd routersploit
pip install -r requirements.txt
termux-fix-shebang rsf.py
./rsf.py
fi
if [ $man = 7 ]
then
apt update && apt upgrade
apt install python
pip install bs4
pip install google
apt install git
git clone https://github.com/TegarXploit/search-dork.git
cd search-dork
chmod +x *
python dork.py
fi
if [ $man = 8 ]
then
apt update -y && apt upgrade -y
pkg install nano git python python2 -y
git clone https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python2 sqlmap.py
fi
if [ $man = 9 ]
then
apt update && apt upgrade
apt install python2
apt install git
apt install toilet
pip2 install requests
git clone  https://github.com/TegarXploit/Admin-finder
cd Admin-finder
ls
chmod +x admin.py
python2 admin.py
fi
if [ $man = 0 ]
then
sleep 2
sh pro.sh
fi
fi
if [ $pil = 5 ]
then
echo "--------------------------------------"
echo " AUTHOR : TegarXploit"
echo " Team : SecurityXploit crew"
echo "--------------------------------------"
echo "salin 127.0.0.1 port paste ke google"
echo
echo -n "Localhost port: "
read port
sleep 2
echo -n "Masukan Php File: "
read file
sleep 2
php -S 127.0.0.1:$port $file
fi
if [ $pil = 6 ]
then
echo "
$wht===============================================
$kun mengunci dan membuka file
1. Encrypt
2. Decrypt
3. Exit
$wht===============================================
"
read -p "pilih nomor: " pil
case $pil in
1) #memilih angka satu
read -p "masukan file: " file
gpg -c $file
echo "File berhasil di encrypt"
;;
2) #memilih angka dua
read -p "masukan file: " file
gpg -d $file
echo "File berhasil di decrypt"
;;
3) #exit program
sleep 2
echo "Terima kasih"
sleep 2
clear
exit
esac
fi
if [ $pil = 7 ]
then
echo $gre"================================="
echo $wht"" "" "" "INFORMATION FOR PICTURES"
echo
echo $kun "masukan contoh : /sdcard/gambar.png"
echo $gre"================================="
echo
echo -n "masukan gambar: "
read gam
sleep 2
echo ""
echo $gre "-----------"
echo $wht " INFO"
echo $gre "-----------"
echo ""
exiftool $gam
fi
if [ $pil = 8 ]
then
apt update
apt upgrade
apt install curl
apt install php
apt install gnupg
apt install bash
apt install htop
apt install nmap
apt install exiftool
clear
sh pro.sh
fi
if [ $pil = 9 ]
then
sleep 1
xdg-open https://wa.me/+6285703474394
fi
