ó
 V>_c           @   sJ  d  Z  d Z d Z d Z d Z d Z d Z d Z d d	 l Z d d	 l	 Z	 d d	 l
 Z
 d d	 l Z d d	 l Z d d	 l Z d d	 l Z d d	 l	 Z	 d d	 l Z d d	 l Z d
   Z d   Z d   Z e d e d e d Z e d e d e d Z e d e d e d Z Hd   Z d   Z d   Z d   Z d   Z e   d	 S(   s   [0ms   [90ms   [1;37ms   [94ms   [91ms   [1;32ms   [1;33ms   [1;36miÿÿÿÿNc         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      ð?i   (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   st   c(    (    s   bt.pyt   wr   s    c         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      ð?id   (   R    R   R   R   R   R   (   t   ht   d(    (    s   bt.pyt   bn   s    c         C   s   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x, | D]$ } |  j  d | d | |  }  q7 W|  d 7}  |  j  d d  }  |  GHd  S(   Ni   t   mi    R	   i!   t   ki"   t   bi#   t   pi$   R   s   %ss   [%s;1ms   [0ms   0(   t   replace(   t   xt   wt   i(    (    s   bt.pyt   tampil   s    0"
t   [t   ?s   ] s   ât   !t   ]c           C   s   t  d  t j j   d  S(   Ns   m[!]Thanks for used my script(   R   t   osR    t   exit(    (    (    s   bt.pyt   keluar*   s    
c          C   s0  yö t  t t d t d t  }  t |  d  } | j   } | j   | j d d  } t  t t d t d t  } t | d  } | j |  | j   t	 j
 d	  t	 j
 d
 | d  t	 j |  t	 j
 d |  t d GHt  d  } Wn3 t k
 rt d GHn t k
 r+t d GHn Xd  S(   Ns   Masukkan Alamat Input s   > t   rt   evalt   echos   Masukkan Alamat Outputs    > R   s   touch tes.shs   bash s	    > tes.shs   mv -f tes.sh s   Done..s   mau lagi?[y/n]s	    Stopped!s    File Not Found!(   t	   raw_inputt   askt   Wt   Gt   opent   readt   closeR   R   R   t   systemt   removet   suksest   KeyboardInterruptt   erort   IOError(   t   sct   ft   filedatat   newdatat   outt   pil0(    (    s   bt.pyt   dekrip/   s(     
 
	c          C   s    yf t  t t d t d t  }  t  t t d t d t  } t j d |  d |  t d GHWn3 t k
 r t d GHn t	 k
 r t d GHn Xd  S(	   Ns   Masukan Alamat Script s   |> s   Masukan Alamat Output s   bash-obfuscate s    -o s
   Berhasil..s
    Berhenti!s    File Tidak Terdeteksi!(
   R   R    R!   R"   R   R&   R(   R)   R*   R+   (   t   scriptt   output(    (    s   bt.pyt   enkripH   s      c           C   sh   yG t  t d  t  t d  t j d  t j d  t j d  Wn t k
 rc t d GHn Xd  S(   Ns   Install bahan dulu...s
   Loading...s#   pkg install nodejs -y &> /dev/null;s+   npm install -g bash-obfuscate &> /dev/null;s   python2 bash.pys
    Berhenti!(   R   R"   t   BR   R&   R)   R*   (    (    (    s   bt.pyt   bahanS   s    c          C   sß   t  j d  t d  d GHd GHd GHd GHt t d t d  }  |  d	 k s[ |  d
 k re t   nv |  d k s} |  d k r t   nT |  d k s |  d k r© t   n2 |  d k sÁ t	 d k rË t
   n t d GHt
   d  S(   Nt   clearsà   	 [1;33m____            _       _____           _
	| __ )  __ _ ___| |__   |_   _|__   ___ | |___  
	|  _ \ / _` / __| '_ \    | |/ _ \ / _ \| / __| 
	| |_) | (_| \__ \ | | |   | | (_) | (_) | \__ \ 
	|____/ \__,_|___/_| |_|   |_|\___/ \___/|_|___/ 
[1;36mââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
[1;37m		Author  : MRROBO28
[1;37m		github  : https://github.com/MRROBO28
[1;37m		Youtube : TEKTRIKBOT CN
[1;36mââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
s   [91m[1][97mEncripts   [91m[2][97mDecrypts   [91m[3][97minstall bahan dulus   [91m[0][97mKeluart   Pilihs    |> t   1t   01t   2t   02t   3t   03t   0t   00s    Wrong input(   R   R&   R   R   R!   R"   R5   R2   R7   t   tatokR   R*   (   t   takok(    (    s   bt.pyt   menu]   s$    




	(   t   Nt   DR!   t   Ct   RR"   t   YR6   R   R    t	   fileinputR   t   sockett   randomt   platformR   R   R   R    R(   R*   R   R2   R5   R7   RD   (    (    (    s   bt.pyt   <module>   s*   x			
				
	