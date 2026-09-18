student_details = ("Alex Jones", 10, "Grade 5")

print("Student Name:", student_details[0])
print("Roll Number:", student_details[1])
print("Class:", student_details[2])

monday_subjects = {"Math", "Science", "English", "History"}
tuesday_subjects = {"Math", "Geography", "English", "Art"}

monday_subjects.add("Computer")
tuesday_subjects.remove("Art")

print("Updated Monday:", monday_subjects)
print("Updated Tuesday:", tuesday_subjects)

common_subjects = monday_subjects.intersection(tuesday_subjects)
print("Subjects on both days:", common_subjects)

all_subjects = monday_subjects.union(tuesday_subjects)
print("Total unique subjects:", all_subjects)
