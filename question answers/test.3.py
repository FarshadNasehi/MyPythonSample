inputString = input("Enter your Encrypted string:")
splittedStr=inputString.split();
plainStr=""
for item in splittedStr:
    if(item[0].islower()):
        plainStr=plainStr+item[::-1]+" "
    else:
        plainStr=plainStr+item+" "
        
print(plainStr)
    

