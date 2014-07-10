# This file is an improved version of countViruses.r, it counts organisms in all rows [12:] rather than just one row.

import csv
import sys
from collections import Counter
filename = sys.argv[1]
result = []
DESC_START = 12 #description start
exclusion_str = "virus"

with open(filename, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		if not any(exclusion_str in string for string in row): #add not between if and any for negation: i.e. all hits without 'virus'
#remove not for hits only hits with "virus"
			result.append(set(row[DESC_START:]))	

counted = Counter([item for sublist in result for item in sublist])
outfile = open(filename+".noviruses.counts", 'w')
csvwriter = csv.writer(outfile, delimiter=",")
for key, count in counted.iteritems():
    blast = key
    csvwriter.writerow([blast, count])
