from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

# # Form definitions for web input

class NameForm(FlaskForm): #like creating a database version
    Stud_id = StringField("Student Id")
    SName = StringField("Surname")
    FName = StringField("firstName")
    submit = SubmitField("Submit")
    #delete = SubmitField("Delete")

class DelForm(FlaskForm): #like creating a database version
    Stud_id = StringField("Student Id")
    delete = SubmitField("Delete")

class SinForm(FlaskForm): #like creating a database version
    Stud_id = StringField("Student Id")
    submit = SubmitField("Submit")

# class ListOption(FlaskForm):
#     subjlist = SelectField("Subject List", choices=[])
#     submit = SubmitField("Submit")


class SelectFieldForm(FlaskForm):
    list = SelectField("SELECT ONE", choices=['All Student Page','All Moodle Page','Register A Student','Register A Moodle','Delete A Student','Home Page','Enter Student ID'])
    submit = SubmitField("Submit")