import pandas as pd
from  cPickle import load, dump
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from dateutil import parser


def read_csv():
	p = pd.read_csv("properties_2016.csv",dtype=str)
	t = pd.read_csv("train_2016.csv",dtype=str)

	logerror = {}
	for i in xrange(t["parcelid"].count()):
		logerror[int(t.get_value(i,'parcelid'))] = [
				float(t.get_value(i,'logerror')), 
				t.get_value(i,'transactiondate')
		]


	rawcensustractandblock = {}
	for i in xrange(p["parcelid"].count()):
		rawcensustractandblock[int(p.get_value(i,'parcelid'))] = p.get_value(i,'rawcensustractandblock')


	f = open("pandas.dump","wb")
	dump(logerror,f)
	dump(rawcensustractandblock,f)
	f.close()

def load_pickle(first=True,second=True):
	print "Loading dumped objects"
	f = open("pandas.dump","rb")
	logerror = load(f) if first else None
	rawcensustractandblock = load(f) if second else None
	f.close()
	print "done"
	return logerror, rawcensustractandblock

def scatter_plot(x,y):
	plt.plot(x, y, "o")
	plt.show()



def run_census_analysis():
	logerror, rawcensustractandblock = load_pickle()
	x = []
	y = []
	print "Processing scatter plot ... "
	for key in logerror.keys():
		census = rawcensustractandblock[key]
		if not census: continue
		if type(census) is not str: continue
		if "." not in census: continue
		###val = int(census.split(".")[-1])
		val = int(census.split(".")[0])
		x.append(val)
		y.append(logerror[key][0])
	print "done"
	#scatter_plot(x,y)

	vals1 = {}
	vals2 = {}
	for key, val in rawcensustractandblock.iteritems():
		if type(val) is not str: continue
		if "." not in val: continue
		if key not in logerror: continue
		val1, val2 = [int(item) for item in val.split(".") ]
		vals1.setdefault(val1,0)
		vals1[val1]+=1
		vals2.setdefault(val2,0)
		vals2[val2]+=1

	v1 = [value for key, value in vals1.iteritems()]
	v2 = [value for key, value in vals2.iteritems()]
	v1.sort(reverse=True)
	v2.sort(reverse=True)

	len([i for i in v2 if i>20])
	len([i for i in v1 if i>20])

def run_time_analysis():
	logerror = load_pickle(first = True, second = False)[0]
	x = []
	y = []
	#meandates = [parser.parse("%04d%02d%02d"%(year,month,day))  for year in xrange(2016,2018) for month in xrange(1,13) for day in xrange(1,31,5)]
	meandates = [parser.parse("%04d%02d01"%(year,month))  for year in xrange(2016,2018) for month in xrange(1,13)]
	means = {}
	print "Processing scatter plot ... "
	for key in logerror.keys():
		error, date = logerror[key]
		date = parser.parse(date)
		x.append(date)
		y.append(error)

		# mean values
		for i in xrange(len(meandates)-1):
			#if meandates[i]<= date and date<=meandates[i]:
			if meandates[i]<= date and date<=meandates[i+1]:
				means.setdefault(meandates[i],[])
				means[meandates[i]].append(error)
				break
	print "done"
	dates = x
	x = dts.date2num(x)

	x2, y2, y2_2 = [], [], []
	for key, value in means.iteritems():
		x2.append(key)
		mean  = sum(value)*1.0/len(value)
		mean2 = sum([val**2 for val in value])*1.0/len(value)
		y2.append(mean)
		y2_2.append((mean2 - mean**2)**0.5)
	x2 = dts.date2num(x2)
	"""
	meandates = [parser.parse("%04d%02d%02d"%(year,month,day))  for year in xrange(2016,2018) for month in xrange(1,13) for day in xrange(1,31,5)]
	means = {}
	for date, val in zip(dates,y):
		for i in xrange(len(meandates)-1):
			if meandates[i]<= date and date<=meandates[i]:
				means.setdefault(meandates[i],[])
				means[meandates[i]].append(val)
				break

	x2, y2 = [], []
	for key, value in means.iteritems():
		x2.append(key)
		y2.append()
		
	"""	
	plt.plot_date(x, y)
	plt.plot_date(x2, y2,color="red")
	plt.plot_date(x2, y2_2,color="green")
	plt.show()
	
	
#run_census_analysis()
run_time_analysis()






	
#f = open("pandas.dump","rb")
#p = load(f)
#t = load(f)
#f.close()

#rawcensustractandblock



#for column in p:
#	print column
#p.get_value(10000,'rawcensustractandblock')

#Column  0 :  2985217 values;  #Column name parcelid Types:  ['i'] Vals:  ['10711725', '10711726', '10711727', '10711728', '10711729'] ...
#Column  1 :  8 values;  #Column name airconditioningtypeid Types:  ['i', 'n'] Vals:  ['', '1', '11', '12', '13'] ...
#Column  2 :  9 values;  #Column name architecturalstyletypeid Types:  ['i', 'n'] Vals:  ['', '10', '2', '21', '27'] ...
#Column  3 :  752 values;  #Column name basementsqft Types:  ['i', 'n'] Vals:  ['', '100', '1000', '1002', '1007'] ...
#Column  4 :  38 values;  #Column name bathroomcnt Types:  ['f', 'n'] Vals:  ['', '0.0', '0.5', '1.0', '1.5'] ...
#Column  5 :  22 values;  #Column name bedroomcnt Types:  ['f', 'n'] Vals:  ['', '0.0', '1.0', '10.0', '11.0'] ...
#Column  6 :  6 values;  #Column name buildingclasstypeid Types:  ['i', 'n'] Vals:  ['', '1', '2', '3', '4'] ...
#Column  7 :  13 values;  #Column name buildingqualitytypeid Types:  ['i', 'n'] Vals:  ['', '1', '10', '11', '12'] ...
#Column  8 :  35 values;  #Column name calculatedbathnbr Types:  ['f', 'n'] Vals:  ['', '1.0', '1.5', '10.0', '10.5'] ...
#Column  9 :  2 values;  #Column name decktypeid Types:  ['i', 'n'] Vals:  ['', '66'] ...
#Column  10 :  4605 values;  #Column name finishedfloor1squarefeet Types:  ['i', 'n'] Vals:  ['', '100', '1000', '1001', '10018'] ...
#Column  11 :  12588 values;  #Column name calculatedfinishedsquarefeet Types:  ['f', 'n'] Vals:  ['', '1.0', '10.0', '100.0', '1000.0'] ...
#Column  12 :  10671 values;  #Column name finishedsquarefeet12 Types:  ['i', 'n'] Vals:  ['', '1', '10', '100', '1000'] ...
#Column  13 :  251 values;  #Column name finishedsquarefeet13 Types:  ['i', 'n'] Vals:  ['', '1000', '1008', '1020', '1032'] ...
#Column  14 :  8817 values;  #Column name finishedsquarefeet15 Types:  ['i', 'n'] Vals:  ['', '1000', '10000', '10002', '10007'] ...
#Column  15 :  4803 values;  #Column name finishedsquarefeet50 Types:  ['i', 'n'] Vals:  ['', '100', '1000', '1001', '10018'] ...
#Column  16 :  4252 values;  #Column name finishedsquarefeet6 Types:  ['i', 'n'] Vals:  ['', '1000', '1001', '1002', '1003'] ...
#Column  17 :  4 values;  #Column name fips Types:  ['i', 'n'] Vals:  ['', '06037', '06059', '06111'] ...
#Column  18 :  10 values;  #Column name fireplacecnt Types:  ['i', 'n'] Vals:  ['', '1', '2', '3', '4'] ...
#Column  19 :  21 values;  #Column name fullbathcnt Types:  ['i', 'n'] Vals:  ['', '1', '10', '11', '12'] ...
#Column  20 :  25 values;  #Column name garagecarcnt Types:  ['i', 'n'] Vals:  ['', '0', '1', '10', '11'] ...
#Column  21 :  2241 values;  #Column name garagetotalsqft Types:  ['i', 'n'] Vals:  ['', '0', '100', '1000', '1001'] ...
#Column  22 :  2 values;  #Column name hashottuborspa Types:  ['n', 's'] Vals:  ['', 'true'] ...
#Column  23 :  15 values;  #Column name heatingorsystemtypeid Types:  ['i', 'n'] Vals:  ['', '1', '10', '11', '12'] ...
#Column  24 :  852326 values;  #Column name latitude Types:  ['i', 'n'] Vals:  ['', '33324388', '33339132', '33339136', '33339201'] ...
#Column  25 :  1042551 values;  #Column name longitude Types:  ['f', 'n'] Vals:  ['', '-117554316', '-117554343', '-117554372', '-117554482'] ...
#Column  26 :  69954 values;  #Column name lotsizesquarefeet Types:  ['f', 'n'] Vals:  ['', '1.0201752E7', '1.0497786E7', '1.0749024E7', '1.4043439E7'] ...
#Column  27 :  2 values;  #Column name poolcnt Types:  ['i', 'n'] Vals:  ['', '1'] ...
#Column  28 :  908 values;  #Column name poolsizesum Types:  ['i', 'n'] Vals:  ['', '100', '1000', '1001', '1004'] ...
#Column  29 :  2 values;  #Column name pooltypeid10 Types:  ['i', 'n'] Vals:  ['', '1'] ...
#Column  30 :  2 values;  #Column name pooltypeid2 Types:  ['i', 'n'] Vals:  ['', '1'] ...
#Column  31 :  2 values;  #Column name pooltypeid7 Types:  ['i', 'n'] Vals:  ['', '1'] ...
#Column  32 :  241 values;  #Column name propertycountylandusecode Types:  ['i', 'n', 's'] Vals:  ['', '0', '010', '0100', '0101'] ...
#Column  33 :  16 values;  #Column name propertylandusetypeid Types:  ['i', 'n'] Vals:  ['', '246', '247', '248', '260'] ...
#Column  34 :  5639 values;  #Column name propertyzoningdesc Types:  ['i', 'n', 's'] Vals:  ['', '"#12"', '"GDE7-20', '"GDE7-30', '"GDE7-40'] ...
#Column  35 :  100285 values;  #Column name rawcensustractandblock Types:  ['f', 'n', 's'] Vals:  ['', '0"', '00"', '060371011.101000', '060371011.101001'] ...
#Column  36 :  221 values;  #Column name regionidcity Types:  ['f', 'i', 'n'] Vals:  ['', '060374004.042015', '060374004.042020', '060374004.042048', '060374004.043007'] ...
#Column  37 :  5 values;  #Column name regionidcounty Types:  ['i', 'n'] Vals:  ['', '11626', '1286', '2061', '3101'] ...
#Column  38 :  530 values;  #Column name regionidneighborhood Types:  ['i', 'n'] Vals:  ['', '113455', '113688', '113713', '113749'] ...
#Column  39 :  406 values;  #Column name regionidzip Types:  ['i', 'n'] Vals:  ['', '399675', '95982', '95983', '95984'] ...
#Column  40 :  39 values;  #Column name roomcnt Types:  ['f', 'i', 'n'] Vals:  ['', '0.0', '1.0', '10.0', '11.0'] ...
#Column  41 :  3 values;  #Column name storytypeid Types:  ['f', 'i', 'n'] Vals:  ['', '0.0', '7'] ...
#Column  42 :  8 values;  #Column name threequarterbathnbr Types:  ['i', 'n'] Vals:  ['', '1', '2', '3', '4'] ...
#Column  43 :  6 values;  #Column name typeconstructiontypeid Types:  ['i', 'n'] Vals:  ['', '10', '11', '13', '4'] ...
#Column  44 :  147 values;  #Column name unitcnt Types:  ['i', 'n'] Vals:  ['', '1', '10', '100', '101'] ...
#Column  45 :  1640 values;  #Column name yardbuildingsqft17 Types:  ['i', 'n'] Vals:  ['', '1', '10', '100', '1000'] ...
#Column  46 :  595 values;  #Column name yardbuildingsqft26 Types:  ['i', 'n'] Vals:  ['', '10', '100', '1000', '1005'] ...
#Column  47 :  169 values;  #Column name yearbuilt Types:  ['f', 'n'] Vals:  ['', '1801.0', '1805.0', '1806.0', '1807.0'] ...
#Column  48 :  90 values;  #Column name numberofstories Types:  ['f', 'i', 'n'] Vals:  ['', '1', '14', '17', '1890.0'] ...
#Column  49 :  2 values;  #Column name fireplaceflag Types:  ['n', 's'] Vals:  ['', 'true'] ...
#Column  50 :  426079 values;  #Column name structuretaxvaluedollarcnt Types:  ['f', 'n'] Vals:  ['', '1.0', '1.0020446E7', '1.0052426E7', '1.006434E7'] ...
#Column  51 :  638898 values;  #Column name taxvaluedollarcnt Types:  ['f', 'n'] Vals:  ['', '1.0', '1.0000176E7', '1.0005035E7', '1.0006209E7'] ...
#Column  52 :  321 values;  #Column name assessmentyear Types:  ['f', 'i', 'n'] Vals:  ['', '100358.0', '1016674.0', '102220.0', '102222.0'] ...
#Column  53 :  531401 values;  #Column name landtaxvaluedollarcnt Types:  ['f', 'i', 'n'] Vals:  ['', '1.0', '1.0021303E7', '1.003237E7', '1.0032694E7'] ...
#Column  54 :  1045924 values;  #Column name taxamount Types:  ['f', 'n'] Vals:  ['', '1.34', '1.85', '10.02', '10.12'] ...
#Column  55 :  308 values;  #Column name taxdelinquencyflag Types:  ['f', 'n', 's'] Vals:  ['', '1000.57', '10066.66', '10066.72', '10072.52'] ...
#Column  56 :  34 values;  #Column name taxdelinquencyyear Types:  ['i', 'n', 's'] Vals:  ['', '0', '1', '10', '11'] ...
#Column  57 :  96753 values;  #Column name censustractandblock
#Types:  ['f', 'i', 'n'] Vals:  ['', '-1', '14', '15', '483030105084015'] ...



