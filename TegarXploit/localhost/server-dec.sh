blu='\033[34;1m'
gre='\033[32;1m'
pur='\033[35;1m'
cya='\033[36;1m'
red='\033[31;1m'
kun='\033[33;1m'
wht='\033[37;1m'
clear
xdg-open https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ/videos
echo $wht "▐▓█▀▀▀▀▀▀▀▀▀█▓▌"
sleep 1
echo $red "▐▓█         █▓▌" "" $gre"Author: "$wht"Tegar"$red"Xploit"
sleep 1
echo $wht "▐▓█         █▓▌" "" $gre"Youtube: "$wht"CYTOM"
sleep 1
echo $red "▐▓█▄▄▄▄▄▄▄▄▄█▓▌" $kun"port bebas salin link 127.0.0.1:port"
sleep 1
echo $wht "" "" "" ""  "▄▄█"$red"██▄▄"
sleep 1
echo $gre
echo -n "Localhost port: "
read port
sleep 2
echo -n "Masukan Php File: "
read file
sleep 2
php -S 127.0.0.1:$port $file
