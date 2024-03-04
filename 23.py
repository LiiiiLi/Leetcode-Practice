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
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        这道题和 21 最大的不同在于从两个链表变成了多个链表，那么需要比较的元素就从两个变成了多个
        1. 多个链表元素的比较
        2. 出现空链表时的排除
        """

        while len(lists)>1:
            new_lists = []

            l = len(lists)
            if l==0:
                return 
            elif l==1:
                return lists[0]
            # len(lists)>=2

            while len(lists)>=2:
                l1 = lists.pop()
                l2 = lists.pop()
                new_lists.append(self.mergeTwoLists(l1,l2))
            # if lists has an element
            if lists:
                new_lists.append(lists[0])
            lists = new_lists


        # while(len(lists)):
        #     l2 = lists.pop()
        #     l1 = self.mergeTwoLists(l1, l2)
        return lists[0]

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

l1=[1,2,3]
l2 = [2,3,]
l3 = [5,6]
list1 = ListToListNodes(l1)
list2 = ListToListNodes(l2)
list3 = ListToListNodes(l3)
l = [list1,list2,list3]
# l = []
s =Solution()
sol = s.mergeKLists(l)
print(sol)