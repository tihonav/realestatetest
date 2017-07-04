import sys
import re

f = open(sys.argv[1])
l = f.readlines()

nvals = len(l[0].split(","))
print "nvals=", nvals


# read values
print "Read values values\n"
#vals = [[None]*(len(l)-1) for i in xrange(nvals)]
index = 0
vals  = [[] for i in xrange(nvals)]
types = [[] for i in xrange(nvals)]
for line in l[1:]:
	avals = [val.strip() for val in line.split(",")]
	sys.stdout.write('\r%5.2f %%'%(index*100.0/len(l)))
	sys.stdout.flush()
	for i in xrange(nvals): 
		#if avals[i] not in vals[i]: pass
		vals[i].append(avals[i])
		# type
		atype = 's'
		if not avals[i]: atype = 'n'
		elif avals[i].isdigit(): atype = 'i'
		else:
			try:
				float(avals[i])
				atype = 'f'
			except:
				pass
		if atype not in types[i]:
			types[i].append(atype)
	index+=1
	if index>10000: break
	#break


# print unique values
print "Get unique values\n"
for n in xrange(nvals):
	vals[n].sort()
	unique = []
	previous = None
	for val in vals[n]:
		if val == previous: continue
		previous = val
		unique.append(val)
	types[n].sort()
	print "Column ",n, ": ", len(unique), "values;  Column name", l[0].split(",")[n], "Types: ", types[n], "Vals: ", unique[:5], "..."


# zones
# https://planning.lacity.org/zone_code/Appendices/sum_of_zone.pdf  \d+
ZONES = [
	r"A1",r"A2",r"RA",                                                # agricultural
	r"RE\d+",r"RS",                                                   # residential estate  RE20, RE40, RE9
	r"R\d+",r"RU",r"RZ[\d\.]+",r"RW[\d\.]+", r"RD[\d\.]+", "RAS\d+",  # *-Family Residential
	r"CR", r"CM", "C\d+",                                             # commercial
	r"M\d+", r"MR\d+",                                                # manufacturing
	r"P",r"PB",                                                       # parking
	r"OS", r"PF", r"SL",                                              # open space
	r"LA",
]
zones = vals[34]

def find_and_shrink(word,pattern):
	r = re.search(pattern,word)
	if r:
		matched = r.group(0)
		word = word.replace(matched,'')
	return word, bool(r)


# test
#t=zones[5000]
#for z in ZONES:
#	t, test = find_and_shrink(t,z)
	
		
