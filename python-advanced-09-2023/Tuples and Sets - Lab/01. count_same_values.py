# nums = tuple(float(x) for x in input().split())
# dict = {}
#
# for num in nums:
#     if num not in dict:
#         dict[num] = nums.count(num)
#
# for key, value in dict.items(): # .items разопакова ключ и стойност
#     print(f'{key} - {value} times')

# по-оптимизиран вариант:

nums = tuple(float(x) for x in input().split())
dict = {}

for num in nums:
    if num not in dict: # използвай тази опция! 
        dict[num] = nums.count(num)
        print(f'{num} - {nums.count(num)} times')

# когато ви остане ментална енергия, може да седнете и да помислите да оптимизирате още кода
