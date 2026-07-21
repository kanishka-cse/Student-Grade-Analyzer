#Grade_Analyzer.py - STUDENT GRADE ANALYZER
#Author:Kanishka Dinakaran
#Date:July 2026


import csv

FILENAME = "students.csv"

# ---------- Calculate Grade ----------
def calculate_grade(average):

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 35:
        return "E"
    else:
        return "F"

# ---------- Load Students ----------
def load_students():
    students = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader) #skip header row
            for row in reader:
                if len(row) == 6:  # Ensure the row has all required fields
                    students.append(row)
    except FileNotFoundError:
        pass
    return students

# ---------- Add Student ----------
def add_student():
    print("\nADD STUDENT")
    n=int(input("Enter number of students to add :"))
    for i in range(n):
        name = input("Enter Student Name : ")
        python_marks = int(input("Python Marks : "))
        c_marks = int(input("C Programming Marks : "))
        maths_marks = int(input("Maths Marks : "))
        english_marks = int(input("English Marks : "))
        physics_marks = int(input("Physics Marks : "))
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                name,
                python_marks,
                c_marks,
                maths_marks,
                english_marks,
                physics_marks
            ])
    print("\nStudent Added Successfully!")

# ---------- Display Students ----------
def display_students():
    students = load_students()
    if len(students) == 0:
        print("\nNo Student Records Found.")
        return
    # Sort students by Total marks
    students.sort(key=lambda x: (int(x[1])+int(x[2])+int(x[3])+int(x[4])+int(x[5])), reverse=True)
    print("\n" + "="*60)
    print(f"{'Rank':<4} {'Name':<15} {'Total':<8} {'Average':<8} {'Grade':<5} {'Status'}")
    print("="*60)
    for i, student in enumerate(students):
        python_marks=int(student[1])
        c_marks=int(student[2])
        maths_marks=int(student[3])
        english_marks=int(student[4])
        physics_marks=int(student[5])
        total = python_marks + c_marks + maths_marks + english_marks + physics_marks
        average = total / 5
        grade = calculate_grade(average)
        if(int(student[1])>=35 and int(student[2])>=35 and int(student[3])>=35 and int(student[4])>=35 and int(student[5])>=35):
            status = "PASS"
        else:
            status = "FAIL"
        if i == 0:
            rank = "🥇"
        elif i == 1:
            rank = "🥈"
        elif i == 2:
            rank = "🥉"
        else:
            rank = str(i + 1)
        print(f"{rank:<4} {student[0]:<15} {total:<8} {average:<8} {grade:<5} {status}")
       
 # ---------- Menu ----------
def menu():
    while True:
        print("\n===== STUDENT GRADE ANALYZER =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("\nThank You!")
            break
        else:
            print("Invalid Choice! Please try again.")

# ---------- Main ----------
def main():
    menu()


if __name__ == "__main__":
    main()