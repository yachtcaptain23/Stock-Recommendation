import urllib2
import re


def grab_site(post_text):
  url = "http://finance.yahoo.com/q?s=" + post_text
  
  f = urllib2.urlopen(url)
  lines = f.read()
  counter = 0
  line = [""]
  for char in lines:
    if char == '\n':
      counter+=1
      line.append("")
    else:

      line[counter] = line[counter] + "" + char


  lines = line
  
  for line in lines:
    mo = re.search("Mean Recommendation.*?\>(\d+(\.\d{1,2})?)",line,)
    if mo:
      return "%s%s"%(post_text, mo.group(1))

#
#url = "http://finance.yahoo.com/q?s=FB"

#f = urllib2.urlopen(url)
#print f.read()

print grab_site("fb")
print grab_site("yhoo")
print grab_site("msft")
print grab_site("intc")
print grab_site("ddd")
print grab_site("amzn")

