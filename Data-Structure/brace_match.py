from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    count = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
            print("+1")
        else:
            if s.isEmpty():
                balanced = False
                print("Flip")
            else:
                s.pop()
                print("-1")
        
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker("((5))"))