Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German,'

print(len(Belgium))
# used to find out the length of the string Belgium

print(Belgium)
print("-" * 82 )
# used the output of the length of the string to use the number to multiply the operator
# hence the operator overloading

line = Belgium.replace("," ,":")
print(line)
# the string has the element divided by a comma, so use replace method to replace "," with ":"

print("#" * 82)
# used operator overloading for line division

parts= Belgium.split(",")
# using a variable which has assigned value of the string which is separated using a split method
print(parts)
# print function is used to print the separated string

print(int(parts[1]) + int(parts[3]))
# using the operator and the index of the string to
# add the integer values of the 2nd and 4th position items of the string