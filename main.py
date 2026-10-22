from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/products", methods=["GET"])
def products():
    return "Продукты"


@app.route("/info", methods=["GET"])
def info():
    return "Дополнительнвя информация"


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run()
