class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        (self.children).append(child)

def print_product_tree(root):
    if (root == None):
        return
    q = []
    q.append(root)
    result = []
    while (len(q) != 0):
        n = len(q)
        while (n>0):
            p =q[0]
            q.pop(0)
            result.append(p.data)
            for i in range(len(p.children)):
                q.append(p.children[i])
            n -= 1
    print(result)

if __name__ == "__main__":
    root = TreeNode(3)

    root.add_child(TreeNode(4))
    root.add_child(TreeNode(1))
    root.add_child(TreeNode(9))

    root.children[0].add_child(TreeNode(5))
    root.children[2].add_child(TreeNode(2))
    root.children[2].add_child(TreeNode(7))

    root.children[0].children[0].add_child(TreeNode(8))
    root.children[0].children[0].add_child(TreeNode(6))
    print_product_tree(root)