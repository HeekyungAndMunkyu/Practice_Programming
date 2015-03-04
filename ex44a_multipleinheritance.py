class Parent(object):
    def hi(self):
        print "Parent hi"

class Child1(Parent):
    def hi(self):
        print "Child1 hi"

class Child2(Parent):
    def hi(self):
        print "Child2 hi"

class GrandChild(Child1, Child2):
    pass


GrandChild().hi()
