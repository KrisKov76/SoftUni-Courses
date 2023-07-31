data = input().split()
concatinated_string = ''

for i in range(len(data)):
    concatinated_string += data[i] * len(data[i])
print(concatinated_string)

# решение на Марио

new_text = [word * len(word) for word in data]
print(''.join(new_text))