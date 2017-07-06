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
	#if index>100000: break
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


"""
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
#zones = [zone.replace(" ","") for zone in vals[34]]  # zones
zones = [zone.replace(" ","") for zone in vals[35]]  #rawcensustractandblock

def find_and_shrink(word,pattern):
	r = re.search(pattern,word)
	if r:
		matched = r.group(0)
		word = word.replace(matched,'')
	return word, bool(r)



maxzonelen = max(len(zone)for zone in zones)
symbols  = [{} for i in xrange(maxzonelen)]
symbols2 = [{} for i in xrange(maxzonelen)]
patterns = {}
index = 0
for zone in zones:
	sys.stdout.write('\rProcessing zones: %5.2f %%'%(index*100.0/len(zones)))
	sys.stdout.flush()
	for minlim in xrange(0,maxzonelen):
		for i in xrange(minlim,len(zone)):
			pattern = zone[i-minlim:i+1]
			patterns.setdefault(pattern,0)
			patterns[pattern]+=1
	for i in xrange(len(zone)):
		symbol = zone[i]
		symbols[i].setdefault(symbol,0)
		symbols[i][symbol]+=1

		symbol2 = zone[i-1:i+1]
		if i%2:
			symbols2[i].setdefault(symbol2,0)
			symbols2[i][symbol2]+=1
	index+=1

p = list(patterns.iteritems())
p.sort(key=lambda x: x[1],reverse=True)


p5 = [zone for zone in zones if len(zone[0])==5]
"""


"""
# test
#t=zones[5000]
#for z in ZONES:
#	t, test = find_and_shrink(t,z)
for zone in zones:
	test = zone 
	for z in ZONES:
		test, result = find_and_shrink(test,z)
		if not test: break
	if test:
		print zone, test
"""
"""
patterns1 = {}
patterns2 = {}
patterns3 = {}
patterns4 = {}
patterns5 = {}
patterns6 = {}
numbers   = {}
patterns1number = {}
patterns2number = {}
for zone in zones:
	for c in zone:
		if not c.isalpha(): continue
		#if c.isdigit: continue
		patterns1.setdefault(c,0)
		patterns1[c]+=1
	for i in xrange(1,len(zone)):
		pattern = zone[i-1:i+1]
		if len([c for c in pattern if c.isalpha()])<len(pattern): continue
		#if [c.isdigit for c in pattern]: continue
		patterns2.setdefault(pattern,0)
		patterns2[pattern]+=1
	for i in xrange(2,len(zone)):
		pattern = zone[i-2:i+1]
		#if [c.isdigit for c in pattern]: continue
		if len([c for c in pattern if c.isalpha()])<len(pattern): continue
		patterns3.setdefault(pattern,0)
		patterns3[pattern]+=1

	for i in xrange(3,len(zone)):
		pattern = zone[i-3:i+1]
		#if [c.isdigit for c in pattern]: continue
		if len([c for c in pattern if c.isalpha()])<len(pattern): continue
		patterns4.setdefault(pattern,0)
		patterns4[pattern]+=1

	for i in xrange(4,len(zone)):
		pattern = zone[i-4:i+1]
		#if [c.isdigit for c in pattern]: continue
		if len([c for c in pattern if c.isalpha()])<len(pattern): continue
		patterns5.setdefault(pattern,0)
		patterns5[pattern]+=1

	for i in xrange(5,len(zone)):
		pattern = zone[i-5:i+1]
		#if [c.isdigit for c in pattern]: continue
		if len([c for c in pattern if c.isalpha()])<len(pattern): continue
		patterns6.setdefault(pattern,0)
		patterns6[pattern]+=1

	for number in re.findall(r"[\d\.]+",zone):
		numbers.setdefault(number,0)
		numbers[number]+=1

	for number in re.findall(r"\D[\d\.]+",zone):
		patterns1number.setdefault(number,0)
		patterns1number[number]+=1

	for number in re.findall(r"\D\D[\d\.]+",zone):
		patterns2number.setdefault(number,0)
		patterns2number[number]+=1

	

p1 = list(patterns1.iteritems())
p1.sort(key=lambda x: x[1],reverse=True)

p2 = list(patterns2.iteritems())
p2.sort(key=lambda x: x[1],reverse=True)

p3 = list(patterns3.iteritems())
p3.sort(key=lambda x: x[1],reverse=True)
		
p4 = list(patterns4.iteritems())
p4.sort(key=lambda x: x[1],reverse=True)
		
p5 = list(patterns5.iteritems())
p5.sort(key=lambda x: x[1],reverse=True)
	
p6 = list(patterns6.iteritems())
p6.sort(key=lambda x: x[1],reverse=True)

n = list(numbers.iteritems())
n.sort(key=lambda x: x[1],reverse=True)

p1n = list(patterns1number.iteritems())
p1n.sort(key=lambda x: x[1],reverse=True)
		
p2n = list(patterns2number.iteritems())
p2n.sort(key=lambda x: x[1],reverse=True)
"""
