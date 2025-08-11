class Node:
    def __init__(self,data):
        self.data= data
        self.right= None
        self.left= None

class BinaryTree:
    def __init__(self):
        self.root= None

    def array_to_tree(self, arr):
        if not arr:
            self.root= None
            return

        nodes= []
        for val in arr:
            nodes.append(Node(val))
        
        n =len(arr)

        for i in range(n):
            left_child= 2*i +1
            right_child = 2*i +2

            if left_child < n:
                nodes[i].left= nodes[left_child]
            if right_child < n:
                nodes[i].right = nodes[right_child]
        # even though the previous steps creates the left and right nodes, the start of building the tree is at this line:
        self.root=nodes[0]

    def recursive_array_to_tree(self, arr):
        def helper_function(index):
            # if index is out of bounds, stop
            if index >= len(arr):
                return None
            
            node= Node(arr[index])
            node.left= helper_function(2*index +1)
            node.right= helper_function(2*index +2)
            return node
        self.root= helper_function(0)




# example usage:
a = [7, 12, 9, 25, 30, 15, 40, 50, 60]
bt = BinaryTree()
bt.array_to_tree(a)
r= BinaryTree()
r.recursive_array_to_tree(a)

print(bt.root.data)         # the expected outcome is7
print(bt.root.left.data)    # the expected outcome is 12
print(r.root.right.data)   # the expected outcome is 9 