class School:
    def __init__(self):
        # This dictionary will store grades as keys and a set of student names as values
        self.grades = {}

    def add_student(self, name, grade):
        """Adds a student to a specific grade. If the student is already in that grade, indicates an error."""
        if grade not in self.grades:
            self.grades[grade] = set()
        if name in self.grades[grade]:
            return "This student is already added to this grade."
        self.grades[grade].add(name)
        return "OK."

    def grade(self, grade_number):
        """Returns a sorted list of all students in a specified grade."""
        if grade_number in self.grades:
            return sorted(self.grades[grade_number])
        return []  # Return an empty list if there are no students in the grade

    def roster(self):
        """Returns a sorted list of all students in all grades, sorted first by grade, then by name."""
        all_students = []
        for grade in sorted(self.grades.keys()):
            students_in_grade = sorted(self.grades[grade])
            all_students.extend(students_in_grade)
        return all_students

    def added(self):
        """Prints a summary of students added in each grade, sorted."""
        result = []
        for grade in sorted(self.grades):
            students = sorted(self.grades[grade])
            if students:
                result.append(bool(True))
        return result if result else "No students are enrolled."
