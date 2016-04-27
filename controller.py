from bottle import template, static_file
from dao import StudentDAO

class Controller:
    def __init__(self, app):
        self.app = app
        db = self.app.config['db']
        self.dao = StudentDAO(db)
        self.app.route("/", callback=self.index)
        self.app.route("/student/<userid>", callback=self.student)
        self.app.route("/static/<filepath:path>", callback=self.server_static)

    def index(self):
        students = self.dao.getAllStudents()
        return template('index_template', dict(students=students))

    def student(self, userid):
        studentWithScores = self.dao.loadScoresForStudent(userid)
        return template('student_template', dict(student=studentWithScores))

    def server_static(self, filepath):
        return static_file(filepath, root=self.app.config['static'])
