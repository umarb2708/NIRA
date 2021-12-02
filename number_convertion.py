

def decimalToBinary(n):
    bi= bin(n).replace("0b", "")
    if len(bi) < 3:
        for i in range(len(bi),4):
            bi=bi+"0"
    print("DEBUG::CONV->binary="+bi)
    return bi


#bi=decimalToBinary(6)
#print (bi[2])
