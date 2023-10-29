import os

files = {}

directory = '../'

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f): # ако това е файл...
        ext = element.split('.')[-1] # взимаме си разширението на файла
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f'.{ext}\n')
        for f_names in sorted(f_names):
            output_file.write(f'- - - {f_names}\n')

