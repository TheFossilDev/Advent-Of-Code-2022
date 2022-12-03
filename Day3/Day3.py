inputFile = open("input.txt", "r")

def getPriority(char):
  if char.isupper():
    return ord(char.lower()) - ord("a") + 1 + 26
  else:
    return ord(char.lower()) - ord("a") + 1


sumOfPriorities = 0
for line in inputFile:
  firstCompartment = set(line[:len(line)//2])
  secondCompartment = line[len(line)//2:]
  for char in secondCompartment:
    if char in firstCompartment:
      sumOfPriorities += getPriority(char)
      break

print(sumOfPriorities)


# ==== Part 2 ====
inputFile.close()
inputFile = open("input.txt", "r")

sumOfPriorities = 0
lines = inputFile.readlines()

group = [set(""), set(""), set("")]
for i in range(len(lines)):
  group[i % 3] = set(lines[i].strip())
  if (i+1) % 3 == 0:
    # The group is stored in the sets, now find the intersection
    set1 = group[0].intersection(group[1]) # Intersection will keep only what is shared between two lists
    badgeItemType = set1.intersection(group[2])
    badgeItemType = list(badgeItemType)[0] # I feel ok hard indexing the first value because it's guarenteed that an intersection between the three elves is guarenteed

    sumOfPriorities += getPriority(badgeItemType)

print("Sum of badges:", sumOfPriorities)