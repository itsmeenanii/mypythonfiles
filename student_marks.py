#program for analysing student marks
n=int(input("Enter number of students:"))
marks=[]
for i in range(n):
    mark=float(input(f"Enter marks for student {i+1}:"))
    marks.append(mark)
average=sum(marks)/n
highest=maximum(marks)
lowest=min(marks)
print(f"Average marks: {average}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
above_average=[mark for mark in marks if mark>average]
print(f"Marks of students above average: {above_average}")





