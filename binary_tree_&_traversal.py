class Tree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def assignment(self,data):
        if self.data==data:
            return
        else:
            if data<self.data:
                if self.left:
                    self.left.assignment(data)
                else:
                    self.left=Tree(data)
            else:
                if self.right:
                    self.right.assignment(data)
                else:
                    self.right=Tree(data)


    def inOrderTraversal(self):
        elements=[]
        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def search(self,value):
        if self.data==value:
            return True
        else:
            if value<self.data:
                if self.left:
                    return self.left.search(value)
                else:
                    return False
            else:
                if self.right:
                    return self.right.search(value)
                else:
                    return False


def build_tree(elements):
    root=Tree(elements[0])
    for i in range(1,len(elements)):
        root.assignment(elements[i])
    return root



if __name__=='__main__':
    numbers=list(input().split())
    numbers_tree=build_tree(numbers)
    id=int(input())
    print(numbers_tree.inOrderTraversal())
    print(numbers_tree.search(id))
    
