def q3_optimized():
    n = int(input())
    present = [False] * (n + 1)  # Initialize a boolean list to track presence

    for _ in range(n):
        num = int(input())
        if 1 <= num <= n:  # Ignore numbers outside the range [1, n]
            present[num] = True

    missing_number = -1
    for i in range(1, n + 1):
        if not present[i]:
            missing_number = i
            break

    print(missing_number)

q3_optimized()