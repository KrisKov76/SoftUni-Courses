# 100.0

population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

all_persons_are_wealthy = True

for person in range(len(population)):

    if population[person] < minimum_wealth:

        diff_wealth = minimum_wealth - population[person]
        population[person] += diff_wealth
        index_max_number = population.index(max(population))
        population[index_max_number] -= diff_wealth

        if population[index_max_number] < minimum_wealth:
            print("No equal distribution possible")
            all_persons_are_wealthy = False
            break

if all_persons_are_wealthy:
    print(population)