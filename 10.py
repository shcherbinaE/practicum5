num = input()

if len(num) != 4 or len(set(num)) != 4 or int(num) in range(1900, 2051):
    print("ERROR")
else:
    print("OK")