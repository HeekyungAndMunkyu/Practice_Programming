# -*- coding: utf-8 -*-

class Parent(object):

    def override(self):
        print u"부모 override()"


class Child(Parent):

    def override(self):
        print u"자식 override()"

dad = Parent()
son = Child()

dad.override()
son.override()
