def find_lost_pencil(n, colors):
    """
    Finds the color of the lost pencil in Ramiz Uncle's collection.

    Args:
        n: The number of pencils in the uncle's collection.
        colors: A list of integers representing the colors of the pencils after Mujgan added a pencil.

    Returns:
        The color of the lost pencil if it can be determined, otherwise -1.
    """

    counts = {}
    for color in colors:
        counts[color] = counts.get(color, 0) + 1

    duplicate_color = None
    for color, count in counts.items():
        if count == 2:
            if duplicate_color is not None:
                return -1  # More than one color appears twice, cannot determine the lost pencil
            duplicate_color = color

    if duplicate_color is None:
        return -1  # No color appears twice, which means Mujgan didn't replace with an existing pencil

    for i in range(1, n + 1):
        if i not in counts:
            return i  # This color is missing, so it's the lost pencil

    return -1  # If we reach here, something went wrong


n = int(input())
colors = []
for _ in range(n):
    colors.append(int(input()))

result = find_lost_pencil(n, colors)
print(result)