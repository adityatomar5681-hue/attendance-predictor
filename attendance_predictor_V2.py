import csv
import os
import math

FILE_NAME = "attendance_records.csv"


def calculate_attendance():
    print("\n--- CHECK ATTENDANCE ---")

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        total = int(input("Enter total classes conducted: "))
        attended = int(input("Enter classes attended: "))
        target = float(input("Enter required attendance percentage: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    # Validate details
    if total <= 0 or attended < 0 or attended > total:
        print("Invalid class details.")
        return

    if target <= 0 or target > 100:
        print("Invalid attendance target.")
        return

    # Calculate attendance
    percentage = (attended / total) * 100

    print("\n========== ATTENDANCE REPORT ==========")
    print("Student:", name)
    print("Total classes:", total)
    print("Classes attended:", attended)
    print(f"Current attendance: {percentage:.2f}%")

    if percentage >= target:
        print("Status: Attendance requirement met!")

        if target == 100:
            print("Maximum classes you can miss: 0")
        else:
            max_miss = math.floor(attended / (target / 100) - total + 1e-10)
            print("Maximum future classes you can miss:", max(0, max_miss))

    else:
        print("Status: Attendance is below target.")

        if target == 100:
            print("Reaching 100% is impossible because classes were missed.")
        else:
            needed = math.ceil(
                (target * total / 100 - attended) / (1 - target / 100)
            )
            print("Classes to attend continuously:", needed)

    # Predict next class
    next_percentage = ((attended + 1) / (total + 1)) * 100

    print(f"Attendance after attending next class: {next_percentage:.2f}%")

    # Save record
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow([
                "Name", "Total Classes", "Attended Classes",
                "Attendance Percentage", "Required Percentage"
            ])

        writer.writerow([name, total, attended, round(percentage, 2), target])

    print("\nStudent record saved successfully!")


def view_records():
    print("\n--- SAVED STUDENT RECORDS ---")

    if not os.path.exists(FILE_NAME):
        print("No records found. Add a student first.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))


def main():
    while True:
        print("\n================================")
        print("   STUDENT ATTENDANCE SYSTEM")
        print("================================")
        print("1. Check and save attendance")
        print("2. View saved student records")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculate_attendance()

        elif choice == "2":
            view_records()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1, 2 or 3.")


# Start the program
if __name__ == "__main__":
    main()