import re

text = input()

pattern = r'\b_([A-Za-z0-9]+)\b'
# pattern2 = '\\b_([A-Za-z0-9]+)\\b' # без r се налагат двойни наклонени черти

matches = re.findall(pattern, text)

print(','.join(matches))