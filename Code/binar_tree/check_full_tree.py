from tree_node import TreeNode

class Node(TreeNode):
    def insert(self, value):
      if self.value:
         if value < self.value:
            if self.left is None:
               self.left = Node(value)
            else:
               self.left.insert(value)
            elif value > self.value:
               if self.right is None:
                  self.right = Node(value)
               else:
                  self.right.insert(value)
      else:
         self.value = value
