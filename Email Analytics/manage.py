import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint


from app.main import create_app, db
from flask_cors import CORS

app = create_app('dev')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)


manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(port=81)


if __name__ == '__main__':
    manager.run()
