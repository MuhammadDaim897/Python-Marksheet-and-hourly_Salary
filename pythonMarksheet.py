# Marksheet

name=input("Enter the Student name: ")

RollNo=int(input("Enter Student Roll Number"))

total_marks=500

Ew=float(input("Enter EW Marks: "))

dld=float(input("Enter dld Marks: "))

Oop=float(input("Enter Oop Marks: "))

Iot=float(input("Enter Iot Marks: "))

MulimulQuran=float(input("Enter Fah-e-Quran Marks: "))

Obtained_marks= Ew + dld + Oop + Iot + MulimulQuran

per=(Obtained_marks/total_marks) * 100

Subject_Failed = Ew < 40 or dld < 40 or Oop < 40 or Iot < 40 or MulimulQuran < 40

if Subject_Failed:
    result = "FAIL"
    grade = "F"

else:
    result="pass"
    if per>=80:
        grade="A+"

    elif per>=70:
        grade="A"

    elif per>=60:
        grade="B"

    elif per>=50:
        grade="C"

    elif per>=40:
        grade="D"

    else:
        grade="F"

    print("\n<<<---Marksheet--->>>")

    print("Student name is: ",name)
    print("Student Roll No: ",RollNo)
    print("English Marks: ",Ew)
    print("dld Marks: ",dld)
    print("Oop Marks",Oop)
    print("Iot Marks",Iot)
    print("MulimulQuran Marks",MulimulQuran)
    print("Total Marks: ",total_marks)
    print("Obtained Marks: ",Obtained_marks)
    print("Percentage: ",per)
    print("Grade: ",grade)
    print("Result: ",result)