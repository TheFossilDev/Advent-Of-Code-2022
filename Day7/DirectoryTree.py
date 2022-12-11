class TreeNode:
  def __init__(self, callingDir, label):
    self.children = []
    self.parent = callingDir
    self.label = label
    self.size = 0

class TreeFile:
  def __init__(self, label, size) -> None:
    self.label = label
    self.size = size


class DirectoryTree:
  def __init__(self, inputFilename):
    self.root = TreeNode(None, "/")
    self.currDir = self.root
    inputFile = open(inputFilename, "r")
    self.shellContents = inputFile.readlines()
    # Pop off init before starting
    self.shellContents.pop(0)

    while self.shellContents:
      # Pop a command
      command = self.shellContents.pop(0).split()
      # Interpret
      if command[1] == "cd":
        self.handleCd(command[2])
      elif command[1] == "ls":
        self.handleLs()
    
    self.calculateDirSizes()


  def handleCd(self, dest):
    if dest == "..":
      self.currDir = self.currDir.parent
      # print("CD UP", self.currDir.label)
    else:
      for child in self.currDir.children:
        if child.label == dest:
          self.currDir = child
          # print("CD DOWN INTO", self.currDir.label)
          return
      print("ERR: File dir not found in cd")

  def handleLs(self):
    while self.shellContents and self.shellContents[0][0] != "$":
      entryCommand = self.shellContents[0].strip().split()
      if entryCommand[0] == "dir":
        # print(f"Adding new dir {entryCommand[1]}")
        self.currDir.children.append(TreeNode(self.currDir, entryCommand[1]))
      else:
        # Going to add just the size to the dir
        # print(f"Adding {entryCommand[0]} to dir {self.currDir.label}")
        self.currDir.children.append(TreeFile(entryCommand[1], int(entryCommand[0])))
      self.shellContents.pop(0)
      
  def calculateDirSizes(self):
    for child in self.root.children:
      if isinstance(child, TreeFile):
        self.root.size += child.size
      else:
        self.root.size += self.calculateDirSizesHelper(child)

  def calculateDirSizesHelper(self, node):
    for child in node.children:
      if isinstance(child, TreeFile):
        node.size += child.size
      else:
        node.size += self.calculateDirSizesHelper(child)
    return node.size

  def printContents(self):
    identLevel = 0
    print(self.root.label)
    for child in self.root.children:
      if isinstance(child, TreeNode):
        self.printContentsHelper(child, identLevel+1)
      else:
        print(f"FILE {child.label} SIZE {child.size}")
  

  def printContentsHelper(self, currDir, identLevel):
    print("-" * identLevel,end="") # Tree lines
    print(f" {currDir.label} size: {currDir.size}")
    for child in currDir.children:
      if isinstance(child, TreeNode):
        self.printContentsHelper(child, identLevel+1)
      else:
        print("-" * (identLevel + 1),end="") # Tree lines
        print(f"FILE {child.label} SIZE {child.size}")



