# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        head.next = curr

        if not list1 and not list2:
            return None

        while(list1 and list2):
            temp = None
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            curr.next = temp
            curr = curr.next
        if(not list1 and list2):
            curr.next = list2
        if(not list2 and list1):
            curr.next = list1
        
        return head.next           
            


           


        
            

        