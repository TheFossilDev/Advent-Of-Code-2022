# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8

FILENAME = "input.txt"
# FILENAME = "testExample.txt"
inputFile = open(FILENAME, "r")

def PartOne(file):
  count = 0
  for line in file:
    ranges = line.strip().split(",")
    s1, e1 = ranges[0].split("-")
    s2, e2 = ranges[1].split("-")
    if int(s1) <= int(s2) and int(e1) >= int(e2):
      print(s1, e1, "contains", s2, e2)
      count += 1
    elif int(s2) <= int(s1) and int(e2) >= int(e1):
      print(s2, e2, "contains", s1, e1)
      count += 1
  return count



def PartTwo(file):
  count = 0
  for line in file:
    ranges = line.strip().split(",")
    s1, e1 = ranges[0].split("-")
    s2, e2 = ranges[1].split("-")
    s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
    if s1 >= s2 and s1 <= e2:
      count += 1
    elif e1 >= s2 and e1 <= e2:
      count += 1
    elif s2 >= s1 and s2 <= e1:
      count += 1
    elif e2 >= s1 and e2 <= e1:
      count += 1
  return count


# print(PartOne(inputFile))
print(PartTwo(inputFile))