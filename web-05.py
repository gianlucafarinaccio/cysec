import requests

c = {'password':'admin'}

r = requests.get('http://web-05.challs.olicyber.it/flag', cookies = c)
print(r.text)


h = {'Content-Type':'application/x-www-form-urlencoded'}
d = 'username=admin&password=admin'
r = requests.post('http://web-08.challs.olicyber.it/login', data = d, headers=h)
print(r.text)