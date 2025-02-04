age = { "John": 45, "Sarah" :40.5, "George": 67, "Charlotte": 80, "Lana": 20, "Paris": 34}
# The syntax for a Python dictionary begins with the left curly brace ({),
# ends with the right curly brace (}), and contains zero or more key : value items
# separated by commas (,). The key is separated from the value by a colon (:).
# the key is the string
# the value is integer


# for  statement is used to iterate over the key element of dictionary
# The enumerate object yields pairs containing a count (from start, which
# defaults to zero) and a value yielded by the iterable argument.
# .key is the method applied to the variable age
# 1 is the keyword/named argument stating iteration of enumeration starts from 1
for i, key in enumerate(age.keys(), 1):

    # Formatted string/f - strings help to simplify string formatting and interpolate
    print(f"{i:2d}. {key:15s} {age[key]: 02.1f} years")
    # these are type specifiers
    # d  specifies the argument as the integers and it explains the argument should have 2 digit space
    # s specifies the argument as the character string
    # the less that '<' shows left justified
    # hence the <15s is left justified with 10 string characters
    # f treats the argument as floats
    #0 padding, 2 DECIMAL includes a decimal point
