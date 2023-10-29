nums = tuple(float(x) for x in input().split())
dict = {}

for num in nums:
    if num not in dict:
        dict[num] = nums.count(num)
        print(f'{num} - {nums.count(num)} times')