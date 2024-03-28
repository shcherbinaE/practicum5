n, k, m = map(int,input().split())
if abs(m - k - 1) <= abs(n - k + m - 1):
    print(m - k - 1)
else:
    print(n - k + m - 1)