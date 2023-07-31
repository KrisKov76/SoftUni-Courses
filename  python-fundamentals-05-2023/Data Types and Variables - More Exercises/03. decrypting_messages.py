
key = int(input())
num = int(input())

for _ in range(num):
    letter = input()
    decrypted = key + ord(letter)
    print(chr(decrypted), end='')

