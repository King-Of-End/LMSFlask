import json
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/member')
def member():
    dct = json.load(open('templates/members.json'))
    return render_template('member.html', **random.choice(list(dct.values())))

if __name__ == '__main__':
    app.run(port=8080)
