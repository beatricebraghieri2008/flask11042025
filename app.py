from flask import Flask, request, render_template
app = Flask(__name__)

lista=[54,95,2,36,18]

@app.route("/")
def hello():
    return render_template("index.html", lista=lista)

@app.route("/profilo")
def profilo():
    return "questa è la pagina profilo"


if __name__ == "__main__":
    app.run(debug=True)