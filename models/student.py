class Student:
    id = None
    name = None
    major = None
    semesters = []

    def __init__(self, _id, name, major):
        self.id = _id
        self.name = name
        self.major = major

    def addSemester(self, semester):
        self.semesters.append(semester)



