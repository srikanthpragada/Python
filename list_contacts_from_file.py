# Reads contacts information from contacts.xml in local file system and prints details 
from bs4 import BeautifulSoup

file = open(r"e:\classroom\python\dec10\contacts.xml","rt")
bs = BeautifulSoup(file.read(),'xml')
file.close()

for c in bs.find_all("contact"):
      for n,v in c.attrs.items():
          print(n,v)


contacts.xml
=============
<contacts>
  <contact name="Larry" mobile="3939393933"/>
  <contact name="Peter" mobile="3432234222"/>
  <contact name="Mike" phone="343434343"  email="mike@gmail.com" />
</contacts>

Output 
======
name Larry
mobile 3939393933
name Peter
mobile 3432234222
name Mike
phone 343434343
email mike@gmail.com


