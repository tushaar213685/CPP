def check_honours_completion(file_name):
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
                student_credits[student_id] = {'Honours': 0, 'Core': 0}
            
            # Accumulate credits for relevant course types
            if course_type == "Honours":
                student_credits[student_id]['Honours'] += credits
            elif course_type == "Core":
                student_credits[student_id]['Core'] += credits
        
        # Check for students who completed honours
        students_with_honours = []
        for student_id, credits in student_credits.items():
            if credits['Honours'] >= 10 and credits['Core'] >= 20:
                students_with_honours.append(student_id)
        
        # Print roll numbers of students who completed honours
        print("Students who completed honours:")
        for student_id in students_with_honours:
            print(student_id)

# Example usage
file_name = 'student_records.csv'
check_honours_completion(file_name)
