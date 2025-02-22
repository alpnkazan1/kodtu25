def q4():
    n = int(input())
    s = str(n)
    best_num = -1

    for i in range(len(s)):
            for digit in range(9, -1, -1):
                new_s = list(s)
                new_s[i] = str(digit)
                new_num_str = "".join(new_s)
                new_num = int(new_num_str)

                if new_num % 7 == 0:
                    if new_num > best_num:
                        best_num = new_num

    print(best_num)

q4()