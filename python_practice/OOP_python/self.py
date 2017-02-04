class MyClass(object):
    i = 123
    def __init__(self):
        self.i = 345
a = MyClass()
print (a.i)#345
print (MyClass.i)#123

