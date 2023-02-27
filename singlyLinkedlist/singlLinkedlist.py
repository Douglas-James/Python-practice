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

  # Reverse the -infinity - +infinity order to a - z
  def reverse(self):

    arr = []
    # node  current head 
    node = self.head

    # head equal to the tail
    self.head = self.tail

    #let next be None
    next = None

    # prev equal to None
    prev = None
    

    # length of length


    for i in range(0, self.length):
      arr.append(node.val)
      next = node.next
      node.next = prev

      prev = node
      node = next
    
    return arr
  
  # get would get the val of index you have requested
  def get(self, index):
    # index shouldn't access below zero or greater then the length 
    if index < 0 or index >= self.length: return None
    # count becuse we are going to use while loop
    count = 0

    # currenthead would equal to the head
    currenthead = self.head

    # while loop is not we equal and is not index
    while count != index:
      # currenthead is equal to next head
      currenthead = currenthead.next
      # count incremented by one
      count += 1
    
    # return currenthead val equal value
    return currenthead.val

  # remove use the index to remove the val
  # def remove(self, index):
  #   if index < 0 or index >= self.length: return None 
  #   if index == 0: return self.shift()
  #   if index == self.length - 1: return self.pop()
    

  #   self.length -= 1
  #   return self


  # print list method show me in details
  def printlist(self):
    arr = []
    currentnode = self.head
    while currentnode is not None:
       arr.append(currentnode.val)
       currentnode = currentnode.next
    return arr
  
  # sort method should sort array
  def sort(self):
   arr = []
   currentnode = self.head
   while currentnode is not None:
      arr.append(currentnode.val)
      currentnode = currentnode.next
  
   length = len(arr)

  #  print(length) # it just check the length of the arr

   # here we could use self.length 
   for i in range(length):
       for j in range(0, length-i-1):
          if arr[j] > arr[j+1] :
              arr[j], arr[j+1] = arr[j+1], arr[j]      
   return arr



singly = SinglyLinkedList()

# push
singly.push(40)
singly.push(20)
singly.push(30)
singly.push(-1)
singly.push(-2)
singly.push(3)
singly.push(1000)

# pop method remove from the last
singly.pop()


# shift method remove from the first
singly.shift()


# unshift
singly.unshift(50)
singly.unshift(300)

# get method should get index of val
print(singly.get(2))

# remove 
# singly.remove(2)

# sort should sort the array passed upon the val
print(singly.sort())


# reverse order
print(singly.reverse())


# print method for me
# print(singly.printlist())


  

