with open('/Users/j03/Desktop/Coding/GitHub/AoC/AoC2024/puzzle1IDs.txt', 'r') as file:
    column1 = []
    column2 = []

    for line in file:
        num1, num2 = map(int, line.split())
        column1.append(num1)
        column2.append(num2)

total = 0 
for i in column1:
    k=0
    for j in column2:
        if i == j:
            k += 1
    val = i * k
    total = total + val
print(total)