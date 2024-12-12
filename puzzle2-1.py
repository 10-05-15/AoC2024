safe = 0

with open('/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle2Levels.txt', 'r') as file:
    for line in file:
        level = []
        level = list(map(int, line.split()))
        for i in range(len(level) - 1):
            safe_temp=0
            h = level[i + 1] - level[i]
            h = abs(h)
            if h > 0 and h < 4:
                safe_temp += 1 
            for j in range(len(level)-1):
                up =0
                down=0
                if level[i] > level[i+1]:
                    down+=1
                elif level[i] < level[i+1]:
                    up+=1
            if up == len(level) or down == len(level):
                safe =  safe + safe_temp
            

print(safe)
