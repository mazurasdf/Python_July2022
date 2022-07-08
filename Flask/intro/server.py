from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello_page():
    return "yooooo, it's the hello page!!!"

@app.route("/repeat/<phrase>")
def repeat_phrase(phrase):
    return f"your phrase is: {phrase}"

@app.route("/repeat/<phrase>/<int:times>")
def repeat_times(phrase, times):
    return (phrase + " ") * times

if __name__ == "__main__":
    app.run(debug=True)