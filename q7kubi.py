def solve():
    matrix = []
    while True:
        try:
            row = list(map(int, input().split()))
            matrix.append(row)
        except:
            break

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    max_area = 0
    best_rect1 = None
    best_rect2 = None

    for r1_start in range(rows):
        for c1_start in range(cols):
            for r1_end in range(r1_start, rows):
                for c1_end in range(c1_start, cols):

                    valid_rect1 = True
                    for r in range(r1_start, r1_end + 1):
                        for c in range(c1_start, c1_end + 1):
                            if matrix[r][c] == 0:
                                valid_rect1 = False
                                break
                        if not valid_rect1:
                            break

                    if not valid_rect1:
                        continue

                    area1 = (r1_end - r1_start + 1) * (c1_end - c1_start + 1)

                    for r2_start in range(rows):
                        for c2_start in range(cols):
                            for r2_end in range(r2_start, rows):
                                for c2_end in range(c2_start, cols):

                                    valid_rect2 = True
                                    for r in range(r2_start, r2_end + 1):
                                        for c in range(c2_start, c2_end + 1):
                                            if matrix[r][c] == 0:
                                                valid_rect2 = False
                                                break
                                        if not valid_rect2:
                                            break

                                    if not valid_rect2:
                                        continue

                                    area2 = (r2_end - r2_start + 1) * (c2_end - c2_start + 1)

                                    if area1 != area2:
                                        continue

                                    intersect = False
                                    for r in range(r1_start, r1_end + 1):
                                        for c in range(c1_start, c1_end + 1):
                                            if r2_start <= r <= r2_end and c2_start <= c <= c2_end:
                                                intersect = True
                                                break
                                        if intersect:
                                            break

                                    if intersect:
                                        continue

                                    if area1 > max_area:
                                        max_area = area1
                                        best_rect1 = [r1_start, c1_start, r1_end, c1_end]
                                        best_rect2 = [r2_start, c2_start, r2_end, c2_end]

    if max_area > 0:
        print("Area:", max_area)
        print("Coordinates: [[{}, {}, {}, {}], [{}, {}, {}, {}]]".format(
            best_rect1[0], best_rect1[1], best_rect1[2], best_rect1[3],
            best_rect2[0], best_rect2[1], best_rect2[2], best_rect2[3]
        ))
    else:
        print("Area: 0")
        print("Coordinates: [[], []]")


solve()