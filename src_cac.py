#Code Cặc lỏ
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
vchh_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
def banner():
 banner = f"""
\033[1;35mMINH   
\033[1;37mDEP    
\033[1;35mZAI
\033[1;37mKHOAI
\033[1;35mTO
\033[1;37mNHAT VIET NAM
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GỘP PYTHON 1.0
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mHỒ ĐỨC MINH
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31mhttps://www.facebook.com/yeuemthemmotchut/
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/0773150128
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mHODUCMINH Share Tool
\033[1;31m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print('')
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Spam Sms \033[1;31m[\033[1;33mV1\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool Spam Sms \033[1;31m[\033[1;33mV2\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool Buff View Tiktok Zefoy ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool Buff Tim Tiktok ")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Facebook  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool Spam Messenger ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool Nuôi Facebook ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool Tự Động Kết Bạn [\033[1;33mBảo Trì\033[1;31m]")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool TTC TikTok\033[1;31m[\033[1;33mBảo Trì \033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool TTC Token \033[1;31m[\033[1;33mBảo Trì\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool TTC Pro5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool TDS Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool TDS Cookie ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool TDS Tiktok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool TDS IG ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Reg Page Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Get Token Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Menber Group Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mTool Share Ảo Pro5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Encode        \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool Encode\033[1;31m[\033[1;33mV1\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Encode\033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Mail+Prx      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;32mTool Mail,Prx Tổng Hợp")
chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/b25d4f37-b7f8-44eb-9268-1d02219fa6e1').text)
if chon == 2 :
	exec(requests.get('https://run.mocky.io/v3/3b1ab121-1229-4234-ae43-db64bb58cc8a').text)
if chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/accb3541-128f-4c8e-a023-489a66629fc4').text)
if chon == 4 :
	exec(requests.get('https://run.mocky.io/v3/de9c9fa5-6f34-456f-acbe-1bb675c4133a').text)
if chon == 5 :
	exec(requests.get('https://run.mocky.io/v3/0547d2bf-e8d8-420c-874b-5853245a44b9').text)
elif chon == 6 :
    exec(requests.get('https://run.mocky.io/v3/0e317561-578d-45f2-890c-b4537f288629').text)
if chon == 7 :
	exec(requests.get('https://run.mocky.io/v3/9a2cab14-4a60-47ae-8c1f-18722edf4cbc').text)
if chon == 8 :
	exec(requests.get('https://run.mocky.io/v3/9a2cab14-4a60-47ae-8c1f-18722edf4cbc').text)
if chon == 9 :
	exec(requests.get('https://run.mocky.io/v3/9a2cab14-4a60-47ae-8c1f-18722edf4cbc').text)
if chon == 10 :
	exec(requests.get('https://run.mocky.io/v3/dd7f9ccd-d9b8-4853-b327-83188a2c4e95').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/e66e0a5f-008d-45bc-add0-4e5400315491').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/0a0a25a2-2985-4d85-afe9-e49d50e51f1a').text)
if chon == 13 :
	exec(requests.get('https://run.mocky.io/v3/d6322f1e-0713-42dc-bbc4-c58565b444d0').text)
elif chon == 14 :
	exec(requests.get('https://run.mocky.io/v3/ecd4e511-5015-4f72-8ccf-58d561a3667c').text)
elif chon == 15 :
	exec(requests.get('https://run.mocky.io/v3/1056cf19-14fc-4096-b636-94f45c7c6c95').text)
elif chon == 16 :
	exec(requests.get('https://run.mocky.io/v3/cfa0cbf2-f86f-47eb-ad42-9c999dc6c2a6').text)
elif chon == 17 :
    exec(requests.get('https://run.mocky.io/v3/251b95a8-b581-494f-9c0c-8edc4b72b83a').text)
elif chon == 18 :
    exec(requests.get('https://run.mocky.io/v3/165f7e3a-4593-4b29-a8e9-3e308b5978b2').text)
elif chon == 19 :
    exec(requests.get('https://run.mocky.io/v3/eaedce18-b5bf-4f3e-8d5f-b6bc07ac93c2').text) 
elif chon == 20 :
    exec(requests.get('https://run.mocky.io/v3/98d7a8d7-16b4-40cd-bf3c-e90d01aab131').text)
elif chon == 21 :
    exec(requests.get('https://run.mocky.io/v3/11c2dd68-5d29-4af2-8bb1-3088f819453d').text)  
elif chon == 22 :
    exec(requests.get('https://run.mocky.io/v3/7e7bfc8f-15b8-426b-88aa-1ff21d7eb82b').text)
else :
	sys.exit("Tool đang được bảo trì hoặc sai sự lựa chọn hãy thử lại")