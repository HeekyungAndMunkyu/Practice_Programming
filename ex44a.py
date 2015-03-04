# -*- coding: utf-8 -*-

class Parent(object):

    def implicit(self):
        print u"부모 implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
