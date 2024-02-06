from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
@app.route('/promotion')
def index3():
    return """Человечество вырастает из детства.</br>
Человечеству мала одна планета.</br>
Мы сделаем обитаемыми безжизненные пока планеты.</br>
И начнем с Марса!</br>
Присоединяйся!"""


@app.route('/')
@app.route('/image_mars')
def index4():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
