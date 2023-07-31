word_one, word_two = input(), input()

for i in range(len(word_one)):
    if word_one[i] != word_two[i]:
        print(word_two[0:i + 1] + word_one[i + 1:len(word_one)])

