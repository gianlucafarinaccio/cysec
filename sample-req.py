import requests


url = 'https://webhook.site/3fcbddf1-d2c4-4a69-b86c-623d24f26d0a'

'''
	'Content-Type':'application/x-www-form-urlencoded'
	'Content-Type':'application/json'
	'Content-Type':'application/xml'

	'Accept':'application/xml'

'''
h = {'Content-Type':'application/json'}

d = {'password[]':'ciao', 'test':'ciao2'}

par = {'a':'1','b':'2'}

cookie = {'c1':'1', 'c2':'2'}



r = requests.post(url, params = par, data = d, json = None ,headers = h, cookies = cookie)

print(r.text)