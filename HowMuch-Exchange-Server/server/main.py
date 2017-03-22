from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    print('서버 시작')
    app.run('0.0.0.0')