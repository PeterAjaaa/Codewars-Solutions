# Link to kata: https://www.codewars.com/kata/5acf710f46b4cb00810001e2

class Tree:
    def __init__(self, trunks):
        self.trunks = trunks
        self.branches = trunks * 10
        self.twigs = trunks * 100
        self.leaves = trunks * 1000
        
    def chop_trunk(self, n):
        if n > self.trunks: # If 'n' parameter > self.trunks, add to every self values so that it returns 0.
            self.trunks = n
            self.branches = n * 10
            self.twigs = n * 100
            self.leaves = n * 1000
        self.trunks -= n
        self.branches -=n * 10
        self.twigs -= n * 100
        self.leaves -= n * 1000
        
    def chop_branch(self, n):
        self.branches -= n
        self.twigs -= n * 10
        self.leaves -= n * 100
    
    def chop_twig(self, n):
        self.twigs -= n
        self.leaves -= n * 10
    
    def chop_leaf(self, n):
        self.leaves -= n
    
    def describe(self):
        return "This tree has {} trunks, {} branches, {} twigs and {} leaves.".format(self.trunks, self.branches, self.twigs, self.leaves)

# Used {}.format() to avoid changing self values to str (required by the kata author).
