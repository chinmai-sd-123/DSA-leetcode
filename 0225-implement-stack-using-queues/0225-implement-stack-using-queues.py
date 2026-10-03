class MyStack(object):

    def __init__(self):
        self.queue_in=[]
        self.queue_out=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue_in.append(x)
        for _ in range(len(self.queue_in)-1):
            self.queue_in.append(self.queue_in.pop(0))
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue_in.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue_in[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue_in)==0 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()