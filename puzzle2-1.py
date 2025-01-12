safe = 0
with open('/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle2Levels.txt', 'r') as file:
    for line in file:
        # Convert the line into a list of integers
        level = list(map(int, line.split()))

        # Check if the list is strictly increasing or strictly decreasing
        is_increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
        is_decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))

        # Proceed only if the list is ordered
        if is_increasing or is_decreasing:
            increment_valid = all(0 < abs(level[i] - level[i + 1]) < 4 for i in range(len(level) - 1))
            # Increment the safe counter if valid
            if increment_valid:
                safe += 1

print(safe)
