"""
Python3 code to delete middle of a stack without using additional data structure.

Write the deleteMid function where st is the call to the Stack class, 
n is the size of the stack, and curr is the current item number.
"""
class Stack:
    def __init__(self):
        self.items = []
      
    def isEmpty(self):
        return self.items == []
      
    def push(self, item):
        self.items.append(item)
      
    def pop(self):
        return self.items.pop()
      
    def peek(self):
        return self.items[len(self.items)-1]
      
    def size(self):
        return len(self.items)
          
def deleteMid(st, n, curr) :
    pass
  
# Driver function to test above functions
st = Stack()
  
# push elements into the stack
st.push('1')
st.push('2')
st.push('3')
st.push('4')
st.push('5')
st.push('6')
st.push('7')
  
deleteMid(st, st.size(), 0)
  
# Printing stack after deletion
# of middle.
while (st.isEmpty() == False) :
    p = st.peek()
    st.pop()
    print (str(p) + " ", end="")

#Expected output is: 7 6 5 4 3 2 1
 
# This code is contributed by
# Manish Shaw (manishshaw1)