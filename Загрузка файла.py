from flask import Flask, request, url_for
from PIL import Image

app = Flask(__name__)

@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    temp = f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <h1>Форма для регистрации в суперсекретной системе</h1>
                        <div>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="photo">
                                </div>
                                <img src="{url_for('static', filename='img/img.jpg')}"
                                     alt="Сначала загрузите картинку">
                                <p></p>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''
    if request.method == 'GET':
        return temp
    if request.method == 'POST':
        img = Image.open(request.files['photo'])
        img.save(f'static/img/img.jpg')
        return temp


if __name__ == '__main__':
    app.run(port=8080)