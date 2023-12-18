def GetMaxAverage(listOfDict):#بزرگترين معدل را حساب کرده و بر ميگرداند
    TopStudent={"StudentName":"","StudentNumber":"","Average":""}
    topAverage=0
    for x in listOfDict:
        if x==0:
            topAverage=x["Average"]
            TopStudent={"StudentName":x["StudentName"],"StudentNumber":x["StudentNumber"],"Average":x["Average"]}
        elif float(x["Average"])>float(topAverage):
            TopStudent={"StudentName":x["StudentName"],"StudentNumber":x["StudentNumber"],"Average":x["Average"]}
        else:
            continue

    return TopStudent
            

studentCount= input("Enter Quantity of Students: ")
studentsInfo = []
for i in range(int(studentCount)):
    studentName= input("Enter Student Name: ")
    StudentNumber= input("Enter a Student Number: ")
    studentAverage= input("Enter a Mark: ")
    print("**Student Information Recorded**")
    studentsInfo.append({"StudentName":studentName,"StudentNumber":StudentNumber,"Average":studentAverage})
topStudent = GetMaxAverage(studentsInfo)
print("Max Mark Is : "+topStudent["Average"]+ "From "+topStudent["StudentName"]+ " ("+topStudent["StudentNumber"]+")")
input("")    

    

    
