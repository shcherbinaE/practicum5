num = int(input())
last = num % 10
if 5 <= last <= 9 or last == 0 or 11 <= num <= 20:
    print( num,'попугаев')
elif 2 <= last <= 4:
    print(num, 'попугая')
else:
    print(num, 'попугай')