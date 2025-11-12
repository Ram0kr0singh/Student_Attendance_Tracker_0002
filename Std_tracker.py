from datetime import datetime


def collect_attendance():
    """Collect student attendance records with validation."""
    attendance_records = {}

    print("\nWelcome to the Attendance Tracker System!")
    print("Record attendance with student names and check-in times.\n")

    try:
        total_entries = int(input("How many attendance entries would you like to record? "))
    except ValueError:
        print("Invalid number. Please restart and enter a valid integer.")
        return {}

    for entry in range(1, total_entries + 1):
        print(f"\nEntry {entry}:")

        while True:
            name = input("Student Name: ").strip()
            if name == "":
                print("Name cannot be empty. Please re-enter.")
            elif name in attendance_records:
                print("This student is already recorded. Enter a different name.")
            else:
                break

        while True:
            time = input("Check-in Time (e.g., 09:10 AM): ").strip()
            if time == "":
                print("Check-in time cannot be empty. Please re-enter.")
            else:
                break

        attendance_records[name] = time

    return attendance_records


def display_summary(attendance):
    """Display formatted attendance summary table."""
    print("\n\n========== Attendance Summary ==========")
    print(f"{'Student Name':<25} {'Check-in Time':<15}")
    print("-" * 40)

    for name, time in attendance.items():
        print(f"{name:<25} {time:<15}")

    print("-" * 40)
    print(f"Total Students Present: {len(attendance)}")


def calculate_absentees(present_count):
    """Optional absentee calculation."""
    choice = input("\nDo you want to calculate absentees? (yes/no): ").lower()

    if choice == "yes":
        total_students = int(input("Enter total number of students in class: "))
        absentees = total_students - present_count

        print(f"\nTotal Present: {present_count}")
        print(f"Total Absent: {absentees}")

        return absentees

    return None


def save_to_file(attendance, absentees=None):
    """Optional saving to a text file."""
    choice = input("\nDo you want to save this attendance record? (yes/no): ").lower()

    if choice == "yes":
        timestamp = datetime.now().strftime("%d-%m-%Y  %I:%M %p")
        with open("attendance_log.txt", "w") as file:
            file.write("Attendance Report\n")
            file.write("-" * 40 + "\n")
            for student, time in attendance.items():
                file.write(f"{student:<25} {time:<15}\n")
            file.write("-" * 40 + "\n")
            file.write(f"Total Present: {len(attendance)}\n")
            if absentees is not None:
                file.write(f"Total Absent: {absentees}\n")
            file.write(f"Report Generated On: {timestamp}\n")

        print("\nAttendance report saved to attendance_log.txt")


# ------------------- MAIN PROGRAM FLOW -------------------
attendance_data = collect_attendance()

if attendance_data:
    display_summary(attendance_data)
    abs_value = calculate_absentees(len(attendance_data))
    save_to_file(attendance_data, abs_value)

print("\nThank you for using the Attendance Tracker!")
