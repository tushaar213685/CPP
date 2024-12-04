def read_csv(file_name):
    # Step 1: Read the CSV file and parse it into a dictionary
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    headers = lines[0].strip().split(',')
    student_data = []
    
    for line in lines[1:]:
        values = line.strip().split(',')
        student = {headers[i]: values[i] for i in range(len(headers))}
        student_data.append(student)
    
    return student_data

def display_all_students(student_data):
    # Step 2: Display all student records
    for student in student_data:
        print(student)

def find_student_by_id(student_data, student_id):
    # Step 3: Find a student by ID
    for student in student_data:
        if student['ID'] == student_id:
            return student
    return None

def calculate_average_grade(student_data):
    # Step 4: Calculate the average grade of all students
    total_grade = 0
    count = 0
    for student in student_data:
        total_grade += float(student['Grade'])
        count += 1
    return total_grade / count if count > 0 else 0

def add_student(student_data, new_student):
    # Step 5: Add a new student record
    student_data.append(new_student)

def save_csv(file_name, student_data):
    # Step 6: Save the updated data back to the CSV
    with open(file_name, 'w') as file:
        headers = ','.join(student_data[0].keys())
        file.write(headers + '\n')
        for student in student_data:
            row = ','.join(student.values())
            file.write(row + '\n')

# Example usage
file_name = 'student_records.csv'

# Load student records
students = read_csv(file_name)

# Display all students
print("All Students:")
display_all_students(students)

# Find a specific student
student_id = '1234'  # Example ID
print("\nStudent Found:", find_student_by_id(students, student_id))

# Calculate average grade
print("\nAverage Grade:", calculate_average_grade(students))

# Add a new student
new_student = {'ID': '5678', 'Name': 'John Doe', 'Grade': '85'}
add_student(students, new_student)

# Save updated records back to CSV
save_csv(file_name, students)

def print_first_10_rows(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # Print the header and first 10 rows
        print("First 10 rows (including header):")
        for i, line in enumerate(lines[:10]):
            print(line.strip())

# Example usage
file_name = 'student_records.csv'
print_first_10_rows(file_name)

