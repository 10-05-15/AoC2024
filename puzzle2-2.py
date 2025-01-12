safe = 0
with open('/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle2Levels.txt', 'r') as file:
    for line in file:
        level = list(map(int, line.split()))

        is_increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
        is_decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))

        if is_increasing or is_decreasing:
            increment_valid = all(0 < abs(level[i] - level[i + 1]) < 4 for i in range(len(level) - 1))
            if increment_valid:
                safe += 1
        else:
            i = 1
            pop_count = 0

            while i < len(level) - 1:
                if (
                    (level[i] <= level[i + 1] and level[i] <= level[i - 1]) or
                    (level[i] >= level[i + 1] and level[i] >= level[i - 1]) or
                    (level[i] == level[i + 1] or level[i] == level[i - 1])):
                    print(level)
                    if pop_count < 1: 
                        level.pop(i)
                        pop_count += 1
                        print(level)

                        is_increasing = all(level[j] < level[j + 1] for j in range(len(level) - 1))
                        is_decreasing = all(level[j] > level[j + 1] for j in range(len(level) - 1))

                        if is_increasing or is_decreasing:
                            increment_valid = all(0 < abs(level[j] - level[j + 1]) < 4 for j in range(len(level) - 1))

                            if increment_valid:
                                safe += 1
                        break 
                    else:
                        break
                else:
                    i += 1

print(safe)
