from copy import copy
class Node(object):
    def __init__(self,name,category,max_childrens):
        self.name = name
        self.category = category
        self.depth = 1
        self.left = None
        self.right = None
        
    def set_right(self, node):
        self.right = copy(node)
    def set_left(self, node):
        self.left = copy(node)

    def generate_string(self):
        if(self.left):
            return self.name + "("+ self.left.generate_string() + " , " +self.right.generate_string()+")"
        else:
            return self.name
            

    def calculate_depth(self):
        depth_right = 0
        depth_left  = 0
        if(self.right):
            self.right.calculate_depth()
            depth_right = self.right.depth
        if(self.left):
            self.left.calculate_depth()
            depth_left = self.left.depth
        
        self.depth =  depth_right + 1 if depth_right >= depth_left  else depth_left + 1