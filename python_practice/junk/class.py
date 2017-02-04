class A():
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print (self.x + ' ' + foo)

a = A()
print(a.method_a('may'))
