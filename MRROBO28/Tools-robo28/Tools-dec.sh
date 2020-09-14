r="\033[31;1m" #merah
g="\033[0;32m" #hijau
b="\33[0;36m" #biru
w="\033[37;1m" #putih
yl="\033[1;33m" #kuning
p="\033[1;35m" #ungu
clear
sleep 1
figlet "MRROBO28" | lolcat
echo $r"m============================================="
sleep 1
echo $yl"==========[×] MENU[×]=========="
sleep 1
echo $g"Date :$(date)"
sleep 1
echo $b"["$g"1"$b"]"$yl"Login Tools"
echo $b"["$g"2"$b"]"$yl"Install bahan"
echo $b"["$g"3"$b"]"$yl"Update Tools"
echo $b"["$r"00"$b"]"$r"exit"$g""
read -p "[?]Silahkan pilih : " h;
if [ $h = 1 ]
then
clear
sleep 3
figlet "LOGIN PAGE" | lolcat
sleep 1
echo "untuk mendapatkan user dan pwnya silahkan Download"
sleep 1
xdg-open https://www.mediafire.com/download/i7jj6voddpqst9s
echo $g"Link:"$b"https://www.mediafire.com/download/i7jj6voddpqst9s"
sleep 3
echo $g""
echo "[LOGIN] "
read -p "Username:" user;
fi
if [ $h = 2 ]
then
cd bahan
clear
sleep 3
figlet "INSTALL BAHAN" | lolcat
bash setup.sh
exit
fi
if [ $h = 3 ]
then
cd bahan
clear
sleep 3
figlet "Update Tools" | lolcat
bash Update.sh
exit
fi
if [ $h = 0 ] || [ $h = 00 ]
then
echo "Thank for used my script"
sleep 3
echo $r"EXIT"
exit
fi
if [ $user = MRROBO28 ]
then
echo ""
else
echo "Salah!!!"
sleep 1
echo "Silahkan ulang"
sleep 1
sh Tools.sh
fi
read -p "Password:" pw;
if [ $pw = toolsrobo28 ]
then
sleep 2
echo "Sucses Login"
sleep 3
else
echo "Salah!!!"
sleep 1
echo "silahkan ulang"
sleep 1
sh Tools.sh
fi
cd bahan
sh SC.sh
