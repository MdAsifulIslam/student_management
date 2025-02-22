# Student Management System

# List to store student data
students = []

# Function to add a student
def add_student(name, age, grades):
    student = {
        "name": name,
        "age": age,
        "grades": grades
    }
    students.append(student)

# Function to display all students
def display_students():
    if not students:
        print("No students available.")
        return
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

# Function to calculate the average grade of a student
def calculate_average_grade(student):
    return sum(student['grades']) / len(student['grades'])

# Function to save students' data to a file
def save_to_file(filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student['name']},{student['age']},{','.join(map(str, student['grades']))}\n")

# Main function to run the program
def main():
    while True:
        try:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Calculate Average Grade")
            print("4. Save Data to File")
            print("5. Exit")
            choice = input("Enter your choice: ")
 
            if choice == '1':
                 name = input("Enter student's name: ")
                 age = int(input("Enter student's age: "))
                 grades = list(map(int, input("Enter student's grades (separated by spaces): ").split()))
                 add_student(name, age, grades)
            elif choice == '2':
                 display_students()
            elif choice == '3':
                 name = input("Enter the student's name to calculate average grade: ")
                 for student in students:
                     if student['name'] == name:
                         avg_grade = calculate_average_grade(student)
                         print(f"{name}'s average grade is {avg_grade:.2f}")
                         break
                 else:
                     print(f"No student found with name {name}")
            elif choice == '4':
                 filename = input("Enter filename to save data: ")
                 save_to_file(filename)
                 print(f"Data saved to {filename}")
            elif choice == '5':
                 print("Exiting the program...")
                 break
            else:
                 print("Invalid choice. Please try again.")
        except ValueError as e:
             print(f"Error: {e}. Please enter valid input.")
 
 # Run the program
if __name__ == "__main__":
     main()
