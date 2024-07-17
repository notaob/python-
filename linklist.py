class Node(object):
    
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        return self._head==None
    
    def length(self):
        cur=self._head
        count=0
        while cur!=None:
             count += 1 
             cur=cur.next     
        return count

    def travel(self):
        cur=self._head
        while cur!= None:
            print(cur.elem)
            cur=cur.next

    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=node

    def append(self,item):
        node =Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur = self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def insert(self,pos,item):  
        if pos<=0:
            self.add(item)
        if pos>self.length()-1:
            self.append(item)
        pre=self._head
        count=0
        while count<pos-1:
            pre=pre.next
            count+=1
        node=Node(item)
        node.next=pre.next
        pre.next=node
        
    def remove(self,item):
        pass
    def search(self,item):
        pass

if __name__=="__main__":
    lls=SingleLinkList();
    print(lls.is_empty())
    print(lls.travel())
    lls.append(1)
    lls.append(2)
    lls.add(8)
    lls.insert(1,100)
    print(lls.is_empty())
    print(lls.travel())
    print(lls.length())