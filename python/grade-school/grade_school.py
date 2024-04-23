class School:
    def __init__(self):
        self.grades = {}
        self.student_registry = {}
        self.addition_tracker = []

    def add_student(self, name, grade):
        """Adds a student to a specific grade, preventing enrollment in multiple grades."""
        if name in self.student_registry and self.student_registry[name] != grade:
            self.addition_tracker.append(False)
            return "This student is already enrolled in a different grade."
        if grade not in self.grades:
            self.grades[grade] = set()
        if name in self.grades[grade]:
            self.addition_tracker.append(False)
            return "This student is already added to this grade."
        self.grades[grade].add(name)
        self.student_registry[name] = grade
        self.addition_tracker.append(True)
        return "OK."

    def grade(self, grade_number):
        """Returns a sorted list of all students in a specified grade."""
        return sorted(self.grades.get(grade_number, []))

    def roster(self):
        """Returns a list of all students in all grades, sorted by grade and then by name."""
        all_students = []
        for grade in sorted(self.grades.keys()):
            students_in_grade = sorted(self.grades[grade])
            all_students.extend(students_in_grade)
        return all_students

    def added(self):
        """Returns a list of booleans indicating whether each student was successfully added."""
        return self.addition_tracker
