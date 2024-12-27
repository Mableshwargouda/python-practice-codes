studentName=input("enter your name : ")
studentUSN=input("enter USN : ")
marks=[]
totalmarks=0
avgmarks=0.0
for i in range(3):
    m=int(input("enter the marks of %s in subject %d :"%(studentName,i+1)))
    marks.append(m)
    totalmarks=totalmarks+m
    avgmarks=totalmarks/3
print("")
print("student name : ",studentName)
print("student USN : ",studentUSN)
print("total marks scored by %s is : %d"%(studentName,totalmarks))
print("avarage marks scored by %s is :%f"%(studentName,avgmarks))
print("")
