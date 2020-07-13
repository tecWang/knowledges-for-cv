# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # if pHead1 == None or pHead2 == None:
         #    return -1
        
        ss = []
        while pHead2:
            ss.append(pHead2.val)
            pHead2 = pHead2.next
            
        while pHead1:
            if pHead1.val in ss:
                 return pHead1
            else:
                pHead1 = pHead1.val
                
                