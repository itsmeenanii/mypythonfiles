#mini project student managament system

students=[]
def add_student():
    name=input("Name: ")
    age=int(input("Age: "))
    course=input("Course: ")
    roll=input("Roll: ")
    branch=input("Branch: ")
    #store as dictionary
    student={
        'Name':name,
        'Age':age,
        'Course':course,
        'Roll':roll,
        'Branch':branch
    }
    students.append(student)
    print("\nStudent Added Successfullyy.....\n")


def show_students():
    if not students:
        print("\nThere are no students !!!!\n")
        return
    for index,student in enumerate(students,1):
        print(f"\nStudent {index}")
        for key,value in student.items():
            print(f"{key}: {value}")


while True:
    print("==== Student Management System ===\n")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Exit")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        add_student()
    elif choice==2:
        show_students()
    elif choice==3:
        print("\n=== Ok Thank You ===\n")
        break
    else :
        print("Entered wrong value!!!!!")