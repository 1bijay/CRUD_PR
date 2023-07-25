class Person():
    def __init__(self, pid =0, name = '', adress=''):
        self.pid = pid
        self.name = name
        self.adress = adress

        #getters
        def  getPID(self):
            return self.pid
        def getName(self):
            return self.name
        def getAdress(self):
            return self.adress

        # setters
        def setPID(self,pid):
            self.pid =pid
        def setName(self,name):
            self.name = name
        def setAdress(self,adress):
            self.adress=adress
        # toString
        def __str__(self):
            return str(self.pid)+","+self.name+","+self.adress

