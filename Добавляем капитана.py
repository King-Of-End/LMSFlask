from flask import Flask
from data import db_session
from data.__all_models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    captain = User()
    captain.surname = 'Scott'
    captain.name = 'Ridley'
    captain.age= 21
    captain.position = 'captain'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'

    dohodyaga1 = User()
    dohodyaga1.surname = 'Wind'
    dohodyaga1.name = 'Ding'
    dohodyaga1.age= 666
    dohodyaga1.position = 'dohodyaga'
    dohodyaga1.address = 'underground/dark_world'
    dohodyaga1.email = 'gaster1@lab.ut'

    dohodyaga2 = User()
    dohodyaga2.surname = 'Wind'
    dohodyaga2.name = 'Ding'
    dohodyaga2.age= 666
    dohodyaga2.position = 'dohodyaga'
    dohodyaga2.address = 'underground/dark_world'
    dohodyaga2.email = 'gaster2@lab.ut'

    dohodyaga3 = User()
    dohodyaga3.surname = 'Wind'
    dohodyaga3.name = 'Ding'
    dohodyaga3.age= 666
    dohodyaga3.position = 'dohodyaga'
    dohodyaga3.address = 'underground/dark_world'
    dohodyaga3.email = 'gaster3@lab.ut'

    session.add(captain)
    session.add(dohodyaga1)
    session.add(dohodyaga2)
    session.add(dohodyaga3)
    session.commit()

if __name__ == '__main__':
    main()