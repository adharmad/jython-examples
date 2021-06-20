from java.lang import Cloneable 

class A(Cloneable):
    def __init__(self, x=12, y=34):
        self.x = x
        self.y = y

    def clone(self):
        a = A()
        a.x = self.x
        a.y = self.y
        return a

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

aa = A(55, 66)
print str(aa)
bb = aa.clone()
print str(bb)
