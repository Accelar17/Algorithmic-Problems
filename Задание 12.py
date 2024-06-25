__name__
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    
    dummy = ListNode()
    current = dummy 
    
   
    ptr1, ptr2 = list1, list2
    
   
    while ptr1 and ptr2:
        if ptr1.val <= ptr2.val:
            current.next = ptr1
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2 = ptr2.next
        current = current.next
    
   
    if ptr1:
        current.next = ptr1
    elif ptr2:
        current.next = ptr2
    
   
    return dummy.next





list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")



list1 = None


list2 = None

merged_list = mergeTwoLists(list1, list2)

if not merged_list:
    print("Empty list")



list1 = None


list2 = ListNode(0)

merged_list = mergeTwoLists(list1, list2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
