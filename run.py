from app import create_app, db, mail
from app.models import Course, Dining, Student, User
from app.helpers import get_courses
from app.scraping import upload_to_db_from_file  # get_students
import os

app = create_app()

with app.app_context():
    # get_students()
    get_courses()
    upload_to_db_from_file("./data/student_data.json")


@app.shell_context_processor
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                mail=mail,
                Student=Student,
                Course=Course,
                Dining=Dining,
                )


@app.cli.command()
def test():
    """Run unit tests from command line"""
    from unittest import TestLoader, TextTestRunner
    suite = TestLoader().discover('tests')
    TextTestRunner(verbosity=2, buffer=False).run(suite)


def clear():
    os.system('clear')
