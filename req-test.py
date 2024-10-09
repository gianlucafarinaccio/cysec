import requests


# Create a python script that uses the requests library
# Make it do a GET request to web-01.challs.olicyber.it
r = requests.get('http://web-01.challs.olicyber.it')
print('1 ---------------------------- \n')
print(r.text)


# Create a python script that uses the requests library
# Obtain the flag by doing a GET request on
# http://web-02.challs.olicyber.it/server-records
# with parameter "id" and value "flag"
param = [('id','flag')]
r = requests.get('http://web-02.challs.olicyber.it/server-records', params=param)
print('\n2 ----------------------------')
print(r.text)


# Create a python script that uses the requests library
# Obtain the flag by doing a GET request on
# http://web-03.challs.olicyber.it/flag
# with header "X-Password" containing "admin" as value
header = {'X-Password':'admin'}
r = requests.get('http://web-03.challs.olicyber.it/flag', headers=header)
print('\n3 ----------------------------')
print(r.text)


# Create a python script that uses the requests library
# Obtain the flag by doing a GET request on
# http://web-04.challs.olicyber.it/users
# allowing the server only to give you the "application/xml" format
header = {'Accept':'application/xml'}
r = requests.get('http://web-04.challs.olicyber.it/users', headers = header)
print('\n4 ----------------------------')
print(r.text)


# Create a python script that uses the requests library
# Obtain the flag by doing a POST request on
# http://web-08.challs.olicyber.it/login
# with an HTTP form (application/x-www-form-urlencoded type) containing
# username: admin
# password: admin
header = {'Content-Type':'application/x-www-form-urlencoded'}

''' The content-type application/x-www-form-urlencoded, encode variables as a key=value pair
    and each pair is divided by & char. 
    Two ways to do it in requests
        1. create a data string manually encoded following the pattern 'key=value&...'
        2. create a list of tuple where each tuple is like ('key','value') 
'''
data = 'username=admin&password=admin'
r = requests.post('http://web-08.challs.olicyber.it/login', data=data, headers=header)
print('\n5 ----------------------------')
print(r.text)

data = [('username','admin'),('password','admin')]
r = requests.post('http://web-08.challs.olicyber.it/login', data=data, headers=header)
print(r.text)



# Create a python script that uses the requests library
# Obtain the flag by doing a POST request on
# http://web-09.challs.olicyber.it/login
# sending in JSON the values
# username: admin
# password: admin
data = '{"username":"admin", "password":"admin"}'
header = {'Content-Type':'application/json'}
r = requests.post('http://web-09.challs.olicyber.it/login', data=data, headers=header)
print('\n6 ----------------------------')
print(r.text)

''' Alternatively
    Create a JSON serializable object, like a python dict, like below
    data = {'username':'admin','password':'admin'}
    
    and use the parameter 'json' instead of 'data' in the request method invocation, like below
    r = requests.post('http://web-09.challs.olicyber.it/login', json=data, headers=header)
'''

