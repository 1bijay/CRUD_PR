class Person():
    def __init__(self, pid=0, name='', address=''):
        self.pid = pid
        self.name = name
        self.address = address
    # getters
    def getPID(self):
        return self.pid
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    # setters
    def setPID(self, pid):
        self.pid=pid
    def setName(self, name):
        self.name=name
    def setAddress(self, address):
        self.address=address
    # toString
    def __str__(self):
        return str(self.pid)+", "+self.name+", "+self.address