lst_one = input().split(', ')
lst_two = input().split(', ')

word = []
# правим вложен цикъл, за да можем да сравняваме думите една спрямо друга в двата списъка
for x in lst_one:
    for y in lst_two:
        # ако елементите от първия и втория съвпадат
        if x in y:
            print(x, y)
            # и не се повтарят...
            if x not in word:
                word.append(x)
print(word)
