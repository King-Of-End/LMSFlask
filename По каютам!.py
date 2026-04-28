from flask import Flask, render_template

app = Flask(__name__)

cosmo_list = ['Риддли Скотт', "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]

@app.route('/distribution')
def distribution():
    return render_template('distribution.html', cosmo_list=cosmo_list)

if __name__ == '__main__':
    app.run(port=8080)