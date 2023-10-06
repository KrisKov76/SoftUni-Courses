import re

pattern = r"(^|(?<=\s))-?([1-9]\d*)(.\d+)?($|(?=\s))"

text = '1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), end=' ')

# с грипата (^|(?<=\s)) - 1 -1 123 -123 123.456 -123.456

# без групата - 1 -1 123 -123 123.456 -123.456 -1.1 2 -2 -3.5 5

