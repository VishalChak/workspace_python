class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

if __name__ == "__main__":
    head = None
    for i in range(10):
        node = Node(i)
        if head == None:
            head = node
            temp = node
        else:
            temp.nextval= node
            temp = temp.nextval
    temp = head
    while(temp!=None):
        print(temp.dataval)
        temp= temp.nextval
    print("-----------")

    temp = head

    prev = None
    next = None

    while(temp!=None):
        next = temp.nextval
        temp.nextval = prev
        prev = temp
        temp=next
    
    temp = prev
    # print(prev.dataval)

    while(temp!=None):
        print(temp.dataval)
        temp= temp.nextval
