
def palindrom_filtered(word):
    return word == word[::-1] #обратно написана дума [::-1]

words = input().split(' ')
palindrom = input()
palindrom_list = [word for word in words if palindrom_filtered(word)]
# count брои колко пъти се среща един повтарящ се елемент в цикъла
palindrom_counter = palindrom_list.count(palindrom)

print(palindrom_list)
print(f'Found palindrome {palindrom_counter} times')

# word = 'Пепеляшка'
# print(word[::-1])