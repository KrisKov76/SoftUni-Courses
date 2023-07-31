# import re
#
# text = input()
# pattern = input()
#
# matches = re.findall(r'\b' + pattern + r'\b', text, re.IGNORECASE)
#
# print(len(matches))

# Втори вариант

import re

text = input()
word = input()

pattern = fr'\b{word}\b'# с използване на fr'

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))