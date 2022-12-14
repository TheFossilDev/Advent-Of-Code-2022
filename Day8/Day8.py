def PartOne(map) -> str:
  HEIGHT, WIDTH = len(map), len(map[0])
  visibleMap = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT-1)]
  visibleMap.append([1 for _ in range(WIDTH)])
  visibleMap.insert(0,[1 for _ in range(WIDTH)])
  for i in range(1, HEIGHT):
    visibleMap[i][0] = 1
    visibleMap[i][-1] = 1
  
  # Peek top
  for i in range(WIDTH):
    depth = 1
    while depth < HEIGHT and map[depth][i] > map[depth-1][i]:
      visibleMap[depth][i] = 1
      depth += 1

  # Peek right
  for i in range(1, HEIGHT-1):
    depth = WIDTH - 2
    while depth >= 0 and map[i][depth+1] < map[i][depth]:
      visibleMap[depth][i] = 1
      depth -= 1


  # Peek left
  for i in range(1, HEIGHT-1):
    depth = 1
    while depth < WIDTH and map[i][depth] > map[i][depth-1]:
      visibleMap[depth][i] = 1
      depth += 1


  # Peek bottom
  debugFile = open("debug.txt", "w")
  DebugMapPrinter(visibleMap, debugFile)
  print("\n\n\n", file=debugFile)
  DebugMapPrinter(map, debugFile)

def DebugMapPrinter(map, outFile):
  for line in map:
    for val in line:
      print(val, end="", file=outFile)
    print(file=outFile)

def MakeMap(filename):
  inputFile = open(filename, "r")
  map = []
  for line in inputFile.readlines():
    newLine = []
    for char in line.strip():
      newLine.append(int(char))
    map.append(newLine)

  return map


def main():
  filename = "input.txt"
  map = MakeMap(filename)

  PartOne(map)

main()