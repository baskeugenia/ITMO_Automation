class A():

    def __init__(self):
        self.x = 10

class B(A):

    def __init__(self):
        super().__init__()
        self.y = 15


a = A()
print(a.x)

b = B()
print(b.x)
print(b.y)
