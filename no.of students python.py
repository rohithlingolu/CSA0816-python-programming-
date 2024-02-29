def calculate_users(total_users, staff_users):
    if total_users < 0 or staff_users < 0:
        print("Invalid input. Total users and staff users must be non-negative.")
        return

    student_users = total_users - staff_users
    non_teaching_staff_users = staff_users // 3
    total_staff_users = staff_users + non_teaching_staff_users

    print(f"Student Users: {student_users}")
    print(f"Non-Teaching Staff Users: {non_teaching_staff_users}")
    print(f"Total Staff Users: {total_staff_users}")

calculate_users(0, 0)
calculate_users(-143, 0)
calculate_users(1026, 1026)
calculate_users(450, 540)
calculate_users(600, 450)
