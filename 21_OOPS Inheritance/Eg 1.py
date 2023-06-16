# OOPS
# Object-Oriented Programming
# Class is a blue-print or a template
# Object is an instance of a class
# Inheritance mean acquiring the properties from one class to another class
# Polymorphism mean having many forms
# Abstraction mean hiding te data
# Encapsulation mean wrapping the data and their methods into a single unit

# Inheritance
# Single Level
# Multi-Level
# Multiple
# Hybrid
# Hierarchical

class Parent:
    def d1(self):
        print('d1 method')

    @classmethod
    def d2(cls):
        print('d2 method')
class Child(Parent):

    @staticmethod
    def d3():
        print('d3 method')

c = Child()
c.d1()
c.d2()
c.d3()