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

# class SubjectList(FlaskForm):
#     subjlist = SelectField("Subject List", choices=[])
#     submit = SubmitField("Submit")


# class exampleSelectField(FlaskForm):
#     list = SelectField("Farm Animals", choices=['Submit','Delete','Show All'])
#     submit = SubmitField("Submit")