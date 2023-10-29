def num_sums(*args):
    neg_sum = 0
    pos_sum = 0
    for num in args:
        if num > 0:
            pos_sum += num
        else:
            neg_sum += num
    return neg_sum, pos_sum


nums = [int(x) for x in input().split()]
n, p = num_sums(*nums)

print(n)
print(p)

if abs(n) > p:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")