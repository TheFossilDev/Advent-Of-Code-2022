from DirectoryTree import DirectoryTree, TreeNode

def PartOne(dirTree: DirectoryTree):
  totalSum = 0
  CUTOFF_AT_MOST = 100000
  def PartOneTreeSearch(node: TreeNode):
    currSearchSum = 0
    for child in node.children:
      if isinstance(child, TreeNode):
        if child.size <= CUTOFF_AT_MOST:
          print(f"Adding {child.label}'s {child.size}")
          currSearchSum += child.size
        currSearchSum += PartOneTreeSearch(child)
    return currSearchSum

  for child in dirTree.root.children:
    # REMINDER: They can be counted twice
    if isinstance(child, TreeNode):
      if child.size <= CUTOFF_AT_MOST:
        # print(f"Adding {child.label}'s {child.size}")
        totalSum += child.size
      totalSum += PartOneTreeSearch(child)
  return f"Total size of small dirs: {totalSum}"


def PartTwo(dirTree: DirectoryTree):
  SYSTEM_UNUSED_SPACE = 70000000 - dirTree.root.size # 70000000 is total storage size
  SPACE_TO_FREE = 30000000 - SYSTEM_UNUSED_SPACE
  print("Must free", SPACE_TO_FREE)
  def dirCandidateSearch(node: TreeNode):
    candidate = float("inf")
    for child in node.children:
      if isinstance(child, TreeNode):
        if child.size >= SPACE_TO_FREE:
          candidate = min(candidate, child.size)
        candidate = min(candidate, dirCandidateSearch(child))
    return candidate

  deletionCandidate = dirCandidateSearch(dirTree.root)
  return f"You can delete a directory of size {deletionCandidate}"




def main():
  fileName = "input.txt"
  dirTree = DirectoryTree(fileName)
  dirTree.printContents()
  print(PartOne(dirTree))
  print(PartTwo(dirTree))


main()