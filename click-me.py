import requests


url = 'http://click-me.challs.olicyber.it/'

'''
	'Content-Type':'application/x-www-form-urlencoded'
	'Content-Type':'application/json'
	'Content-Type':'application/xml'

	'Accept':'application/xml'

'''
h = {'Content-Type':'application/json'}

d = {'password[]':'ciao', 'test':'ciao2'}

par = {'a':'1','b':'2'}

cookie = {'cookie':'10000000'}

s = requests.Session()

r = s.get(url, params = None, data = None, json = None ,headers = None, cookies = None)
print(r.text)
print(requests.utils.dict_from_cookiejar(s.cookies))

for i in range(1):

	r = s.get(url, params = None, data = None, json = None ,headers = None, cookies=cookie)
	print(r.text)
	print(requests.utils.dict_from_cookiejar(s.cookies))