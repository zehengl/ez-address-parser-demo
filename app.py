import os

from ez_address_parser import AddressParser
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

from forms import AddressForm

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True

ap = AddressParser()


@app.route("/", methods=["get", "post"])
def index():
    form = AddressForm(request.form)

    result = ap.parse(form.address.data or "")

    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True)
