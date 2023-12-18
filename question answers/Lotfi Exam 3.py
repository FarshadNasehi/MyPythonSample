def CalculateWeightAverage(newScore,newMultiply,TotalAverage,TotalLessonUnit):
    studentWeightAverage = (((newScore*newMultiply)+(TotalAverage*TotalLessonUnit))/(newMultiply+TotalLessonUnit))
    return round(studentWeightAverage,2)


def GetMaxAverage(listOfDict):#بزرگترين معدل را حساب کرده و بر ميگرداند
    TopStudent={"StudentName":"","StudentNumber":"","WeightAverage":""}
    topAverage=0
    for x in listOfDict:
        if float(x["WeightAverage"])>float(topAverage):
            topAverage=x["WeightAverage"]
            TopStudent={"StudentName":x["StudentName"],"StudentNumber":x["StudentNumber"],"WeightAverage":x["WeightAverage"]}
        else:
            continue

    return TopStudent

def GetMinAverage(listOfDict):#کوچکترين معدل را حساب کرده و بر ميگرداند
    lastStudent={"StudentName":"","StudentNumber":"","WeightAverage":""}
    lastAverage=20
    for x in listOfDict:        
        if float(x["WeightAverage"])<float(lastAverage):
            lastAverage=x["WeightAverage"]
            lastStudent={"StudentName":x["StudentName"],"StudentNumber":x["StudentNumber"],"WeightAverage":x["WeightAverage"]}
        else:
            continue

    return lastStudent

studentCount= input("Enter Quantity of Students: ")
studentsInfo = []
for i in range(int(studentCount)):
    studentTotalAverage=0;
    studentTotalLessonUnit=0;
    studentName= input("Enter Student Name: "+str(i+1)+":")
    StudentNumber= input("Enter a Student Number: ")
    LessonCount= input("Enter Lesson Count: ")
    for j in range(int(LessonCount)):
        score= input("Enter Score for Lesson : "+str(j+1)+":")
        multiply= input("Enter multiply for Lesson : "+str(j+1)+":")
        studentTotalAverage = CalculateWeightAverage(float(score),float(multiply),float(studentTotalAverage),float(studentTotalLessonUnit))
        studentTotalLessonUnit=float(multiply)+float(studentTotalLessonUnit)
        
    studentsInfo.append({"StudentName":studentName,"StudentNumber":StudentNumber,"WeightAverage":studentTotalAverage})       
    print("Weight Average for student "+studentName+ " is : "+str(studentTotalAverage))
    print("-------------------")

topStudent = GetMaxAverage(studentsInfo)
print("-------------------")
print("Top Student Is : "+str(topStudent["WeightAverage"])+ " For "+topStudent["StudentName"]+ " ("+topStudent["StudentNumber"]+")")
print("-------------------")
if(len(studentsInfo)>1):
    lastStudent= GetMinAverage(studentsInfo)
    print("Last Student Is : "+str(lastStudent["WeightAverage"])+ " For "+lastStudent["StudentName"]+ " ("+lastStudent["StudentNumber"]+")")

