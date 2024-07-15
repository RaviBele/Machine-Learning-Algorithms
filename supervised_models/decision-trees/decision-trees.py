class TreeNode:
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.split_point = None
        self.length = len(examples)
        self.best_feature = None

    def split(self):
        if len(self.examples) == 1:
            return
        mse = float('inf')
        best_left = None
        best_right = None
        best_feature = None
        best_split_point = None
        for feature in self.examples[0].keys():
            if feature == "bpd":
                continue
            
            self.examples.sort(key=lambda example:example[feature])

            for i in range(self.length-1):
                adjacent_average = (self.examples[i][feature] +  self.examples[i+1][feature]) / 2
                left = []
                right = []
                for example in self.examples:
                    if example[feature] <= adjacent_average:
                        left.append(example)
                    else:
                        right.append(example)
                
                left_sum = 0
                left_len = len(left)
                left_total = 0
                for example in left:
                    left_total += example['bpd']
                
                left_average = left_total / left_len
                for example in left:
                    left_sum += (example['bpd'] - left_average)**2


                right_sum = 0
                right_len = len(right)
                right_total = 0
                for example in right:
                    right_total += example['bpd']

                right_average = right_total / right_len
                for example in right:
                    right_sum += (example['bpd'] - right_average)**2

                mse_current = (left_sum + right_sum) / self.length

                if mse > mse_current:
                    best_left = left
                    best_right = right
                    mse = mse_current
                    best_split_point = adjacent_average
                    best_feature = feature

        self.left = TreeNode(best_left)
        self.left.split()
        self.right = TreeNode(best_right)
        self.right.split()
        self.split_point = best_split_point
        self.best_feature = best_feature

class RegressionTree:
    def __init__(self, examples):
        self.root = TreeNode(examples)
        self.train()

    def train(self):
        self.root.split()

    def predict(self, example):
        node = self.root
        while node.left or node.right:
            print(node.best_feature)
            best_feature = node.best_feature
            split_point = node.split_point
    
            if example[best_feature] <= node.split_point:
                node = node.left
            elif node.right:
                node = node.right

        print(len(node.examples))
        return node.examples[0].get('bpd')
        