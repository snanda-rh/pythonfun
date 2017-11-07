import re
import urllib2


try:

    word = raw_input("Enter word: ")
    url = "https://www.dictionary.reference.com/browse/" + word


    data = urllib2.urlopen(url).read()
    data1 = data.decode("utf-8")


    m = re.search('meta name="description" content=', data1)
    start=m.end()
    end=start+300
    newString= data1[start:end]    
    print "##################3"
    m = re.search("See more.", newString)
    end =m.start()
    final= newString[0:end]
    print final



except:
    print (" I am sorry your word is not in the dictionary")
