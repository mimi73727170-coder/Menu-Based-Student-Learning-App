class student :
    def __init__(self,name,course) :
        self.name = name
        self.course = course
        self.progress = 0

    def update_progress(self,progress) :
        self.progress = progress

    def show_details(self) :
        print("\n Name :",self.name)
        print("course :",self.course)
        print("progress :",self.progress)

students = []

while True :
    print("\n=====student Learning App=====")
    print("1.Add student")
    print("2.View students")
    print("3.Update Progress")
    print("4.Exit")

    choice = input("Enter choice :")
    
    if choice == "1" :
        name = input("Enter name :")
        course = input("Enter course :")

        student = student(name,course)
        students.append(student)
        print("student Added!")

    elif choice == "2" :
        for student in students :
            student.show_details()

    elif choice == "3" :
        name = input("Enter student name :")
        progress = int(input("Enter progress :"))

        for student in students :
            if student.name == name :
                student.update_progress(progress) 
                print("Progress Updated!")

    elif choice == "4" :
        break

    else :
        print("Invalid choice")

