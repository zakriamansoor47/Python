import re

teststring = "nns sdfasdasdasdas"
patt = re.compile(r'[nsd]')
matches = patt.finditer(teststring)
for match in matches:
    print(match)
