echo -e "\033[0;32m[Updating]"
apt update -y &> /dev/null;
apt upgrade -y &> /dev/null;
sleep 3
clear
figlet "INSTALL BAHAN" | lolcat
echo -e "\033[0;32m[Installing package]"
sleep 3
echo -e "\033[1;33m[Install vim]"
pkg install vim -y &> /dev/null;
echo -e "\033[1;33mSucses Install vim\033[0;36m[\033[0;32m✓\033[0;36m]" &> /dev/null;
sleep 2
echo -e "\033[1;33m[Install php]"
pkg install php -y &> /dev/null;
echo -e "\033[1;33mSucses Install php\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install toilet]"
apt install toilet -y &> /dev/null;
echo -e "\033[1;33mSucses Install toilet\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install neofetch]"
apt install neofetch -y &> /dev/null;
echo -e "\033[1;33mSucses Install neofetch\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install cowsay]"
apt install cowsay -y &> /dev/null;
echo -e "\033[1;33mSucses Install cowsay\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install nano]"
pkg install nano -y &> /dev/null;
echo -e "\033[1;33mSucses Install nano\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install wget]"
pkg install wget -y &> /dev/null;
echo -e "\033[1;33mSucses Install wget\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 2
echo -e "\033[1;33m[Install pip]"
pip install mechanize &> /dev/null;
pip2 install mechanize &> /dev/null;
pip install requests &> /dev/null;
pip2 install requests &> /dev/null;
pip install lolcat &> /dev/null;
pip install bs4 &> /dev/null;
pip2 install bs4 &> /dev/null;
echo -e "\033[1;33mSucses install pip\033[0;36m[\033[0;32m✓\033[0;36m]"
sleep 3
echo -e "\033[0;32m[Done]"
