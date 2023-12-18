string = str(input("Enter your string:"))
newstring="";
for i in string: 
     if (i=='A'): 
            newstring=newstring+"B"
     elif (i=='a'): 
            newstring=newstring+"b"
     else:
         newstring=newstring+i

print(newstring)
