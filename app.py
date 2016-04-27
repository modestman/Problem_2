import bottle
import os

app = bottle.default_app()
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))
app.config['db_path'] = os.path.join(app.config['basedir'], 'db\\university.sqlite')
app.config['static'] = os.path.join(app.config['basedir'], 'static')

from db import DB
db = DB(app)
if not os.path.exists(app.config['db_path']):
    print("Created new database: " + app.config['db_path'])
    db.connect()
    db.create_all()
else:
    db.connect()

app.config['db'] = db

from controller import Controller
mainController = Controller(app)

app.run(host='localhost', port=8080, debug=True)
