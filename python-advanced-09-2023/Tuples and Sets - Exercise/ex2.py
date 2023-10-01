from _ast import comprehension

a = {1, 2, 3}
b = {3, 2}

c = a | b
print(c) # union, обединение, като съвпаденията се показват по веднъж

c = a & b # Intersection, пресечна точка, сечението на двата сета
print(c)

c = b - a # Difference, различното в b
print(c)

c = a < b # Subset - дали всичко от а е включено в b
print(c)

c = a > b # Superset -дали всичко от b (каето обаче е по-малко) е включено в a
print(c)

c = a ^ b # Symmetric Difference - различното в двата сета, събрано на едно място
print(c)

# set comprehension

num = [1, 2, 3, 4 ,5 ,6 , 1]
print(num)
unique = {x for x in num} # компрехеншън връща сет с уникалните стойности
print(unique)
