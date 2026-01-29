# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is None:
            return True
        val=[]
        temp=head
        while temp:
            val.append(temp.val)
            temp=temp.next
        i=0
        j=len(val)-1
        while i<j:
            if val[i]!=val[j]:
                return False
            i+=1
            j-=1
        return True
        
        