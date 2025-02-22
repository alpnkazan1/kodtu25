def solve_optimized():
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

    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def rect_sum(r1, c1, r2, c2):
        return prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]

    for r1_start in range(rows):
        for c1_start in range(cols):
            for r1_end in range(r1_start, rows):
                for c1_end in range(c1_start, cols):

                    area1 = (r1_end - r1_start + 1) * (c1_end - c1_start + 1)
                    if rect_sum(r1_start, c1_start, r1_end, c1_end) != area1 or area1 == 0:
                        continue

                    for r2_start in range(rows):
                        for c2_start in range(cols):
                            for r2_end in range(r2_start, rows):
                                for c2_end in range(c2_start, cols):

                                    area2 = (r2_end - r2_start + 1) * (c2_end - c2_start + 1)
                                    if rect_sum(r2_start, c2_start, r2_end, c2_end) != area2 or area2 == 0:
                                        continue

                                    if area1 != area2:
                                        continue

                                    if (r1_start <= r2_end and r1_end >= r2_start and
                                            c1_start <= c2_end and c1_end >= c2_start):
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

solve_optimized()