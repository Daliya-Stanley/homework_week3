# a dictionary where the keys are landmarks around the world, the values are their locations, and they are strings
landmarks = {
    "Eiffel Tower": "France",
    "Great Wall of China": "China",
    "Statue of Liberty": "USA",
    "Taj Mahal": "India",
    "Machu Picchu": "Peru",
    "Christ the Redeemer": "Brazil",
    "Sydney Opera House": "Australia",
    "Colosseum": "Italy",
    "Big Ben": "United Kingdom",
    "Pyramids of Giza": "Egypt"
}

# this is a for loop iterating through the landmarks dictionary keys
# .keys is a method and landmarks.keys() gives us the dictionary variable's keys
# enumerate is a function that yields pairs containing a count, and the second NAMED argument (1) specifies that they are numbered from 1, not zero
# enumerate returns an index value/counter before the item in the loop
for i, key in enumerate(landmarks.keys(), 1):
    # formatting of the string, saves us from doing a lot of concatenation and makes our string look good
    # curly brackets create a placeholder for one of the values; the first one {i:2d} applies to the first argument (i), the second for the second, etc -- called positional argument
    # colon is a format specifier, i.e. the formatting rules to use
    # 2d will apply to i arg and specifies: d is a decimal (a WHOLE NUMBER), 2 is the width (number of spaces) then has a space after it (bc that's what print does)
    # <25 will apply to key arg and specifies: < left aligns the text, 25 means it fills 25 spaces (makes up the rest with space)
    # <15 will apply to the landmarks value, < left aligns the text, 15 means it fills 15 spaces (makes up the rest with space)
    print(f"{i:2d}. {key:<25} is in {landmarks[key]:<15}")

# create a line break
print("\n")

# a dictionary where the keys are countries around the world, the values are their populations in millions, and they are strings
populations = {
    "China": 1441.0,
    "India": 1408.0,
    "USA": 331.9,
    "Mexico": 126.7,
    "Brazil": 213.3,
    "Argentina": 45.8,
    "Germany": 83.2,
    "France": 67.5,
    "Nigeria": 206.1,
    "South Africa": 60.3,
    "Australia": 26.4,
    "Papua New Guinea": 9.2
}

# this is a for loop iterating through the populations dictionary keys
# .keys is a method and populations.keys() gives us the dictionary variable's keys
# enumerate is a function that yields pairs containing a count, and the second NAMED argument (1) specifies that they are numbered from 1, not zero
# enumerate returns an index value/counter before the item in the loop
for i, key in enumerate(populations.keys(), 1):
    # formatting of the string, saves us from doing a lot of concatenation and makes our string look good
    # curly brackets create a placeholder for one of the values; the first one {i:2d} applies to the first argument (i), the second for the second, etc -- called positional argument
    # colon is a format specifier, i.e. the formatting rules to use
    # 2d will apply to i arg and specifies: d is a decimal (a WHOLE NUMBER), 2 is the width (number of spaces) then has a space after it (bc that's what print does)
    # <25 will apply to key arg and specifies: < left aligns the text, 25 means it fills 25 spaces (makes up the rest with space)
    # <15 will apply to the populations values, < left aligns the text, 15 means it fills 15 spaces (makes up the rest with space)
    # 05.1f will apply to value of the dict and specifies: f is a float (DECIMAL), 5 is the entire width of this, including the decimal point, padded with zeroes if it's not 6 characters, the 1 means 1 char after the decimal point
    print(f"{i:2d}. {key:<25} {populations[key]:<05.1f} million")