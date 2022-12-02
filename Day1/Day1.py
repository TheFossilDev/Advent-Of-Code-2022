# Day 1 Challenge: Find the elf with the most calories and print how many calories that elf has

# We are given a list of snacks separated by newlines, and a blank line separates the snacks held by each elf
# Approach 1: Let's create a list of all of the calories of the elves adn then find the max
# Memory O(n) time O(n)

elfCalorieList = []
FILENAME = "input.txt"
inputFile = open(FILENAME, "r")

elf = 0 # Will track the specific elf's accumulation
for line in inputFile:
  if line == "\n":
    elfCalorieList.append(elf)
    elf = 0
  else:
    elf += int(line.strip())

# Searching for the max manually so I can grab the index easier
currMax = 0
maxElf = 0
for i in range(len(elfCalorieList)):
  if elfCalorieList[i] > currMax:
    currMax = elfCalorieList[i]
    maxElf = i

print("Best elf was #" + str(maxElf) + " with " + str(currMax) + " calories!")

# ============ PART 2 ==============

# So now we need to get the top three. I could consider using a heap so I could easily pull the top three just as easily as the first, but I would rather just run through the list multiple times, removing the max as I go

totalOfThreeElves = 0
for i in range(3):
  currMax = 0
  for elf in elfCalorieList:
    currMax = max(currMax, elf)
  elfCalorieList.remove(currMax)
  totalOfThreeElves += currMax

print("Max of the top three elves is:", totalOfThreeElves)

inputFile.close()
