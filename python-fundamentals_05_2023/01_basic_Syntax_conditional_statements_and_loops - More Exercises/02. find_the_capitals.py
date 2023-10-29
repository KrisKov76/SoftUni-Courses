
word = input()

indices = [index for index, char in enumerate(word) if char.isupper()]
print(indices)

# използваме enumerate, което връща индекса и стойността (index и char) на елемента в списъка!
# използваме вградената функция isupper(), koято връща само големите букви
# работим с компрехеншън