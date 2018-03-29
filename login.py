import requests
import importlib    #python3.x
# import imp        #python2.x
import sys

importlib.reload(sys)
#sys.setdefaultencoding("utf-8")

def login(url, username, passwd):
	header = {
		'Accept' : '*/*',
		'Accept-Encoding' : 'gzip, deflate',
		'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
		'Connection' : 'keep-alive',
		'Content-Length' : "",
		'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie' : 'EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_USERNAME=%E5%90%B4%5C201728013229038; EPORTAL_COOKIE_PASSWORD=wwq123; EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_SERVER_NAME=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%9C%8D%E5%8A%A1; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=null; JSESSIONID=7DEF0324F2E512D084F846253828EDB3',
		'Host' : '210.77.16.21',
		'Origin' : 'http://210.77.16.21',
		'Referer' : 'http://210.77.16.21/eportal/success.jsp?userIndex=32633037313662353833633861633363626437353637613834636664653561385f31302e3230322e33322e3132375fcee25c323031373238303133323239303338&keepaliveInterval=0',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}

	user_data = {
		'userId' : username,
		'password' : passwd,
		'service' : "",
		'queryString' : 'wlanuserip%253D0bc386d9e643d188b011a0d00c9b5c40%2526wlanacname%253D5fcbc245a7ffdfa4%2526ssid%253D%2526nasip%253D2c0716b583c8ac3cbd7567a84cfde5a8%2526mac%253D53ba540bde596b811a6d5617a86fa028%2526t%253Dwireless-v2%2526url%253D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&',
		'operatorPwd' : "",
		'operatorUserId' : "",
		'validcode' : ""
	}
	req = requests.post(url, data = user_data, headers = header)
	req.encoding = req.apparent_encoding
	print (req.text)

def logout():
	pass

if __name__ == '__main__':
	url = 'http://210.77.16.21/eportal/InterFace.do?method=login'
	username = '201728013229038'
	#username = '吴\201728013229038'
	passwd = 'xxxxxx'
	login(url, username, passwd)

