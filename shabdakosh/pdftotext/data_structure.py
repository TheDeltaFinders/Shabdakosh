class FIFO():
    def __init__(self):
        self.container_ = list()

    def pop(self):
        return self.container_.pop(-1)
    
    def push(self,data):
        self.container_.append(data)
    
    @property
    def length(self):
        return len(self.container_)
