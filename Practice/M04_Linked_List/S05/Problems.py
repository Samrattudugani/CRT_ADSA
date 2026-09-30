# 1. 876

# class Solution:
#     def middleNode(self, head: ListNode | None) -> ListNode | None:
#       c=0
#       te = head
#       while te:
#         c+=1
#         te = te.next
#       mi = c // 2
#       te = head
#       for i in range(mi):
#         te = te.next
#       return te

# 2. 141
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#       vi = set()
#       te = head
#       while te:
#         if te in vi:
#           return True
#         vi.add(te)
#         te = te.next 
#       return False

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#       s,f = head,head
#       while f and f.next:
#         s = s.next
#         f = f.next.next
#         if s == f:
#           return True
#       return False

## 14
# class Solution:
#     def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
#         c = 0 
#         te = head
#         while te:
#           c += 1
#           te = te.next
#         du = ListNode()
#         du.next = head
#         te = du 
#         for i in range(c-n):
#           te = te.next
#         te.next = te.next.next
#         return du.next

##  21

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         du = ListNode(0)
#         te = du


#         while list1 and list2:
#             if list1.val <= list2.val:
#                 te.next = list1
#                 list1 = list1.next
#             else:
#                 te.next = list2
#                 list2 = list2.next
#             te = te.next

        
#         te.next = list1 if list1 else list2

#         return du.next

