import datetime

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mypwd'
app.permanent_session_lifetime = datetime.timedelta(minutes=1440)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
