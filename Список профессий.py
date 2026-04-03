from flask import Flask, render_template

from render import render_style

app = Flask(__name__)

professions = '''инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, 
специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, 
киберинженер, штурман, пилот дронов'''.split(', ')


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    if list_type not in ['ol', 'ul']:
        return "Неверный параметр! Доступно: 'ol', 'ul'"
    return render_style('list.html', list_type=list_type, items=professions)


def main():
    print('http://127.0.0.1:8080/list_prof/ol')
    print('http://127.0.0.1:8080/list_prof/ul')
    app.run(port=8080)


if __name__ == '__main__':
    main()
