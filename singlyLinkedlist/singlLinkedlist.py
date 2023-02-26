# Node class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# singlyLinked list class
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def push(self, val):
    newnod = Node(val)
    
    if not self.head:
      self.head = newnod
      self.tail = self.head
    else:
      self.tail.next = newnod
      self.tail = newnod

    self.length += 1
    return 

  def pop(self):
    if not self.head: return None

    current = self.head
    newtail = current

    while current.next:
      newtail = current
      current = current.next
    
    self.tail = newtail
    self.tail.next = None

    if self.length == 0:
      self.head = None
      self.tail = None
    
    self.length -= 1
    
    return current
    


  
  def printlist(self):
    currentnode = self.head
    while currentnode is not None:
       print (currentnode.val, "->")
       currentnode = currentnode.next
    print("None")


singly = SinglyLinkedList()

singly.push(10)
singly.push(20)
singly.push(30)


singly.pop()

singly.printlist()

  

