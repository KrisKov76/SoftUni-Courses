num = float(input())

if num == 0:
    print("zero")
elif num >= 1000000:
    print('large positive')
elif num >= 1:
    print('positive')
elif 0 < num < 1:
    print('small positive')
else:
    if abs(num) >= 1000000:
        print('large negative')
    elif abs(num) >= 1:
        print('negative')
    elif abs(num) < 1:
        print('small negative')
