from flask import Flask, render_template

# Create app instance
app = Flask(__name__)

@app.route("/")
def home():
	# return '<h1>Hello World</h1>'
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)