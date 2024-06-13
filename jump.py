# given an arr[] of size n of non-ve  integers  each element represents  the maximum length
# of the jumps that can be made forword from that element,This means if arr[]=x,then we can jump any distance y such that
# y=<x.
def min_jumps(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 1
    max_reach = arr[0]
    steps = arr[0]
    for i in range(1, n):
        if i == n - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i

    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = 11
result = min_jumps(arr)
print(result)