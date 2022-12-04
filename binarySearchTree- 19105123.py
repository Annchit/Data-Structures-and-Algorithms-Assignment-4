class bst_implementation :

    @staticmethod
    
    def main(args) :
    
        tree = BST()
        len = int(input("Enter initial number of nodes \n"))
        curr=0

        while curr<len:
            curr=curr+1
            ele = input ("enter the value for nodes one at a time \n")
            tree.insertNode(ele)
        
        deleteTree = input("enter a/A if you want to delete nodes from the tree ")        
        
        if deleteTree=='a' or deleteTree=='A':
            num = int(input("enter the number of nodes to be deleted from the tree \n"))
            curr=0
        
            while curr<num:
                ele = input ("enter the element to be deleted \n")
                tree.deleteNode(ele)
        
        insertTree = input("enter b/B if you want to insert node into the tree ")

        if insertTree=='b' or insertTree=='B' :
            num = int(input("enter the number of nodes to be inserted to the tree \n"))
            curr=0
        
            while curr<num:
                ele = input ("enter the value of element to be inserted \n")
                tree.insertNode(tree,ele)

        tree.inorder()


class Node :
    
    left = None
    val = 0
    right = None
    
    def __init__(self, val) :
        self.val = val


class BST :
    
    root = None
    
    def insertNode(self, key) :
    
        node = Node(key)
        if (self.root == None) :
            self.root = node
            return
    
        prev = None
        curr = self.root
    
        while (curr != None) :
    
            if (curr.val > key) :
                prev = curr
                curr = curr.left
            elif(curr.val < key) :
                prev = curr
                curr = curr.right
    
        if (prev.val > key) :
            prev.left = node
        else :
            prev.right = node

    def minValueNode(node):
    
        current = node
    
        while(current.left is not None):
            current = current.left
        return current
    
    def deleteNode(root, key):
    
        if root is None:
            return root
        if key < root.val:
            root.left = deleteNode(root.left, key)
        elif(key > root.val):
            root.right = deleteNode(root.right, key)
    
        else:
            if root.left is None:
                curr = root.right
                root = None
                return curr
    
            elif root.right is None:
                curr = root.left
                root = None
                return curr
    
        curr = minValueNode(root.right)
        root.val = curr.val
        root.right = deleteNode(root.right, curr.val)
    
        return root
    
    def inorder(self) :
   
        curr = self.root
        stack =  []
    
        while (curr != None or not (len(stack) == 0)) :
           
            if (curr != None) :
                stack.append(curr)
                curr = curr.left
            else :
                curr = stack.pop()
                print(str(curr.val) + " ", end ="")
                curr = curr.right

if __name__=="__main__":
    bst_implementation.main([])
