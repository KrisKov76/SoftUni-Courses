n = int(input())
word = input()
strings = []

for _ in range(n):
    string = input()
    strings.append(string)
print(strings)

# с използване на comprehension
filtered_strings = [string for string in strings if word in string]
print(filtered_strings)


