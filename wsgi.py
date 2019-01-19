##########
# IMPORTS #
###########
# Generic Flask Requirements
from flask import Flask, render_template
import os

basedir = os.path.abspath(os.path.dirname(__file__))


######################
# APPLICATION SETUPS #
######################
# `flask run` - runs application on local server
app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    instance_relative_config=True
)


# needed for deployment
# redundant for now
if __name__ == '__main__':
    app.run()

@app.route('/')
def home():
    # return 'Hello'
    return render_template('iframe.html')
