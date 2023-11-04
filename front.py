from flask import *

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET', 'POST'])
def run():
    if request.method == "Post":
        print(None)
        # rus_sm = request.form["rus_sm"]
    else:
        render_template("site.html")


def run():
    app.run()
