# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1/,2,4
# 1/,3,5
#
# (None), 1


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode(val = None, next = None)
        tail = sorted_list
        while list1 or list2:
            

            if not list1:
                tail.next = list2
                return sorted_list.next
            if not list2:
                tail.next = list1
                return sorted_list.next

            
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

           


        return sorted_list.next
            

        