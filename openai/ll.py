class Node(object): 
  def __init__(self, data): 
      self.data = data 
      self.next = None
      self.prev = None
  
class DoublyLinkedList(object): 
  def __init__(self): 
      self.head = None
  
  def append(self, data): 
      if self.head is None: 
          newNode = Node(data) 
          newNode.prev = None
          self.head = newNode 
      else: 
          newNode = Node(data) 
          cur = self.head 
          while cur.next: 
              cur = cur.next
          cur.next = newNode 
          newNode.prev = cur 
          newNode.next = None
  
  def printList(self, node): 
      print("\nTraversal in forward direction") 
      while node is not None: 
          print(node.data) 
          last = node 
          node = node.next
      print("\nTraversal in reverse direction")
      while last is not None: 
          print(last.data) 
          last = last.prev 

dllist = DoublyLinkedList() 
dllist.append(1) 
dllist.append(4) 
dllist.append(5) 
dllist.printList(dllist.head)

