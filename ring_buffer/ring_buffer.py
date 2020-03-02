from doubly_linked_list import DoublyLinkedList


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = None
    self.storage = DoublyLinkedList()

  def __len__(self):
    return self.storage.length

  def append(self, item):
    # while there space is available, add to tail, and update current
    if self.storage.length < self.capacity:
      self.storage.add_to_tail(item)
      self.current = self.storage.tail
    # if theres no more space 
    if self.storage.length == self.capacity:
      # update current value
      self.current.value = item
      # if we're currently at the tail
      if self.current is self.storage.tail:
          # go back to head 
          self.current = self.storage.head
      else:
          # else, go to the next
          self.current = self.current.next

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # TODO: Your code here
    node = self.storage.head
    while node != None:
      if node.value is not None:
        list_buffer_contents.append(node.value)
      node = node.next
    return list_buffer_contents

# ----------------Stretch Goal-------------------
class ArrayRingBuffer:
  def __init__(self, capacity):
    self.storage = RingBuffer(capacity)
    for _ in range(0, capacity):
      self.storage.append(None)
  
  def append(self, item):
    return self.storage.append(item)

  def get(self):
    return self.storage.get()