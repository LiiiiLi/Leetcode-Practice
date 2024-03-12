# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 94. 二叉树的中序遍历==================================================
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.returnValue(root,output)
        return output
    def returnValue(self,root,output=[]):
        if root == None:
            return
        self.returnValue(root.left,output)
        output.append(root.val)
        self.returnValue(root.right,output)
        return output
tree_node = TreeNode(1,None,TreeNode(2,TreeNode(3)))

# list = [1,None,2,3,4]
# tree_node = list
# ans = s.inorderTraversal(tree_node)
# print(ans)
s = Solution()
tree_node = TreeNode(1)
ans = s.inorderTraversal(None)
print(ans)
s = Solution()
ans = s.inorderTraversal(tree_node)
print(ans)

# 96. 不同的二叉搜索树==================================================
"""
这根本不是树的问题，这nm是动态规划的问题
思路：确定各种遍历方式，然后在每种遍历方式中寻找可能的情况,还需要合并同类项
问题：是纯数学问题还是需要实际实现这些遍历？
前序遍历：根结点 ---> 左子树 ---> 右子树
中序遍历：左子树---> 根结点 ---> 右子树
后序遍历：左子树 ---> 右子树 ---> 根结点
层次遍历：只需按层次遍历即可
"""
# class Solution(object):
#     def numTrees(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n==1 or n==0:
#             return 1
#         memo = {}
#         memo[0] = 1
#         memo[1] = 1
#         for i in range(2,n+1):
#             memo[i]=0
#             for j in range(1,i+1):
#                 memo[i] += memo[j-1]*memo[i-j]
#
#         # print(memo)
#         return memo[n]
# s = Solution()
# ans = s.numTrees(6)
# print(ans)
# ====================106. 从中序与后序遍历序列构造二叉树=============================
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 首先初始化根节点
        node = TreeNode()
        

