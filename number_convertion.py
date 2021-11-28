

def decimalToBinary(n):
    bi= bin(n).replace("0b", "")
    bi="000"+bi
    return bi


bi=decimalToBinary(3)
print (bi[0])
