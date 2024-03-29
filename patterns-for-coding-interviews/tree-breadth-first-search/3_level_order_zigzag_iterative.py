class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root, reverse = False):
  flag = True
  result = []
  
  if root is None:
    return result

  traverseArr = [root]
  while len(traverseArr) > 0:
    currLevelSize = len(traverseArr)
    currLevel = []

    for _ in range(currLevelSize):
      currNode = traverseArr.pop(0)
      if flag:
        currLevel.append(currNode.val)
      else:
        currLevel.insert(0, currNode.val)

      if currNode.left:
        traverseArr.append(currNode.left)
      if currNode.right:
        traverseArr.append(currNode.right)

    result.append(currLevel)
    flag = not flag

  if reverse:
    return result[::-1]
  return result

if __name__ == "__main__":
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order zig-zag traversal: " + str(traverse(root)))
