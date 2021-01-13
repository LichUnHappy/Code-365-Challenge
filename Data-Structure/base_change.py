from pythonds.basic import Stack

# def divideBy2(decNumber):
#     remstack = Stack()

#     while decNumber > 0:
#         rem = decNumber % 2
#         remstack.push(rem)
#         decNumber = decNumber // 2
    
#     binString = ""
#     while not remstack.isEmpty():
#         binString = binString + str(remstack.pop())    
    
#     return binString

# print(divideBy2(233))

def divideBy2(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        print(rem)
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]    
    
    return newString

print(divideBy2(233, 16))