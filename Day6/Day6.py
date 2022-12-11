def PartOne(filename):
  inputfile = open(filename, "r")
  buffer = inputfile.readline()
  bufferWindow = [buffer[0], buffer[1], buffer[2], buffer[3]]

  for i in range(4,len(buffer)):
    # print("Buffer =", bufferWindow)
    signalValid = True
    for char in bufferWindow:
      if bufferWindow.count(char) != 1:
        signalValid = False
    if signalValid:
      return i
    bufferWindow.pop(0)
    bufferWindow.append(buffer[i])
    

def PartTwo(filename):
  inputfile = open(filename, "r")
  buffer = inputfile.readline()
  bufferWindow = list(buffer[:14])

  for i in range(len(bufferWindow),len(buffer)):
    # print("Buffer =", bufferWindow)
    signalValid = True
    for char in bufferWindow:
      if bufferWindow.count(char) != 1:
        signalValid = False
    if signalValid:
      return i
    bufferWindow.pop(0)
    bufferWindow.append(buffer[i])





filename = "input.txt"
# print(PartOne(filename))
print(PartTwo(filename))