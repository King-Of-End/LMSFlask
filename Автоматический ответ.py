from flask import Flask, request, render_template, redirect

user_answer = {}
auto_answerr = {
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'true',
}

app = Flask(__name__)
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form.html') # вставить название файла с новой формой из задачи

    elif request.method == 'POST':
        global user_answer
        user_answer['surname'] = request.form['surname']
        user_answer['name'] = request.form['name']
        user_answer['email'] = request.form['email']
        user_answer['education'] = request.form['class']
        for i in request.form.keys():
            if request.form[i] == 'on' and i != 'accept':
                user_answer['profession'] = i
        user_answer['sex'] = request.form['sex']
        user_answer['motivation'] = request.form['about']
        user_answer['ready'] = request.form['accept']
        print(user_answer)
        print(request.form)
        return redirect('/answer')

@app.route('/answer')
def answer():
    return render_template('answer.html', **user_answer)

@app.route('/auto_answer')
def auto_answer():
    return render_template('answer.html', **auto_answerr)

if __name__ == '__main__':
    app.run(port=8080)