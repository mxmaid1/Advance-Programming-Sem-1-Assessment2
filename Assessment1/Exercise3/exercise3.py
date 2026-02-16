import tkinter as tk
from tkinter import ttk, messagebox

studentMarksFile = "Marks.txt"
students = []  
studentNames = []

try:

    file = open(studentMarksFile, "r")
    lines = file.readlines()
    file.close()

    for i in range(1, len(lines)):
        line = lines[i].strip()  
        if line == "":
            continue
        parts = line.split(",")  

        if len(parts) == 6:
            idnumber = parts[0].strip()
            name = parts[1].strip()
           
            coursework1 = int(parts[2])
            coursework2 = int(parts[3])
            coursework3 = int(parts[4])
            examscore = int(parts[5])


            studentinfo = {
                "id": idnumber,
                "name": name,
                "coursework": [coursework1, coursework2, coursework3],
                "exam": examscore
            }
            students.append(studentinfo)
except Exception as error:
    messagebox.showerror("Error", "Theres something wrong with the file:"+ str(error) )

for student in students:
    studentNames.append(student["name"])

def Results(student):
    coursework_total = sum(student["coursework"])
    total_mark = 160
    overall = coursework_total + student["exam"]
    percent = (overall / total_mark) * 100

    grade_boundaries = [(70, "A"),(60, "B"),(50, "C"),(40, "D"),(0, "F")]

    for threshold, grade in grade_boundaries:
        if percent >= threshold:
            return coursework_total, student["exam"], percent, grade


def DisplayRecords():
    OutputFrame.delete("1.0", tk.END)
    total_percent = 0
    for student in students:
        coursework, exam, percent, grade = Results(student)
        total_percent += percent
        record = (
            f"Name: {student['name']}\n"
            f"Number: {student['id']}\n"
            f"Coursework Total: {coursework}\n"
            f"Exam Mark: {exam}\n"
            f"Overall Percentage: {percent:.2f}%\n"
            f"Grade: {grade}\n\n"
        )
        OutputFrame.insert(tk.END, record)

    avg = total_percent / len(students) if students else 0
    OutputFrame.insert(tk.END, f"Total Students: {len(students)}\nAverage Percentage: {avg:.2f}%")


def DisplayStudentRecord():
    selected_name = StudentsNamedropdown.get()
    if not selected_name:
        messagebox.showwarning("Warning", "Please select a student.")
        return

    for student in students:
        if student["name"] == selected_name:
            cw, exam, percent, grade = Results(student)
            OutputFrame.delete("1.0", tk.END)
            record = (
                f"Name: {student['name']}\n"
                f"Number: {student['id']}\n"
                f"Coursework Total: {cw}\n"
                f"Exam Mark: {exam}\n"
                f"Overall Percentage: {percent:.2f}%\n"
                f"Grade: {grade}\n"
            )
            OutputFrame.insert(tk.END, record)
            return

def total_marks(student):
    return sum(student["coursework"]) + student["exam"]

def show_highest_or_lowest(highest=True):
    if not students:
        return

    if highest:
        student = max(students, key=total_marks)
    else:
        student = min(students, key=total_marks)


    cw, exam, percent, grade = Results(student)

    OutputFrame.delete("1.0", tk.END)

    title = "Highest Scoring Student" if highest else "Lowest Scoring Student"
    OutputFrame.insert(tk.END, f"{title}\n\n")


    OutputFrame.insert(
        tk.END,
        f"Name: {student['name']}\n"
        f"Number: {student['id']}\n"
        f"Coursework Total: {cw}\n"
        f"Exam Mark: {exam}\n"
        f"Overall Percentage: {percent:.2f}%\n"
        f"Grade: {grade}\n"
    )


def show_highest():
    show_highest_or_lowest(True)

def show_lowest():
    show_highest_or_lowest(False)


backgroundColor="#d1d1d1"
root = tk.Tk()
root.title("Student Manager")
root.geometry("676x767")
root.config(bg=backgroundColor)


title_label = tk.Label(root, text="Student Manager", bg=backgroundColor)
title_label.pack(pady=10)


ButtonsFrame = tk.Frame(root, bg=backgroundColor)
ButtonsFrame.pack(pady=10)

ViewAllButton = tk.Button(ButtonsFrame, text="View All Student Records", width=20, command=DisplayRecords)
ViewAllButton.grid(row=0, column=0, padx=5)

HighestScoreButton = tk.Button(ButtonsFrame, text="Show Highest Score", width=20, command=show_highest)
HighestScoreButton.grid(row=0, column=1, padx=5)

LowestScoreButton = tk.Button(ButtonsFrame, text="Show Lowest Score", width=20, command=show_lowest)
LowestScoreButton.grid(row=0, column=2, padx=5)


IndividualStudentFrame = tk.Frame(root, bg=backgroundColor)
IndividualStudentFrame.pack(pady=10)

label1 = tk.Label(IndividualStudentFrame, text="View Individual Student Record:", bg=backgroundColor)
label1.grid(row=0, column=0, padx=5)

StudentsNamedropdown = ttk.Combobox(IndividualStudentFrame, values=studentNames, width=25)
StudentsNamedropdown.grid(row=0, column=1, padx=5)

buttonview = tk.Button(IndividualStudentFrame, text="View Record", width=12, command=DisplayStudentRecord)
buttonview.grid(row=0, column=2, padx=5)

OutputFrame = tk.Text(root, height=35, width=70, wrap=tk.WORD)
OutputFrame.pack(pady=10)

root.mainloop()
