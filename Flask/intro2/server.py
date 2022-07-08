from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>/<color>/<int:times>")
def index(name, color, times):
    return render_template("index.html",name=name, color=color, times=times)

@app.route("/albums")
def albums():
    album_list = [
        {
            "cover_url": "/img/currents.png",
            "name":"currents",
            "artist":"tame impala"
        },
        {
            "cover_url": "/img/logic.jpg",
            "name":"The Incredible True Story",
            "artist":"Logic"
        },
        {
            "cover_url": "/img/illmatic.jpg",
            "name":"Illmatic",
            "artist":"Nas"
        }
    ]
    return render_template("albums.html", album_list=album_list)

if __name__ == "__main__":
    app.run(debug=True)