def q6():
    a, c = map(int, input().split())

    s = 0  # s is now an integer, not a string

    for b in range(a, 10001):
        num_digits = len(str(b))  # Number of digits in b

        s = (s * (10**num_digits) + b)

        mod = s % c

        if mod == 0:
            print(b)
            return
    print(-1)
    return

q6()