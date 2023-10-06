total_sum = 0

number_of_lines = int(input()) # не е добра практика да поставяме ord към input

for _ in range(number_of_lines):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")
