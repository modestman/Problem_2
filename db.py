import sqlite3

class DB:

    def __init__(self, app):
        self.app = app
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.app.config['db_path'], detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    def create_all(self):
        self.create_tables()
        self.insert_test_data()

    def create_tables(self):
        cur = self.connection.cursor()
        cur.execute("CREATE TABLE students (id TEXT PRIMARY KEY NOT NULL, name TEXT NOT NULL, major TEXT);")
        cur.execute("CREATE TABLE semester (id INTEGER PRIMARY KEY AUTOINCREMENT, date_begin DATE NOT NULL, date_end DATE NOT NULL, name TEXT NOT NULL);")
        cur.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT);")
        cur.execute("""CREATE TABLE student_scores (student_id TEXT REFERENCES students (id),
                                                    semester_id INTEGER REFERENCES semester (id),
                                                    course_id INTEGER REFERENCES courses (id),
                                                    score TEXT);""")
        self.connection.commit()

    def insert_test_data(self):
        cur = self.connection.cursor()
        cur.executescript("""INSERT INTO students (id, Name, Major) VALUES ('123-456-789', 'John Doe', 'Computer Science');
                            INSERT INTO semester (id, date_begin, date_end, name) VALUES (1, '2012-03-01', '2012-05-31', 'Spring 2012');
                            INSERT INTO semester (id, date_begin, date_end, name) VALUES (2, '2012-09-01', '2012-11-30', 'Fall 2012');
                            INSERT INTO semester (id, date_begin, date_end, name) VALUES (3, '2012-12-01', '2013-02-28', 'Winter 2013');
                            INSERT INTO courses (id, name, description) VALUES (1, 'Math 1A', NULL);
                            INSERT INTO courses (id, name, description) VALUES (2, 'Math 1B', NULL);
                            INSERT INTO courses (id, name, description) VALUES (3, 'Math 1C', NULL);
                            INSERT INTO courses (id, name, description) VALUES (4, 'Comp Sci 111', NULL);
                            INSERT INTO courses (id, name, description) VALUES (5, 'Comp Sci 100', NULL);
                            INSERT INTO courses (id, name, description) VALUES (6, 'Comp Sci 2', NULL);
                            INSERT INTO courses (id, name, description) VALUES (7, 'Comp Sci 1', NULL);
                            INSERT INTO courses (id, name, description) VALUES (8, 'English 1', NULL);
                            INSERT INTO courses (id, name, description) VALUES (9, 'History 10', NULL);
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 1, 1, 'A-');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 3, 4, 'A-');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 3, 5, 'A');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 3, 3, 'B+');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 2, 6, 'A-');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 2, 8, 'A');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 2, 2, 'B');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 1, 7, 'A');
                            INSERT INTO student_scores (student_id, semester_id, course_id, score) VALUES ('123-456-789', 1, 9, 'B+');""")
        self.connection.commit()

