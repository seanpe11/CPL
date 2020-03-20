n, m = map(int, input().split())
cdList = set()
while True:
    counter = 0
    for jack in range(n):
        cdList.add(int(input()))
    for jill in range(m):
        if (int(input()) in cdList):
            counter+=1
    cdList.clear()
    print(counter)
    n, m = map(int, input().split())
    if (n == 0 and m == 0):
        break
