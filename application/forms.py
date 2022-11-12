from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class NameForm(FlaskForm):
    Stud_id = StringField("Student Id")
    SName = StringField("Surname")
    FName = StringField("firstName")
    submit = SubmitField("Submit")

class DelForm(FlaskForm): 
    Stud_id = StringField("Student Id")
    delete = SubmitField("Delete")
    submit = SubmitField("Exit")

class SinForm(FlaskForm): 
    Stud_id = StringField("Student Id")
    submit = SubmitField("Submit")

class MoodleForm(FlaskForm):
    Stud_id = StringField("Student Id")
    Modcode = StringField("Code List")
    Subname = StringField("Subject List")
    submit = SubmitField("Submit")


class SelectFieldForm(FlaskForm):
    list = SelectField("SELECT ONE", choices=['All Student Page','All Moodle Page','Register A Student','Register A Moodle','Delete A Student','Home Page','Enter Student ID','Update' ])
    submit = SubmitField("Submit")