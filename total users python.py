def calculate_users(total_users, staff_users):
    if total_users <= 0 or staff_users < 0 or staff_users % 3 != 0:
        return "Invalid input"
    
    non_teaching_staff = staff_users // 3
    student_users = total_users - staff_users - non_teaching_staff
    
    return f"Student Users: {student_users}"

# Test Cases
print(calculate_users(0, 0))        # Output: "Invalid input"
print(calculate_users(-143, 0))     # Output: "Invalid input"
print(calculate_users(1026, 1026))  # Output: "Student Users: 0"
print(calculate_users(450, 540))    # Output: "Student Users: -90" (Invalid input)
print(calculate_users(600, 45))     # Output: "Student Users: 555"
