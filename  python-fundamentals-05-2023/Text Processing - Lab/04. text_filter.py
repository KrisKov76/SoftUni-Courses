banned_list = input().split(', ')
text = input()

for banned_words in banned_list:
    text = text.replace(banned_words, '*' * len(banned_words))
print(text)

