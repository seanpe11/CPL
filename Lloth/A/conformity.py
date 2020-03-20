cases = int(input())
combos = []
parallel = []
for x in range(0,cases):
    newSet = set(map(int, input().split()))
    for x in range(len(combos)):
        if combos[x] == newSet:
            parallel[x] += 1
    if newSet not in combos:
        combos.append(newSet)
        parallel.append(1)

awardees = parallel.count(max(parallel)) * max(parallel)
print(awardees)
