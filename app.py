"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# local modules
import config


# Get the application instance
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    return render_template("home.html"), 200


if __name__ == "__main__":
    app.run(debug=True)