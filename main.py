from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products", methods=["GET"])
def products():
    return "Продукты"


@app.route("/info", methods=["GET"])
def info():
    return "Дополнительнвя информация"


if __name__ == '__main__':
    app.run()
