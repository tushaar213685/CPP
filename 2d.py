def check_minor_completion(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        
        # Extract column indices
        id_index = header.index("Student ID")
        course_type_index = header.index("Course Type")
        department_index = header.index("Department")
        credits_index = header.index("Credits")
        
        student_minors = {}
        
        # Process each row
        for line in lines[1:]:
            row = line.strip().split(',')
            student_id = row[id_index]
            course_type = row[course_type_index]
            department = row[department_index]
            credits = int(row[credits_index])
            
            # Check if the course is tagged as a "Minor"
            if course_type == "Minor":
                if student_id not in student_minors:
                    student_minors[student_id] = {}
                
                if department not in student_minors[student_id]:
                    student_minors[student_id][department] = 0
                
                student_minors[student_id][department] += credits
        
        # Check for students who completed a minor
        students_with_minors = []
        for student_id, departments in student_minors.items():
            for department, total_credits in departments.items():
                if total_credits >= 10:
                    students_with_minors.append((student_id, department))
        
        # Print roll numbers of students who completed a minor
        print("Students who completed a minor:")
        for student_id, department in students_with_minors:
            print(f"Student ID: {student_id}, Department: {department}")

# Example usage
file_name = 'student_records.csv'
check_minor_completion(file_name)
