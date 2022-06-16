class Node:
    def __init__(self,initial=None):
        self.data=initial
        self.next=None
    def isempty(self):
        return(self.data==None)
    def append(self,n):
        if self.isempty():
            self.data=n
        elif self.next==None:
            newnode=Node(n)
            self.next=newnode
        else:
            (self.next).append(n)
    def insert(self,n):
        if self.isempty():
            self.data=n
        else:
            newnode=Node(n)
            (self.data,newnode.data)=(newnode.data,self.data)
            (self.next,newnode.next)=(newnode,self.next)
    def delete(self,n):
        if self.next==None:
                self.value=None
        if self.data==n:
                self.data=self.next.data
                self.next=self.next.next
        else:
            if self.next != None:
                self.next.delete(n)
                if self.next.value == None:
                    self.next=None
    def __str__(self):
        l=[]
        if self.data != None:
            return(str(l))
        temp=self
        l.append(temp.data)
        while temp.next != None:
            temp=temp.next
            l.append(temp.data)
        return(str(l))
    
pairs = [ (x,y) for x in range(3,0,-1) for y in range(2,0,-1) if (x+y)%3 == 0]