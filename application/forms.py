from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

# Form definitions for web input

class NameForm(FlaskForm):
    Stud_id = StringField("StudentId")
    SName = StringField("Surname")
    FName = StringField("firstName")
    submit = SubmitField("Submit")

class SubjectList(FlaskForm):
    subjlist = SelectField("Subject List", choices=[])
    submit = SubmitField("Submit")


class exampleSelectField(FlaskForm):
    list = SelectField("Farm Animals", choices=['cows','chickens','geese','llamas','sheep'])
    submit = SubmitField("Submit")