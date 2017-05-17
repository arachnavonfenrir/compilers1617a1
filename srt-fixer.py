
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
	h=int(h)
	minute=tmp/60
	minute=int(minute)
	s=tmp%60
	
	for line in ifp:
		rexp=re.compile(r'([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3})\s-->\s([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3})')
		timing=rexp.search(line)
		
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		if timing is None:
			sys.stdout.write(line)
		else:
		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --
			
			seconds=timing.group(3) 
			miliseconds=timing.group(4)
			sec2=float(seconds)+float(miliseconds)/1000+s
			min2=int(timing.group(2))+minute+sec2/60
			
			h2=int(timing.group(1))+h+min2/60
			
			sec2=sec2%60
			min2=min2%60
			min2-int(min2)
			sec3=float(timing.group(7))+float(timing.group(8))/1000+s
			
			min3=int(timing.group(6))+sec3/60+minute
			h3=int(timing.group(5))+h+min3/60
			sec3=sec3%60
			min3=min3%60	
			h3=int(h3)
			min3=int(min3)		
			allsec2=sec2+min2*60+h2*3600
			allsec3=sec3=min3*60+h3*3600
			
			d1=datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(allsec2), "%M:%S%f")			
			d2=datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(allsec3), "%M:%S%f")

			
			re.sub('.',',',d1)
			re.sub('.',',',d2)
			date=d1+" --> "+d2+'\n'
			sys.stdout.write(date)
