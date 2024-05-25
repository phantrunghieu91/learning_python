class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def createLinkedList(self, arr, pos):
    if len(arr) == 0:
      return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
      current.next = ListNode(arr[i])
      current = current.next
    # Create cycle
    if pos != -1:
      cycle = head
      for i in range(pos):
        cycle = cycle.next
      current.next = cycle
    return head
  def hasCycle(self, head):
    """
      :type head: ListNode
      :rtype: bool
    """
    if head == None:
      return False
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False

def main():
  head = Solution().createLinkedList([3, 2, 0, -4], 1)
  print(Solution().hasCycle(head)) # True        

if __name__ == "__main__":
  main()