inputString = str(input("Enter your string:"))
hasString=False;
hasNumber=False;
for i in inputString:
    if(i.isnumeric()):
        hasNumber=True
    if(i.isalpha()):
        hasString=True
if(hasString):
    print("your string has letter") 
if(hasNumber):
    print("your string has number") 

