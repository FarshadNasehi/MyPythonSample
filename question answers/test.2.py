def NoDuplicateExists(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False;
    return True;
    

inputNumber = input("Enter your Number:")
newNumber=int(inputNumber)+1;
while True:
    if (NoDuplicateExists(str(newNumber))):
        print(str(newNumber))
        break
    else:
        newNumber=newNumber+1
    

