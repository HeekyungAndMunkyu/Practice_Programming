# encoding=utf8

# FINAL EXAM
# Problem 7
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name



def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    # after atMe
    if atMe.myName() <= newFrob.myName():
        print atMe.myName(), '<=', newFrob.myName()
        # compare with those after
        nextFrob = atMe
        print 'nextFrob = atMe', nextFrob.myName()
        foundPlace = False
        while not foundPlace:
            print 'ummm', nextFrob.myName()
            if nextFrob.getAfter() == None:
                print 'here', nextFrob.myName()
                newFrob.setBefore(nextFrob)
                nextFrob.setAfter(newFrob)
                foundPlace = True

            else:
                if newFrob.myName() <= nextFrob.getAfter().myName():
                    newFrob.setBefore(nextFrob)
                    print ' ', newFrob.getBefore().myName(), 'and', newFrob.myName()
                    newFrob.setAfter(nextFrob.getAfter())
                    print ' ', newFrob.myName(), 'and', newFrob.getAfter().myName()
                    nextFrob.getAfter().setBefore(newFrob)
                    print ' ', nextFrob.getAfter().getBefore().myName(), 'and', nextFrob.getAfter().myName()
                    nextFrob.setAfter(newFrob)
                    print ' ', nextFrob.myName(), 'and', nextFrob.getAfter().myName()

                    print
                    foundPlace = True
                else:
                    nextFrob = nextFrob.getAfter()

    # before atMe
    else:
        print atMe.myName(), '>' , newFrob.myName()
    # compare with those before
        nextFrob = atMe
        foundPlace = False
        while not foundPlace:
            if nextFrob.getBefore() == None:
                newFrob.setAfter(nextFrob)
                nextFrob.setBefore(newFrob)
                foundPlace = True

            else:
                if newFrob.myName() >= nextFrob.getBefore().myName():
                    newFrob.setAfter(nextFrob)
                    newFrob.setBefore(nextFrob.getBefore())
                    nextFrob.getBefore().setAfter(newFrob)
                    nextFrob.setBefore(newFrob)
                    foundPlace = True
                else:
                    nextFrob = nextFrob.getBefore()


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

print 'andrew and', andrew.getAfter().myName()
print eric.getBefore().myName(), 'and eric'
print 'eric and', eric.getAfter().myName()
print fred.getBefore().myName(), 'and fred'
