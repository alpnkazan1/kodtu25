def q2_optimized():
    n = int(input())
    w = list(map(int, input().split()))

    reachable = {0}  # Start with 0 as reachable

    for weight in w:
        new_reachable = set()
        for val in reachable:
            new_reachable.add(val + weight)
            new_reachable.add(val - weight)
        reachable.update(new_reachable)

    i = 1
    while i in reachable:
        i += 1
    return i

print(q2_optimized())