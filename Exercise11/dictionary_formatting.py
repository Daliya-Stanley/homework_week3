age = { "John": 45, "Sarah" :40.5, "George": 67, "Charlotte": 80, "Lana": 20, "Paris": 34}

for i, key in enumerate(age.keys(), 1):
    print(f"{i:2d} {key:15s} {age[key]: 02.1f} years")
