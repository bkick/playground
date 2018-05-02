from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<num>/<color>')
def  index(num, color):
	return render_template("index.html", num=int(num), color=color)
app.run(debug=True)