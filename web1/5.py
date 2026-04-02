from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mars():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return '''Человечество вырастает из детства.</br>
Человечеству мала одна планета.</br>
Мы сделаем обитаемыми безжизненные пока планеты.</br>
И начнем с Марса!</br>
Присоединяйся!</br>
'''


@app.route('/image_mars')
def mars_image():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="https://avatars.mds.yandex.net/get-mpic/15269583/2a0000019a885f57ea752911a07bf65dc3e1/orig" 
             alt="здесь должна была быть картинка, но не нашлась">
        <p>Вот она какая, красная планета</p>
    </body>
    </html>'''


# @app.route('/bootstrap_sample')
# def bootstrap():
#     return '''<!doctype html>
#                 <html lang="en">
#                   <head>
#                     <meta charset="utf-8">
#                     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                     <link rel="stylesheet"
#                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                     crossorigin="anonymous">
#                     <title>Привет, Яндекс!</title>
#                   </head>
#                   <body>
#                     <h1>Привет, Яндекс!</h1>
#                     <div class="alert alert-primary" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-secondary" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-success" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-danger" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-warning" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-info" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-light" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                     <div class="alert alert-dark" role="alert">
#                       Этот HTML Bootstrapа просит!
#                     </div>
#                   </body>
#                 </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/style.css')}"/>
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://avatars.mds.yandex.net/get-mpic/15269583/2a0000019a885f57ea752911a07bf65dc3e1/orig"
         alt="здесь должна была быть картинка, но не нашлась">
    <div class="alert alert-dark" role="alert">
      Человечество вырастает из детства.
    </div>
    <div class="alert alert-success" role="alert">
      Человечеству мала одна планета.
    </div>
    <div class="alert alert-secondary" role="alert">
      Мы сделаем обитаемыми безжизненные пока планеты.
    </div>
    <div class="alert alert-warning" role="alert">
      И начнём с Марса!
    </div>
    <div class="alert alert-danger" role="alert">
      Присоединяйся!
    </div>
</body>
</html>
'''

@app.route('/astro', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 class="text-center">Анкета претендента</h1>
                            <h2 class="text-center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Никакого</option>
                                        </select>
                                    </div>
                                    <p></p>
                                    <p>Какие у Вас есть профессии</p>
                                    <div class="form-group">
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c1" name="c1">
                                            <label class="form-check-label" for="c1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c2" name="c2">
                                            <label class="form-check-label" for="c2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c2" name="c2">
                                            <label class="form-check-label" for="c2">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c1" name="c1">
                                            <label class="form-check-label" for="c1">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c2" name="c2">
                                            <label class="form-check-label" for="c2">Инженер по терраформированию</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c2" name="c2">
                                            <label class="form-check-label" for="c2">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c1" name="c1">
                                            <label class="form-check-label" for="c1">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="c2" name="c2">
                                            <label class="form-check-label" for="c2">Астрогеолог</label>
                                        </div>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        # print(request.form['email'])
        # print(request.form['password'])
        # print(request.form['class'])
        # print(request.form['file'])
        # print(request.form['about'])
        # print(request.form['accept'])
        # print(request.form['sex'])
        return "Форма отправлена"
    return None


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
