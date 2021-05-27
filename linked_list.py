class Node():
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next

class Linked_lst():
    def __init__(self):
        self.head=None

    def insert_node_at_beginning(self,data):
        node=Node(data,self.head)
        node.next=self.head
        self.head=node
        self.print()

    def insert_node_at_the_end(self,data):
        node=Node(data,None)
        if self.head==None:
            self.head=node
    
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=node


    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_node_at_the_end(data)
        self.print()

    def get_length(self):
        count=0
        itr=self.head
        while itr.next:
            itr=itr.next
            count+=1
        print(count)

    def remove(self,index):
        if index==0:
            self.head=self.head.next

        count=0
        itr=self.head
        while itr.next:
            if count==index-1:
                itr.next=itr.next.next

            itr=itr.next
            count+=1
        self.print()

    def insert_at(self,index,data):
        count=0
        itr=self.head
        while itr.next:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1
        self.print()

    
    def print(self):
        if self.head==None:
            print('linked list is empty')
        
        itr=self.head
        ll_data=''
        while itr:
            if itr.next==None:
                ll_data+= str(itr.data)
            ll_data += str(itr.data) + '-->'
            itr=itr.next
        print(ll_data)



# ll=Linked_lst()
# ll.insert_node_at_beginning(15)
# ll.insert_node_at_beginning(21)
# ll.insert_node_at_beginning(12)
# ll.insert_node_at_the_end(36)
# ll.insert_node_at_the_end(2)
# ll.get_length()
# ll.insert_at(3,72)
# ll.remove(3)
# ll.print()