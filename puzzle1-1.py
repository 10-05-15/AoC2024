with open('/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle1IDs.txt', 'r') as file:
    column1 = []
    column2 = []

    for line in file:
        num1, num2 = map(int, line.split())
        column1.append(num1)
        column2.append(num2)
    p=True
    dist=0
    while p==True:
        i = min(column1)
        j = min(column2)

        k = abs (i - j)
        dist = dist + k
        column1.remove(i)
        column2.remove(j)
        if len(column1) <= 0:
            p = False

print(dist)


