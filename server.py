import os 

from flask import Flask, render_template


import list_static_content

app:Flask = Flask("some website")


@app.route("/")
def index()->str:
	statics:List[str] = list_static_content.do_it()
	return render_template("index.html", statics=statics)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="7434", debug=True)