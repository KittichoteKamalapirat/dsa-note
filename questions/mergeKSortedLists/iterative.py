# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: # do I need  "or len(lists) == 0"
            return
        
        while len(lists) > 1:
            merged = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                res = self.merge(list1,list2)
                merged.append(res)

            lists = merged
        return lists[0]

        
    def merge(self,list1,list2):
        dummy = ListNode(-1)
        cur = dummy


        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1

        if list2:
            cur.next = list2
            
        return dummy.next
            
        
        