import requests
import re
import json

###
import time
import datetime
curr_time = datetime.datetime.now()
btime_str = curr_time.strftime("%Y-%m-%d")
stime_str = curr_time.strftime("%p%H:%M:%S")
timez = time.strftime('%Z', time.localtime())
print("时区:", timez, " 当前时间:", btime_str, stime_str)
###

# 将抓包得来的cookie中的SSUUID粘贴到引号中间
SSUUID = "5AFCB77E11D0ACE85D90652ACA7486F41209B2931F0C20FC328292B8072B296EBF02D0E0AC9263A63E350AA4E477EC8B22AFBF79B5D6B57274FD843D489D2FADD040B9E72A28A91BE819836D4BDA1F7AED9582D15EC4F573224C3AEAD08DD14588692DE4247A183622444E314D0FD3070D6D21F5B00368A720CE06883029D5C5028BBC065CEFAB445C9D2EA0932D678B"

# 以下内容无需更改

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; MI MIX 4 Build/S2.MBRJUN.0523; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/4381 MicroMessenger/8.0.18.2062(0x28001241) Process/toolsmp WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_TW ABI/arm64 ",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
	"Cookie": "SSUUID=" + SSUUID
}

def GetStudyID(): # 得到课程id
	url_get = "http://qndxx.bestcood.com/mp/nanning/my/index.html"
	response = requests.get(url_get, headers = headers)
	if ('<title>抱歉，出错了</title><meta charset="utf-8">' in response.text):
		return -1
	id = re.findall(r'(?<=\/mp\/nanning\/daxuexi\/detail_)\d+(?=\.html)', response.text)
	return id[0]

def Study(): # 发送post
	url_hit = "http://qndxx.bestcood.com/mp/nanning/DaXueXi/LearnHit.html"
	id = GetStudyID()
	if (id == -1): 
		return -1
	data = {"id": id}
	response = requests.post(url_hit, headers = headers, data = data)
	return int(json.loads(response.text)['code'])

code = Study()
if (code != 0):
	print("Error!")
else:
	print("Success!")
