import urllib
import re
from BeautifulSoup import BeautifulSoup
proxies = {'http': 'http://61.135.179.52:80'}
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num="46059"
newurl=url+num

while 1:
    try:
        page=urllib.urlopen(newurl,proxies=proxies)
        soup=BeautifulSoup(page)
        print soup
        num=str(soup).split()[-1]
        newurl=url+num
    except TypeError:
        print "error"

print newurl    