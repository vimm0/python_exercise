class library():
    x = 0
    name=""
    def __init__(self,nam):
        self.name = nam
        print("Hello",self.name)
    def __book__(self):
        self.x = self.x + 1
        print("Borrower",self.name)
a = library("Sally")#object a
a.book()#instance of object a
#or a is the variable that is calling the method book of class library
b = library("Sandesh Rana")#object b
b.book()#instance of object b
