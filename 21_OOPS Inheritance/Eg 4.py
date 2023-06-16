# Hierarchical
class GrandParent:
    def d1(self):
        print('d1 method')

class Parent(GrandParent):
    def d2(self):
        print('d2 method')

class Child(GrandParent):
    def d3(self):
        print('d3 method')

c = Child()
c.d1()
c.d3()

p = Parent()
p.d1()
p.d2()
