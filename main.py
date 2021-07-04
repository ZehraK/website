from flask import Flask, render_template


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/subscribed', methods=['GET', 'POST'])
def subscribed():
    return render_template('subscribed.html', scroll='subscribed')


if __name__ == '__main__':
    application.debug = False
    application.run()

