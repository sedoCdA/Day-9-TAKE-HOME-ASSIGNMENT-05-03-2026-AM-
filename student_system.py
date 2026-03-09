# student_system.py
# Day 9 AM - Student Management System

# ─────────────────────────────────────────
# Initial student records (list of lists)
# ─────────────────────────────────────────
records = [
    ["Aman",    "Math",      88],
    ["Priya",   "Physics",   91],
    ["Rahul",   "Math",      76],
    ["Sneha",   "Chemistry", 85],
    ["Arjun",   "Physics",   67],
    ["Divya",   "Math",      92],
    ["Karan",   "Chemistry", 78],
    ["Meera",   "Physics",   88],
    ["Rohan",   "Chemistry", 95],
    ["Ananya",  "Math",      73],
]

# ─────────────────────────────────────────
# 1. add_student
# ─────────────────────────────────────────
def add_student(name, subject, marks):
    """Adds a student using append. Prevents duplicate name+subject."""
    for r in records:
        if r[0] == name and r[1] == subject:
            print(f"'{name}' in '{subject}' already exists.")
            return
    records.append([name, subject, marks])
    print(f"Added: {name} | {subject} | {marks}")

# ─────────────────────────────────────────
# 2. get_toppers
# ─────────────────────────────────────────
def get_toppers(subject):
    """Returns top 3 students in a subject sorted by marks."""
    subject_records = [r for r in records if r[1] == subject]
    if not subject_records:
        print(f"No records found for subject: {subject}")
        return []
    top3 = sorted(subject_records, key=lambda x: x[2], reverse=True)[:3]
    return top3

# ─────────────────────────────────────────
# 3. class_average
# ─────────────────────────────────────────
def class_average(subject):
    """Returns average marks for a subject using list comprehension."""
    marks = [m[2] for m in records if m[1] == subject]
    if not marks:
        print(f"No records found for subject: {subject}")
        return 0
    return sum(marks) / len(marks)

# ─────────────────────────────────────────
# 4. above_average_students
# ─────────────────────────────────────────
def above_average_students():
    """Returns students scoring above the overall class average."""
    if not records:
        return None
    overall_avg = sum(r[2] for r in records) / len(records)
    above = [r for r in records if r[2] > overall_avg]
    return overall_avg, above

# ─────────────────────────────────────────
# 5. remove_student
# ─────────────────────────────────────────
def remove_student(name):
    """
    Removes all records of a student.
    Does NOT use remove() inside a loop — uses list comprehension.
    """
    global records
    before = len(records)
    records = [r for r in records if r[0] != name]
    removed = before - len(records)
    if removed:
        print(f"Removed {removed} record(s) for '{name}'.")
    else:
        print(f"No records found for '{name}'.")

# ─────────────────────────────────────────
# 6. save_to_file
# ─────────────────────────────────────────
def save_to_file():
    """Saves all records to students.txt on exit."""
    with open("students.txt", "w") as f:
        f.write("Name,Subject,Marks\n")
        for r in records:
            f.write(f"{r[0]},{r[1]},{r[2]}\n")
    print(" Records saved to students.txt")

# ─────────────────────────────────────────
# CLI Menu
# ─────────────────────────────────────────
def menu():
    while True:
        print("\n" + "="*40)
        print("Student Management System")
        print("="*40)
        print("  1. Add Student")
        print("  2. Show Toppers (by subject)")
        print("  3. Show Class Average (by subject)")
        print("  4. Show Above-Average Students")
        print("  5. Remove Student")
        print("  6. Exit")
        print("="*40)

        choice = input("  Enter choice (1-6): ").strip()

        if choice == "1":
            name    = input("  Name: ").strip()
            subject = input("  Subject: ").strip()
            marks   = int(input("  Marks: ").strip())
            add_student(name, subject, marks)

        elif choice == "2":
            subject = input("  Subject: ").strip()
            toppers = get_toppers(subject)
            if toppers:
                print(f"\n Top 3 in {subject}:")
                for i, r in enumerate(toppers, 1):
                    print(f"    {i}. {r[0]} — {r[2]}")

        elif choice == "3":
            subject = input("  Subject: ").strip()
            avg = class_average(subject)
            print(f"\n Average marks in {subject}: {avg:.2f}")

        elif choice == "4":
            result = above_average_students()
            if result:
                avg, students = result
                print(f"\n Overall Average: {avg:.2f}")
                print("  Students above average:")
                for r in students:
                    print(f"    → {r[0]} | {r[1]} | {r[2]}")

        elif choice == "5":
            name = input("  Student name to remove: ").strip()
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("Goodbye!")
            break

        else:
            print("
            Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
