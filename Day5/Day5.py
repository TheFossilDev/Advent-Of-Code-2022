# ========= HELPERS =========
def populateInitialStacks(file):
  cargoLines = []
  for line in file:
    if line == "\n":
      break
    cargoLines.append(line[:len(line)-1]) # Cut off trailing newline
  # print(cargoLines)
  numStacks = int(cargoLines[-1].strip()[-1])
  cargoLines = cargoLines[::-1]
  cargoLines = cargoLines[1:]
  cargo = [[] for i in range(numStacks)]

  for line in cargoLines:
    # Skipping first line of reversed cargolines
    for i in range(0, len(line), 4):
      item = line[i+1]
      # print(item, end=" ")
      if item != " ":
        cargo[i // 4].append(item)
  
  return cargo

def moveStack(cargo, command, printMove = False):
  lineParts = command.strip().split(" ")
  quant, origin, dest = int(lineParts[1]), int(lineParts[3]), int(lineParts[5])
  if printMove:
    print(f"Q{quant} S{origin} D{dest}")
  
  for i in range(quant):
    cargo[dest-1].append(cargo[origin-1].pop())

def moveStackSliceable(cargo, command, printMove = False):
  lineParts = command.strip().split(" ")
  quant, origin, dest = int(lineParts[1]), int(lineParts[3]), int(lineParts[5])
  holding = cargo[origin-1][len(cargo[origin-1])-quant:len(cargo[origin-1])]
  for i in range(quant):
    cargo[origin-1].pop()
  cargo[dest-1] = cargo[dest-1] + holding
  if printMove:
    print(f"Q{quant} S{origin} D{dest}")
    print("holding",holding)
    print("After move")
    printCargo(cargo)

def cargoPeek(cargo):
  out = ""
  for stack in cargo:
    out += stack[-1]
  return out


def printCargo(cargo):
  for i in range(len(cargo)):
    print(f"Stack #{i+1}:{cargo[i]}")

def partOne(inputFile):
  cargo = populateInitialStacks(inputFile)
  printCargo(cargo)
  print(cargoPeek(cargo))
  for line in inputFile:
    moveStack(cargo, line)
  return "Final tops of stacks:", cargoPeek(cargo)

def partTwo(inputFile):
  cargo = populateInitialStacks(inputFile)
  printCargo(cargo)
  print(cargoPeek(cargo))
  for line in inputFile:
    moveStackSliceable(cargo, line, printMove=False)
  return f"Final tops of stacks: {cargoPeek(cargo)}"

inputFile = open("input.txt", "r")
# partOne(inputFile)
print(partTwo(inputFile))