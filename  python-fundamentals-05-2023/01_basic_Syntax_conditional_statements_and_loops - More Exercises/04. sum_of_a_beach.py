
lst =["Sand", "Water", "Fish", "Sun"]
lst_upper = [x.upper() for x in lst]

word = input()
word_upper = word.upper()

# for i in range(len(lst)):
#     count = word_upper.count(lst_upper[i])
#     second_count += count
second_count = sum(word_upper.count(x) for x in lst_upper)
print(second_count)
