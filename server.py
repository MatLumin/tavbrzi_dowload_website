import os 

from flask import Flask, render_template

import list_static_content

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



app:Flask = Flask("some website")


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@app.route("/")
@limiter.limit("10/day")
def index()->str:
	statics:List[str] = list_static_content.do_it()
	return render_template("index.html", statics=statics)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="7434", debug=True)