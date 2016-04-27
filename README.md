This repository is the web application written in Python 3 using [Bottle](http://bottlepy.org/docs/dev/index.html) framework and SQLite database.

How to install:
- clone repository
- make [virtualenv](https://virtualenv.pypa.io/en/latest/) environment
```
$ virtualenv venv
$ source bin/activate 
```
- install requirements
```
pip install -r requirements.txt
```
- run
```
python app.py
```
- open web browser http://localhost:8080/

---
Below answers for some questions in [Test, Problem #2](https://docs.google.com/document/d/1g21iOerEXatdjdLZt8USag_1O6gSZcabjbv66rOCaLg/edit)

a) Database schema

![Database schema](images/diagram.png?raw=true "Database schema")

SQL queries for create table and insert some data in file [db.py](db.py)

b) SQL Query for get all semesters for student with id = 123-456-789
```sql
select s.id, s.date_begin, s.date_end, s.name
from semester s, student_scores sc
where sc.student_id = '123-456-789' and sc.semester_id = s.id 
group by s.id order by s.date_begin desc;
```
SQL Query for get scores for student with id = 123-456-789 in semester number 1
```sql
select c.name, c.description, sc.score
from courses c, semester s, students st, student_scores sc
where sc.course_id = c.id and sc.student_id = '123-456-789' and sc.semester_id = 1 
group by c.id
```

c) d) e) Html, css, javascript in file: `problem_2.html`