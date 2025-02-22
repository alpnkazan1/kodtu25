def q3():
    n = int(input())
    numbers = []
    for _ in range(n):
        num = int(input())
        numbers.append(num)

    seen = set(numbers)
    missing_number = -1
    for i in range(1, n + 1):
        if i not in seen:
            missing_number = i
            break 

    print(missing_number)

q3()