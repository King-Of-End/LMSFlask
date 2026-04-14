from flask import Flask, render_template

app = Flask(__name__)

@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choice.html', planet=planet_name)

if __name__ == '__main__':
    app.run(port=8080)