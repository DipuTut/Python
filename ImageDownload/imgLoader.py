# Retrieving Image data (keeping original names unchanged) from URLs in 
# a Text file and store them in local hard disk  

import urllib.request
import fileinput
    
for line in fileinput.input():
    line = line.replace('\n', '')
    URL = line
    IMAGE = URL.rsplit('/',1)[1]
    urllib.request.urlretrieve(URL, IMAGE)
   