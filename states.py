# Written by Jonathan Saewitz, released October 23rd, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, collections

count_rep = collections.Counter()
count_dem = collections.Counter()

#data from https://www.govtrack.us/developers/data
with open('legislators-current.csv') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		congress = True if row[4]=="rep" else False
		if congress:
			party = row[7]
			state = row[5]
			if party == "Democrat":
				count_dem[state] += 1
			elif party == "Republican":
				count_rep[state] += 1
			#this does not account for third parties

#thanks to https://gist.github.com/JeffPaine/3083347
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

total_rep_majorities = 0
total_dem_majorities = 0
total_ties = 0

for state in states:
	count_r = count_rep[state]
	count_d = count_dem[state]

	if count_r > count_d:
		total_rep_majorities += 1
	elif count_d > count_r:
		total_dem_majorities +=1
	else:
		total_ties += 1

print "Total Republican majorities:", total_rep_majorities
print "Total Democratic majorities", total_dem_majorities
print "Total ties:", total_ties