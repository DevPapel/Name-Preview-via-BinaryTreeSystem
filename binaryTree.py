class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements


def tree_maker(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

#name = ["J", "E", "F", "E", "R", "S", "O", "N", "A", "T", "A", "D", "I", "O", "S"]
#name_tree = tree_maker(name)
#print("")
#print("Input name:", name)
#print("\nIn order traversal:", name_tree.in_order_traversal())
#print("\nPost order traversal:", name_tree.post_order_traversal())
#print("\nPre order traversal:", name_tree.pre_order_traversal())

print("\nWelcome to the Name Preview via Binary Tree System")
print("Please write your name for you to see the preview of your name via BinaryTreeSystem")
name = input("Enter your Name: ")
name_to_list = list(name.replace(" ",""))
name_tree = tree_maker(name_to_list)
print("Your Name:", name)
print("\nIn-order traversal preview:", name_tree.in_order_traversal())
print("\nPost-order traversal preview:", name_tree.post_order_traversal())
print("\nPre-order traversal preview:", name_tree.pre_order_traversal())

