import re

a = {
    "a" : {2, 4},
    "b" : {4, 6}, 
    "c" : {3, 2}
}

print(a["a"], a["b"], a["c"])

for item in a:
    for key, value in item.iteritems():
        try:
            item[key] = int(value)
        except ValueError:
            item[key] = float(value) # use here str(value)