# Multi level
class GrandParent:
    def d1(self):
        print('d1 method')

class Parent(GrandParent):
    def d2(self):
        print('d2 method')

class Child(Parent):
    def d3(self):
        print('d3 method')

c = Child()
c.d1()
c.d2()
c.d3()
