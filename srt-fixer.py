
import sys
import re
import argparse
import datetime

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	h=args.offset/3600
	tmp=args.offset%3600
	minute=tmp/60
	s=tmp%60
	
	for line in ifp:
		rexp=re.compile("([0-9]+):([0-9]+):([0-9]+),([0-9]+)/s-->/s([0-9]+):([0-9]+):([0-9]+),([0-9]+)")
		date=rexp.search(line)
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		if date is None
			sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --
			sec2=float(date.group(3))+float(date.group(4))/1000+s
			min2=int(date.group(2))+minute+sec2/60
			h2=int(date.group(1))+h+min2/60
			sec2=sec2%60
			min2=min2%60
			sec3=float(date.group(8))+float(date.group(9))/1000+s
			min3=int(date.group(7))+sec3/60+minute
			h3=int(date.group(6))+h+min3/60
			sec3=sec3%60
			min3=min3%60			
			
			d1= datetime.datetime(h2,min2,sec2)
			'{%H:%M:%S}'.format(d1)
			
			d2= datetime.datetime(h2,min2,sec2)
			'{%H:%M:%S}'.format(d2)
			re.sub('.',',',d1)
			re.sub('.',',',d2)
			sys.stdout.write(d1," --> ", d2)
