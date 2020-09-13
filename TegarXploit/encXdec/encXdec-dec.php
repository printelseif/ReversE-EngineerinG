<?php system('xdg-open https://www.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ/videos');
sleep(2);
system('clear');
echo "
[32;1m
                    
                 
                   
                   
                  
                    
               [37;1m[[32;1m[37;1m] [33;1m SecurityXploit crew [37;1m[[32;1m[37;1m]
                   [37;1m[[32;1m[37;1m] [37;1mTegar[31;1mXploit [37;1m[[32;1m[37;1m]

";
echo "[37;1m[[32;1m1[37;1m] [33;1mEncode
";
echo "[37;1m[[32;1m2[37;1m] [36;1mDecode
";
echo "";
echo "[37;1mpilih nomor: [32;1m";
$pil = trim(fgets(STDIN));
if ($pil == 1) {
    echo "[33;1mpesan: [32;1m";
    $enc = trim(fgets(STDIN));
    $krip = base64_encode($enc);
    echo "[32;1mhasil nya: [37;1m$krip
";
} else if ($pil == 2) {
    echo "[33;1mpesan: [32;1m";
    $dec = trim(fgets(STDIN));
    $dekrip = base64_decode($dec);
    echo "[32;1mhasil nya: [37;1m$dekrip
";
} else {
    echo "yang bener dong asu
";
}