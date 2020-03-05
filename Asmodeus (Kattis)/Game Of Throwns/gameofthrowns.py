ignore = input().split()
kids = int(ignore[0])
keep = input().split()
rhaegalPos = 0


throws = []
x = 0
while (x<len(keep)):
  if keep[x] == "undo":
    del(throws[-int(keep[x+1]):])
    x+=2
  else:
    throws.append(int(keep[x]))
    x+=1

print(sum(throws)%kids)
