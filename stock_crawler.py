import re
import urllib2

url  = "https://www.google.com/finance?q="
stock=str(raw_input("enter your stock name"))
url=url+stock
print url
data =urllib2.urlopen(url).read()
data = data.decode("utf-8")

m= re.search('meta itemprop="price"',data)
start_pos= m.start()
end_pos= start_pos +50
newString = data[start_pos:end_pos]
m = re.search("content=*",newString)
start =m.end()
newString= newString[start:]
m = re.search("/",newString)
start=0
end=m.end()-2
final=newString[start:end]
print ("this is the stock price for"), stock + " - ", final
