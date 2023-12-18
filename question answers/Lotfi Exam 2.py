def inputIsFloat(s):
    try:
        n= float(s)
        return 1
    except :
        return 0


listOfNumbers=[]
for i in range(5):
    number= input("Please Enter number "+str(i+1)+":")
    if inputIsFloat(number)==1:
        listOfNumbers.append(float(number))
    else:
        while (1):
            print("Type Should be Float")
            number= input("Please Enter number "+str(i+1)+":")
            if(inputIsFloat(number)==1):
                listOfNumbers.append(float(number))
                break
 
print("----------------------------")
print(sorted(listOfNumbers))
print("----------------------------")
print("Average is : "+str(sum(listOfNumbers)/len(listOfNumbers)))
print("----------------------------")
print("The largest Number is : "+str(max(listOfNumbers)))
print("----------------------------")
print("The Smallest Number is : "+str(min(listOfNumbers)))
print("----------------------------")
print(tuple(sorted(listOfNumbers)))
    

    
