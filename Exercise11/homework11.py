Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German,'

print(len(Belgium))
print(Belgium)
print("-" * 82 )

line = Belgium.replace("," ,":")
print(line)

print("#" * 82)

parts= Belgium.split(",")
print(parts)

print(int(parts[1]) + int(parts[3]))
