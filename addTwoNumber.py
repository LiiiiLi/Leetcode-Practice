# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        an = ""
        while self.next:
            an+=str(self.val)  # 当前节点值
            self = self.next
        an += str(self.val)
        return an
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        start = lan = ListNode()
        add = 0
        first = True
        # 只要 l1和 l2不全为空，则继续
        while self.Continue(l1,l2):
            if first:
                val ,add = self.addAndForward(l1,l2,add)
                lan.val = val
                l1 = self.Next(l1)
                l2 = self.Next(l2)
                first = False
            else:
                lan.next = ListNode()
                lan = lan.next
                val ,add = self.addAndForward(l1,l2,add)
                lan.val = val
                l1 = self.Next(l1)
                l2 = self.Next(l2)

        if add:
            lan.next = ListNode()
            lan = lan.next
            lan.val = add

        return start


    def Continue(self,l1,l2):
        return l1 or l2
    def ifEmpty(self,l1,l2):
        return l1 and l2
    def Next(self,l):
        if l:
            if l.next:
                return l.next
            else:
                return 0
        else:
            return 0
    # l1和 l2当前节点相加，可以容忍一个空节点
    # 返回相加后的值和进位
    def addAndForward(self,l1,l2,add):
        if l1 and l2:
            val = (l1.val+l2.val+add)%10
            add = (l1.val+l2.val+add)//10
            return val,add
        elif l2:
            l1 = l2
        val = (l1.val  + add) % 10
        add = (l1.val  + add) // 10
        return val,add


# ==========case 1===============
# l1 = [9,9,9,9,9,9,9]
l1 = ListNode(9,None)
for i in range(6):
    l1 = ListNode(9,l1)
# l2 = [9,9,9,9]
l2 = ListNode(9,None)
for i in range(3):
    l2 = ListNode(9,l2)
# =================================
# ==========case 2===============
# # l1 = [0]
# l1 = ListNode(0,None)
# # l2 = [0]
# l2 = ListNode(0,None)
# =================================
s = Solution()
an = s.addTwoNumbers(l1,l2)
l1 = an
print(l1)

# 废弃代码1
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         add = 0
#         Nnode = ListNode(0,None)
#         if l1.val ==0 & l2.val==0:
#             return Nnode
#         # 即：l1=0，l2≠0
#         if l1.val==0:
#             return l2
#         lan = ListNode(0, None)
#         start = lan
#         while self.Continue(l1,l2):
#             print("count for add operation")
#             v1 = lambda l1:l1.val if l1 else 0
#             v2 = lambda l2: l2.val if l2 else 0
#             val =(l1.val+l2.val+add)%10
#             add = (l1.val+l2.val+add)//10
#             lan.val = val
#             lan.next = ListNode(0,None)
#             lan  = lan.next
#             # lan.next = ListNode(val, None)
#             l1 =  l1.next
#             l2 =  l2.next
#         # print("l1=",l1)
#         # print("l2=",l2)
#         if l1:
#             ladd = l1
#         else:
#             ladd = l2
#         lad = ladd
#
#         if add and ladd.next:
#             print("======add=======")
#             print("ladd=",ladd,"\nladd.next=",ladd.next)
#             ladd = self.addTwoNumbers(ladd, ListNode(add, None))
#             print("1: ladd=",ladd)
#             print("======add end=======")
#
#         elif add:
#             print("ladd=", ladd)
#             val = (ladd.val + add) % 10
#             add = (ladd.val  + add) // 10
#             ladd.val = val
#             ladd.next = ListNode(0, None)
#             ladd = ladd.next
#             ladd.val = add
#             add = 0
#
#         lan.next = lad
#         print("start=",start)
#
#
#         # if l1:
#         #     l1 = self.addTwoNumbers(l1,ListNode(add,None))
#         #     lan.next =l1
#         # else:
#         #     l2 = self.addTwoNumbers(l2, ListNode(add, None))
#         #     lan.next =l2
#         return start
#
#
#     def Continue(self,l1,l2):
#
#         return l1 and l2
