class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLable(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLable() + "-->")
        
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinA == None:
            return input("Enter Pin B input for gate " + self.getLable() + "-->")
        
        else:
            return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getLable() + "-->"))

class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()

        if int(a) == 1 and int(b) == 1:
            return 1
        else:
            return 0
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No empty pins.")

g1 = AndGate("G1")
print(g1.getOutput())

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate


    
G1 = AndGate('G1')
G2 = AndGate('G2')
G3 = AndGate('G3')
C1 = Connector(G1, G3)
C2 = Connector(G2, G3)
print(G3.getOutput())