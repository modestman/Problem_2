class Semester:
    id = None
    dateBegin = None
    dateEnd = None
    name = None
    courses = []

    def __init__(self, _id, dateBegin, dateEnd, name):
        self.id = _id
        self.dateBegin = dateBegin
        self.dateEnd = dateEnd
        self.name = name

    def addCourse(self, course):
        self.courses.append(course)
