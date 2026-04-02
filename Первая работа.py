import datetime

from flask import Flask
from data import db_session
from data.__all_models import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    work = Jobs()
    work.team_leader = 1
    work.job = 'deployment of residential modules 1 and 2'
    work.work_size = 15
    work.collaborators = '2, 3'
    work.start_date = datetime.datetime.now()
    work.is_finished = False

    session.add(work)
    session.commit()

if __name__ == '__main__':
    main()