
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
		
		# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
		if date is None
			sys.stdout.write(line)

		# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --
		
			
			d1= datetime.datetime(h2+h,min2+minute,sec2+s)
			'{%H:%M:%S}'.format(d1)
			d2= datetime.datetime(h2+h,min2+minute,sec2+s)
			'{%H:%M:%S}'.format(d2)
			sys.stdout.write(d1 --> d2)
