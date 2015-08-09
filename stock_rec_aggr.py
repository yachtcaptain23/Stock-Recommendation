#!/usr/bin/python

import urllib2
import re, argparse


def readTickersFromText(textfile):
  f_open = open(textfile,'r',)
  lines = f_open.readlines()
  f_open.close()

  for line in lines:
    val = grab_site(line[:-1])
    if(val):
      print val

def grab_site(post_text):
  url = "http://finance.yahoo.com/q?s=" + post_text
  
  f = urllib2.urlopen(url)
  lines = f.read()
  counter = 0
  line = [""]
  rec_mo = None
  eps_mo = None
  for char in lines:
    if char == '\n':
      counter+=1
      line.append("")
    else:

      line[counter] = line[counter] + "" + char


  lines = line
  
  for line in lines:
    if not rec_mo:
      rec_mo = re.search("Mean Recommendation.*?\>(\d+(\.\d{1,2})?)",line,)
    if not eps_mo:
      # eps_mo = re.search("Annual EPS Est.*?\>((|-)\d+(\.\d{1,2})?)",line)
      eps_mo = re.search("Annual EPS Est(.*)",line)
      # First table value is for Annuel EPS Est from Yahoo website June 2014
      # </small>:</th><td class="yfnc_tabledata1">0.83</td></tr><tr><th scope="row" width="50%">Quarterly EPS Est<small>

      eps_mo = re.search("yfnc_tabledata1\">(\d+(\.\d{1,2})?)</td></tr><tr><th scope=\"row\" width=\"50%\">Quarterly",line,);
    if rec_mo and eps_mo:
      return "%s rec=%s eps=%s"%(post_text, rec_mo.group(1), eps_mo.group(1))

'''
Argument parsing
'''
def parse_arguments():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('-filename',type=str,nargs=1,help='')
  args = parser.parse_args()
  return args.filename[0]

def __main__():
  filename = parse_arguments()
  readTickersFromText(filename)

__main__()
