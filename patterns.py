# cross pattern in python
size = 5

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#5X5  * pattern

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
         print('*',end='')
    print(" \r")

# downward triangle star pattern

n=5
for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()


