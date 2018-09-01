from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/sub/')
def sub():
    return 'This is a sub function.'



if __name__ == "__main__":
    app.run()