from models.student import Student
from models.semester import Semester
from models.course import Course

class StudentDAO:
    def __init__(self, db):
        self.db = db

    def getAllStudents(self):
        cur = self.db.connection.cursor()
        cur.execute("SELECT id, name, major FROM students")
        students = []
        result = cur.fetchone()
        while result:
            student = Student(result[0], result[1], result[2])
            students.append(student)
            result = cur.fetchone()
        return students

    def loadScoresForStudent(self, student_id):
        student = self.loadStudentWithId(student_id)
        if student:
            student.semesters = self.loadSemestersForStudent(student)
            for semester in student.semesters:
                semester.courses = self.loadCoursesForStudentAndSemester(student, semester)
            return student
        return None

    def loadStudentWithId(self, student_id):
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        result = cur.fetchone()
        if result:
            student = Student(result[0], result[1], result[2])
            return student

        return None

    def loadSemestersForStudent(self, student):
        cur = self.db.connection.cursor()
        cur.execute("""select s.id, s.date_begin, s.date_end, s.name
                       from semester s, student_scores sc
                       where sc.student_id = ? and sc.semester_id = s.id group by s.id order by s.date_begin desc;""",
                    (student.id,))
        semesters = []
        result = cur.fetchone()
        while result:
            semester = Semester(result[0], result[1], result[2], result[3])
            semesters.append(semester)
            result = cur.fetchone()
        return semesters

    def loadCoursesForStudentAndSemester(self, student, semester):
        cur = self.db.connection.cursor()
        cur.execute("""select c.name, c.description, sc.score
                       from courses c, semester s, students st, student_scores sc
                       where sc.course_id = c.id and sc.student_id = ? and sc.semester_id = ? group by c.id;""",
                    (student.id, semester.id,))
        courses = []
        result = cur.fetchone()
        while result:
            course = Course(result[0], result[1], result[2])
            courses.append(course)
            result = cur.fetchone()
        return courses