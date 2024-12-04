def grade_to_points(grade):
    # Convert letter grades to numerical points
    grade_points = {'AP': 10, 'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7, 'CC': 6}
    return grade_points.get(grade, 0)  # Return 0 if the grade is not valid

def calculate_cpi(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        
        # Extract column indices for required fields
        id_index = header.index("Student ID")
        course_type_index = header.index("Course Type")
        credits_index = header.index("Credits")
        grade_index = header.index("Grade")
        
        student_data = {}
        
        # Process each row
        for line in lines[1:]:
            row = line.strip().split(',')
            student_id = row[id_index]
            course_type = row[course_type_index]
            credits = int(row[credits_index])
            grade = row[grade_index]
            
            grade_points = grade_to_points(grade)
            
            if student_id not in student_data:
                student_data[student_id] = {'total_credits': 0, 'weighted_sum': 0}
            
            # Update total credits and weighted sum for CPI calculation
            student_data[student_id]['total_credits'] += credits
            student_data[student_id]['weighted_sum'] += credits * grade_points
        
        # Calculate CPI for each student
        for student_id, data in student_data.items():
            total_credits = data['total_credits']
            weighted_sum = data['weighted_sum']
            cpi = weighted_sum / total_credits if total_credits > 0 else 0
            print(f"Student ID: {student_id}, Total Credits: {total_credits}, CPI: {cpi:.2f}")

# Example usage
file_name = 'student_records.csv'
calculate_cpi(file_name)
