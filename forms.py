from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class InputDataForm(FlaskForm):
    """
    A class that represents the input-data form that will be used in this application
    """

    category = SelectField('Application options :', choices=["Random", "Display All", "Search"], validate_choice=True)
    search_term = StringField("Species common name")