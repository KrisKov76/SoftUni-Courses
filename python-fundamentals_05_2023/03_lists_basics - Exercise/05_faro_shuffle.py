
faro_cards = input().split()
number_of_shuffles = int(input())
i = 0

# взимане на числото на половината дължина на списъка

# разделяне на списъка на две части -  слайсване
for shuffle in range(number_of_shuffles):
    middle = len(faro_cards) // 2

    left_part = faro_cards[0:middle]
    right_part = faro_cards[middle:]
    final_deck = []

    for i in range(middle):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])
        faro_cards = final_deck

print(final_deck)




