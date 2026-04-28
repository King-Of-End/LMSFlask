from flask import Flask, render_template

app = Flask(__name__)

@app.route('/table/<gender>/<int:age>')
def table(gender: str, age: int):
    match gender:
        case 'female':
            color = '#FF6000' if age >= 21 else '#FFAA55'
        case 'male':
            color = '#0033CC' if age >= 21 else '#C4D4E0'
    return render_template('table.html', color=color, age=age)

if __name__ == '__main__':
    app.run(port=8080)
