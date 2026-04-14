from flask import Flask, render_template

app = Flask(__name__)

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return render_template(
        'result.html',
        nickname=nickname,
        level=level,
        rating=rating
    )

if __name__ == '__main__':
    app.run(port=8080)