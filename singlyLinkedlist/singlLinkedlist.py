# Node class
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None


# singlyLinked list class
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
 
 # push method would add value to by order
  def push(self, val):
    newnod = Node(val)
    
    if self.head is None:
      self.head = newnod
      self.tail = self.head
    else:
      self.tail.next = newnod
      self.tail = newnod

    self.length += 1
    return self

  # pop method here should remove the last value add
  def pop(self):
    if self.head is None: return None

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
    
  # shift method here need to remove the first value add
  def shift(self):
    if self.head is None: return None

    currenthead = self.head

    self.head = currenthead.next

    if self.length == 0: self.tail = None

    self.length -= 1
    return currenthead

  # unshift method should add the first value add
  def unshift(self, val):
     newnode = Node(val)

     if self.head is None: 
        self.head = newnode
        self.tail = self.head
     else:
        newnode.next = self.head
        self.head = newnode
     
     self.length += 1
     return self



  # print list method show me in details
  def printlist(self):
    currentnode = self.head
    while currentnode is not None:
       print (currentnode.val, "->")
       currentnode = currentnode.next
    print("None")


singly = SinglyLinkedList()

# push
singly.push(40)
singly.push(20)
singly.push(30)

# pop method remove from the last
singly.pop()


# shift method remove from the first
singly.shift()


# unshift
singly.unshift(30)
singly.unshift(300)


# print method for me
singly.printlist()


  

