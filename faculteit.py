def faculteit(n):
    if n == 0:
        return 1
    return n * faculteit(n - 1)

T = int(input())

for _ in range(T):
    n = int(input())
    if n > 13:
        print("invoer te groot")
    else:
        print(faculteit(n))

