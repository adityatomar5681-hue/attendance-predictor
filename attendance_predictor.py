import math

print("===================================")
print("       ATTENDANCE PREDICTOR")
print("===================================")

# Take input from the student
total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

# Validate input
if total_classes <= 0:
    print("Error: Total classes must be greater than zero.")

elif attended_classes < 0 or attended_classes > total_classes:
    print("Error: Invalid number of attended classes.")

elif required_percentage <= 0 or required_percentage > 100:
    print("Error: Required percentage must be between 0 and 100.")

else:
    # Calculate current attendance
    attendance = (attended_classes / total_classes) * 100

    print("\n========== YOUR RESULT ==========")
    print(f"Current attendance: {attendance:.2f}%")

    if attendance >= required_percentage:
        print("Status: You are meeting the attendance requirement!")

        # Calculate maximum classes that can be missed
        if required_percentage == 100:
            print("You cannot miss any more classes.")
        else:
            can_miss = math.floor(
                attended_classes / (required_percentage / 100)
                - total_classes + 1e-10
            )
            print(f"Maximum future classes you can miss: {max(0, can_miss)}")

    else:
        print("Status: Attendance is below the requirement.")

        # Calculate classes needed to reach the target
        if required_percentage == 100:
            print("You cannot reach 100% unless you attend every future class.")
            print("Even then, previously missed classes remain in the record.")
        else:
            needed = math.ceil(
                (required_percentage * total_classes / 100 - attended_classes)
                / (1 - required_percentage / 100)
            )
            print(f"Classes you must attend continuously: {needed}")

    # Predict attendance after the next class
    next_attendance = (
        (attended_classes + 1) / (total_classes + 1)
    ) * 100

    print(f"Attendance if you attend next class: {next_attendance:.2f}%")
    print("===================================")