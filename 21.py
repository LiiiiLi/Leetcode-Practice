# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        while current_node:
            print(current_node.val, end=" ")
            current_node = current_node.next
        # return str(self.val)
        return ""
        # return format("{0},{1},{2}",str(self.val),print(self.next))
# 构造链表
def ListToListNodes(list):
    if len(list)==0:
        return ListNode()
    if len(list)==1:
        return ListNode(list[0])
    node = ListNode(list.pop())
    # print(node)
    for i in range(len(list)):
        node  = ListNode(list.pop(),node)
    return node




class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1=[1,2,3]
# print(l1)
l2 = [2,3]
l3 = [5,6]
list1 = ListToListNodes(l1)
print(list1)
# current_node=list1
# while current_node:
#     print(current_node, end=" ")
#     current_node = current_node.next
# print(list1)
list2 = ListToListNodes(l2)
s = Solution()
print("solution")
current_node = s.mergeTwoLists(list1,list2)
print(current_node)









# ========= Dumping Codes
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#
#     def list_to_linkedlist(self, input_list):
#         for item in input_list:
#             self.append(item)
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.val, end=" ")
#             current_node = current_node.next
#         print()
#
#     def __str__(self):
#         result = []
#         current_node = self.head
#         while current_node:
#             result.append(str(current_node.data))
#             current_node = current_node.next
#         return ' -> '.join(result)

# 示例用法
# my_list = [1, 2, 3, 4, 5]
#
# linked_list = LinkedList()
# linked_list.list_to_linkedlist([1,2,3])
# linked_list.print_list()  # 输出: 1 2 3 4 5