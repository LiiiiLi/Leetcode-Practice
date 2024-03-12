# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        # out = str(self.val)+str(self.left)+str(self.right)
        # return out
        return tree_to_str_bfs(self)
def tree_to_str_bfs(root):

    if not root:
        return "None"

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        try:
            print("\ncurrent val",current.val)
        except:
            pass

        if current:
            result.append(str(current.val))
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("None")

    # 在字符串中保留 None 节点
    # while result and result[-1] == "None":
    #     result.pop()

    return ",".join(result)
    # if not root:
    #     return "None"
    #
    # result = []
    # queue = deque([root])
    #
    # while queue:
    #     current = queue.popleft()
    #
    #     if current:
    #         result.append(str(current.val))
    #         queue.append(current.left)
    #         queue.append(current.right)
    #     else:
    #         result.append("None")
    #
    # # 去除末尾的连续 "null"
    # while result and result[-1] == "None":
    #     result.pop()
    # return ",".join(result)
    # # return "[" + ",".join(result) + "]"
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if cloned == None:
            return None
        if cloned.val == target.val:
            return cloned

        # print(original,cloned)

        leftnode = self.getTargetCopy(original.left, cloned.left, target)
        # print("lft called once")
        if (leftnode != None):
            return leftnode
        rightnode = self.getTargetCopy(original.right, cloned.right, target)
        # print("rgt called once")
        if rightnode != None:
            return rightnode
        return None
# def list_to_Tree(list):
#     # i = 0
#     # layer = 0
#     lr = 0
#     tree = TreeNode(None)
#     if len(list)==0:
#         return tree
#     if len(list)==1:
#         tree.val = list[0]
#         return tree
#     tree.val = list.pop(0)
#     node = tree
#     while len(list)>0:
#         i = 0
#         while i < 2:
#             try:
#                 tmp = list.pop(0)
#             except:
#                 return tree
#             if lr ==0:
#                 node.left ==TreeNode(tmp)
#                 lr = 1
#                 i += 1
#             else:
#                 node.right == TreeNode(tmp)
#                 lr = 0
#                 i += 1



# list = [7,4,3,None,None,6,19]
list = [1,None,1,None,None,1,None]
trnode = list_to_tree(list)
cnode = trnode
target = TreeNode(4)
print("list:",list)
print("tree:",trnode)
s = Solution()
ans = s.getTargetCopy(trnode,cnode,target)
print("answer is:",ans)

