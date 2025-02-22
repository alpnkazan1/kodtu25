def q6():
    a, c = map(int, input().split())

    for b in range(a, 10001):
        s = ""
        for i in range(a, b + 1):
            s += str(i)

            try:
                num = int(s)
                if num % c == 0:
                    print(b)
                    return
            except ValueError:
                print(-1)
                return
    print(-1)
    return


q6()