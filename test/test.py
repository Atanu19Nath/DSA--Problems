# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linkedlist(arr):
    if not arr:   # empty array
        return None

    head = ListNode(arr[0])  # first node
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def removeNthFromEnd(head, n):
        
        if head.next == None:

            if n == 1:

                return None

        size = 0

        current = head

        while current:

            size +=1

            current= current.next


        print(size)

# 🔹 Example usage
arr = [1, 2, 3, 4, 5]
linked_list = array_to_linkedlist(arr)

# Print linked list to verify
current = linked_list
while current:
    print(current.val, end=" -> ")
    current = current.next
