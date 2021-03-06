#!/usr/bin/env python

from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_content():
    users = User.query.all()
    return dict(app=app, db=db, User=User, Role=Role, users=users)


manager.add_command('shell', Shell(make_context=make_shell_content))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def test_ot():
    pass


if __name__ == '__main__':
    manager.run()
