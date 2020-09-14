r="\033[31;1m" #merah
g="\033[0;32m" #hijau
b="\33[0;36m" #biru
w="\033[37;1m" #putih
yl="\033[1;33m" #kuning
p="\033[1;35m" #ungu
clear
sleep 3
toilet -f slant "MRROBO28" | lolcat
toilet -f slant "TOOLS" | lolcat
sleep 1
echo $w"-----------------------------------------------------------"
echo $b"Author:"$g"MR.ROBO.28"
sleep 1
echo $b"github:"$g"https://github.com/MRROBO28"
sleep 1
echo $b"Instagram:"$g"@irshad_faqih"
xdg-open https://instagram.com/irshad_faqih
sleep 1
echo $r"You"$w"Tube:"$b"MR_ROBO.28"
sleep 1
echo $b"Contact"$w":"$g"08881734568"
echo $g"Note:"$yl"Jangan salah gunakan script ini dengan sembarangan\nkarena Admin Tidak bertanggung jawab"
echo $w"-----------------------------------------------------------"
sleep 3
echo $p"                           [+]Macam-Macam Tools[+]"
sleep 1
echo $b"["$g"01"$b"]"$yl"Deface aox"
echo $b"["$g"02"$b"]"$yl"Membuat Script Devace"
echo $b"["$g"03"$b"]"$yl"Dark FB"
echo $b"["$g"04"$b"]"$yl"spam WA"
echo $b"["$g"05"$b"]"$yl"spam SMS"
echo $b"["$g"06"$b"]"$yl"spam Call"
echo $b"["$g"07"$b"]"$yl"Hack cctv"
echo $b"["$g"08"$b"]"$yl"sadap WA"
echo $b"["$g"09"$b"]"$yl"Send Trojans"
echo $b"["$g"10"$b"]"$yl"VBUG"
echo $b"["$r"00"$b"]"$r"Exit"
echo -n $g"["$r"?"$g"]"$b"Silahkan pilih :"$g
read menu;
if [ $menu = "1" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
cd /sdcard
git clone https://github.com/Mr-xDODOL/AOXdeface
clear
echo $b"Masukkan script devace lo di internal/AOXdeface ya"
cd AOXdeface
python2 aox.py
elif [ $menu = "2" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/4L13199/LITESCRIPT
cd LITESCRIPT
clear
python2 LITESCRIPT.py
mv hasilsc.html /sdcard
elif [ $menu = "3" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2 &
git clone https://github.com/storiku/darkfb
cd darkfb
clear
python2 Dark.py
elif [ $menu = "4" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/storiku/spammerWA
clear
cd spammerWA
python2 cwa.py
elif [ $menu = "5" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/B4N954N2-ID/Brutal-Sms
clear
cd Brutal-Sms
python2 brutal.py
elif [ $menu = "6" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/MRROBO28/spamCall
clear
cd spamCall
python call.py
elif [ $menu = "7" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/MRROBO28/cctv
clear
cd cctv
python2 cctv.py
elif [ $menu = "8" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/Bl4ckDr460n/HxWhatsApp
clear
cd HxWhatsApp
python2 HxWhatsApp.py
elif [ $menu = "9" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/R133F/Trojans
clear
python2 trojans py
elif [ $menu = "10" ]
then
cd $h
cd Tools-robo28
cd bahan
cd Menu
echo $p"download data..."$b
sleep 2
git clone https://github.com/Junior60/vbug
clear
cd vbug
python2 vbug.py
elif [ $menu = 0 ]
then
echo $g"Thanks for used my Tools"
sleep 3
exit
echo $r"Exit["$g"✓"$r"]"
fi
