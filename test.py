import requests

data = '{"username":"gianluca", "password":"admin"}'
header = {'Content-Type':'application/json'}
r = requests.post('http://too-small-reminder.challs.olicyber.it/register', data=data, headers=header)
print(r)
print(r.text)
print(r.cookies)


data = '{"username":"gianluca", "password":"admin"}'
header = {'Content-Type':'application/json'}
r = requests.post('http://too-small-reminder.challs.olicyber.it/login', data=data, headers=header)
print(r)
print(r.text)
print(r.cookies)



r = requests.get('http://too-small-reminder.challs.olicyber.it/admin')
print(r.text)
print(r.cookies)