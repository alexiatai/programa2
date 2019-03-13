from flask import Flask, render_template
app = Flask(__name__)
@app.route("/alexia")

def hello():
	return render_template("listar.html")
app.run()