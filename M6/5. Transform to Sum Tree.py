class Solution:
    def toSumTree(Node):
        if(Node == None):
            return 0
        old_val = Node.data
        Node.data = toSumTree(Node.left) + toSumTree(Node.right)
        return Node.data + old_val
