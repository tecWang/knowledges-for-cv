# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        
        if pHead.next is None:
            return pHead
        
        head = ListNode(0)
        head.next = pHead

        pre = head
        temp = head.next
        while temp:
            if temp.next != None and temp.val == temp.next.val:
                while (temp.next != None and temp.val == temp.next.val):
                    temp = temp.next

                pre.next = temp.next
                temp = temp.next
            else:
                pre = pre.next
                temp = temp.next
                
        return head.next

# 创建链表
head = ListNode(0)
temp = head
# for val in [1,2,3,3,4,4,5]:
for val in [1,1,1,1,1,1,2]:
    temp.next = ListNode(val)
    temp = temp.next

# 遍历链表确认没有问题
head_print = head.next
while head_print:
    print(head_print.val, end=", ")
    head_print = head_print.next
print()

res = Solution().deleteDuplication(head.next)
while res:
    print(res.val, end=", ")
    res = res.next
print()