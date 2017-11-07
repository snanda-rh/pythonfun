import requests
from bs4 import *
data = requests.get('http://www.synonym.com/synonyms/cold')
soup = BeautifulSoup(data.text,"html.parser")
data2 = soup.find('span',{})
data2 = soup.find('span',{'class':'equals'})
print data2
print data2.string
print data2.contents


'''
data2= soup.find('div', {'class':'info'})
print "data2"
print data2
data3 =data2.find('span',{'class':'large-temp'})
print "****************************"
print "data3"
print data3
print "****************************"
print "data3 content"
print data3.contents[0]'''
