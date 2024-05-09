class Garden:
    DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    PLANT_NAMES = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }
    
    def __init__(self, diagram, students=None):
        self.rows = diagram.split('\n')
        if students is None:
            students = self.DEFAULT_STUDENTS
        self.students = sorted(students)
    
    def plants(self, student):
        index = self.students.index(student) * 2
        student_plants = [
            self.rows[0][index],
            self.rows[0][index + 1],
            self.rows[1][index],
            self.rows[1][index + 1]
        ]
        return [self.PLANT_NAMES[plant] for plant in student_plants]
