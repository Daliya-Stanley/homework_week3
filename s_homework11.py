#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# print a line of hyphens the same length as the Belgium string
print("-" * len(Belgium))

# replace the colons in Belgium with commas
print("String with replacement:", Belgium.replace(",", ":"))

# extract the fields in the Belgium string into a list so they have a sequence
# specify the separator to be a comma
fields = Belgium.split(',')
print(fields)

# create a variable whose value is the population of Belgium (item with index 1 in list) plus population of the capital (item index 3)
# convert values to integers so they can be summed
populations = int(fields[1]) + int(fields[3])

# print value of new variable
print(populations)