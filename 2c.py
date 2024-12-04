def check_graduation_requirements(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        
        # Extract column indices
        id_index = header.index("Student ID")
        course_type_index = header.index("Course Type")
        credits_index = header.index("Credits")
        
        student_credits = {}
        
        # Process each row
        for line in lines[1:]:
            row = line.strip().split(',')
            student_id = row[id_index]
            course_type = row[course_type_index]
            credits = int(row[credits_index])
            
            if student_id not in student_credits:
                student_credits[student_id] = {'Core': 0, 'Department Elective': 0, 'Flexible Elective': 0, 'HASMED': 0}
            
            # Update the credits for the appropriate course type
            if course_type == "Core":
                student_credits[student_id]['Core'] += credits
            elif course_type == "Department Elective":
                student_credits[student_id]['Department Elective'] += credits
            elif course_type == "Flexible Elective":
                student_credits[student_id]['Flexible Elective'] += credits
            elif course_type == "HASMED":
                student_credits[student_id]['HASMED'] += credits
        
        # Check graduation requirements
        graduating_students = []
        for student_id, credits in student_credits.items():
            if (
                credits['Core'] >= 20 and
                credits['Department Elective'] >= 15 and
                credits['Flexible Elective'] >= 10 and
                credits['HASMED'] >= 5
            ):
                graduating_students.append(student_id)
        
        # Print roll numbers of students meeting the requirements
        print("Students meeting graduation requirements:")
        for student_id in graduating_students:
            print(student_id)

# Example usage
file_name = 'student_records.csv'
check_graduation_requirements(file_name)
