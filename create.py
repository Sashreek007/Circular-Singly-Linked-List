class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next= new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+= str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head:
                break
            result += '->'
        return result
    
    def prepend(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next= new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.length+=1

    def insert(self,index,value):
        new_node=Node(value)
        
        if index==self.length or index== -1:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        else:      
            temp_node= self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            self.length+=1
    
    def traversal(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
    def search(self,target):
        temp_node = self.head
        count = 0
        while temp_node:
            if temp_node.value == target:
                return count
            temp_node = temp_node.next
            if temp_node == self.head:
                break  
            count+=1
        return False
    
    def get(self,index):
        temp_node=self.head
        for _ in range(index):
            temp_node=temp_node.next
        return temp_node
    
    def set(self,index,value):
        node= self.get(index)
        if node:
            node.value=value
            return True
        return False
    def pop_first(self):
        temp_node=self.head
        self.head=self.head.next
        temp_node.next=None
        self.tail.next=self.head
        self.length-=1
        return temp_node
        
    def pop(self):
        popped=self.tail
        temp=self.head
        while temp.next is not self.tail:
            temp=temp.next
        self.tail=temp
        popped.next=None
        self.tail.next=self.head
        self.length-=1
    
    def remove(self,index):
        prev= self.head
        popped= self.head
        if index == 0:
            return self.pop_first()
        elif index == -1 or index==self.length-1:
            return self.pop()
        elif index >= self.length:
            return None
        else:
            for _ in range(index):
                popped=popped.next
            prev.next = popped.next
            popped.next=None
            self.length -= 1
        return popped.value
    def delete_all(self):
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
        return None



            
new_linked_list=LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.prepend(90)

print(new_linked_list.tail.value)
print(new_linked_list.tail.next.value)
new_linked_list.insert(1,120)
new_linked_list.traversal()
print(new_linked_list.search(180))
new_linked_list.get(2)
new_linked_list.set(0,80)
new_linked_list.set(5,110)
print(new_linked_list)
print(new_linked_list.length)
new_linked_list.pop_first()
new_linked_list.pop()
print(new_linked_list.remove(2))
print(new_linked_list)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.delete_all())
print(new_linked_list)