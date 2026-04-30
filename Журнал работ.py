from flask import Flask, render_template
from sqlalchemy import select

from data.db_session import global_init, create_session
from models import Jobs

app = Flask(__name__)

@app.route('/')
def works():
    db_sess = create_session()
    query = select(Jobs)

    resp = [x.to_dict() for x in db_sess.execute(query).scalars()]

    return render_template('works.html', works=resp)

if __name__ == '__main__':
    global_init('db/works.db')
    app.run(port=8080)
