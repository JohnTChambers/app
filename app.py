from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from forms import InputDataForm
import pandas as pd
import sqlalchemy as db

from sql.sql_util import get_connection_string, set_up_session
from sql.sql_models import BasicGenomeData
from env import create_env_variables

app = Flask(__name__)

# import connection string locally
from env import create_env_variables
create_env_variables()

# set a secret key
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# routes
@app.route("/")
def main():
    return render_template("homepage.html")

@app.route("/hello_world")
def hello_world():
    return "Hello World!"

# @app.route("/application", methods=["GET", "POST"])
# def query_db():
#     form = InputDataForm()
#     if request.method == "POST":
#         # get string, connect to database, and set up session
#         create_env_variables()
#         connection_string = get_connection_string()
#         session, engine = set_up_session(connection_string)
#         # query records
#         records = session.query(AppData).filter(AppData.category == request.form["category"]).all()
#         return render_template("application.html", form=form, results=records)
#
#     return render_template("application.html", form=form)

@app.route("/application", methods=["GET", "POST"])
def query_db():
    form = InputDataForm()
    if request.method == "POST":
        # get string, connect to database, and set up session
        create_env_variables()
        connection_string = get_connection_string()
        session, engine = set_up_session(connection_string)
        # query records as a dataframe
        df = pd.read_sql_query(sql=db.select([BasicGenomeData]), con=engine)
        # display is based on option chosen
        if request.form["category"] == "Display All":
            return render_template("application.html", form=form, results=True, records=df.to_html())
        elif request.form["category"] == "Random":
            return render_template("application.html", form=form, results=True, records=df.sample().to_html())
        elif request.form["category"] == "Search":
            if request.form["search_term"] == "":
                return render_template("application.html", form=form, results=True, records="Please enter a search term")
            else:
                return render_template("application.html", form=form, results=True, records=df[df["species"].str.contains(request.form["search_term"])].to_html())

    return render_template("application.html", form=form)

@app.route("/cat-formatics")
def cat_formatics():
    return render_template("cat-formatics.html")

@app.route("/Marshmellow")
def marshemellow():
    return render_template("Marshmellow.html")